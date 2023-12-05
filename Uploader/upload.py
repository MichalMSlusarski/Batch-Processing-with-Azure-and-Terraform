import os
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import AzureError
from config import AzureConfig

def get_total_size(folder_path):
    total_size = 0
    for path, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)
    print(f"Total size: {total_size}")        
    return total_size

def read_settings_file(settings_file):
    settings = {}
    with open(settings_file, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            settings[key] = value
    return settings

def read_and_validate_settings(settings_file):
    # Read settings from settings file
    settings = read_settings_file(settings_file)
    active_session_path = settings.get('active_session_path')

    if not active_session_path:
        print("Error: 'active_session_path' not found in settings.")
        return None

    return active_session_path

def get_session_id_and_path(active_session_path):
    active_session_folders = os.listdir(active_session_path)

    if len(active_session_folders) != 1: 
        print(f"Error: There should be exactly one folder inside 'active_session'. Found: {len(active_session_folders)}")
        return None, None

    session_id = active_session_folders[0]
    session_folder_path = os.path.join(active_session_path, session_id)

    return session_id, session_folder_path

def create_blob_service_and_container(session_id):
    connection_string = AzureConfig.CONNECTION_STRING
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a container named after the session ID if it doesn't exist
    container_name = session_id.lower()
    container_client = blob_service_client.get_container_client(container_name)
    if not container_client.exists():
        container_client.create_container()

    return blob_service_client, container_name

def validate_file_size_and_extensions(session_folder_path, all_files_in_session, max_total_file_size, acceptable_file_extensions):
    # Total file size should not exceed 2 GB.
    total_file_size = get_total_size(session_folder_path)

    if total_file_size > max_total_file_size:
        print("Error: Total file size exceeds 2 GB.")
        return False

    # Scan folder for unacceptable file extensions
    for file_name in all_files_in_session:
        file_extension = os.path.splitext(file_name)[1]
        if file_extension not in acceptable_file_extensions:
            print(f"Error: '{file_name}' has an unacceptable file extension. You must delete the file to continue. Delete? (y/n)")
            user_input = input()
            if user_input.lower() == 'y':
                os.remove(os.path.join(session_folder_path, file_name))
                continue
            else:
                print("Upload cancelled.")
            return False

    return True

def validate_critical_files(all_files_in_session, critical_files_to_upload):
    # Scan folder for critical files
    for file_name in critical_files_to_upload:
        if file_name in all_files_in_session:
            continue
        else:
            print(f"Error: '{file_name}' not found in session folder. Would you like to upload anyway? (y/n)")
            user_input = input()
            if user_input.lower() == 'y':
                continue
            else:
                print("Upload cancelled.")
                return False

    return True

def create_others_file(session_folder_path, all_files_in_session, critical_files_to_upload):
    # Inside the session_folder_path create an 'others.txt' file with a list of all other files in the session folder that are not critical files
    
    other_files = [file_name for file_name in all_files_in_session if file_name not in critical_files_to_upload]
    with open(os.path.join(session_folder_path, 'others.txt'), 'w') as file:
        for file_name in other_files:
            file.write(file_name + '\n')
    
    all_files_in_session.append('others.txt')


def upload_files(blob_service_client, container_name, session_folder_path, all_files_in_session):
    # Upload all files in session folder
    print("Uploading files...")

    for file_name in all_files_in_session:
        file_path = os.path.join(session_folder_path, file_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
            print(f"Uploaded '{file_name}' to '{container_name}' container.")
        except AzureError as e:
            print(f"Failed to upload '{file_name}'. AzureError: {e}")
        except Exception as e:
            print(f"Failed to upload '{file_name}'. Exception: {e}")
    
    # Delete the session folder after successful upload
    # if os.path.exists(session_folder_path):
    #     os.rmdir(session_folder_path)
    #     print(f"Session folder '{session_id}' deleted after successful upload.")

def main(settings_file, acceptable_file_extensions, critical_files_to_upload):
    max_total_file_size = 2000000000 # 2 GB
    active_session_path = read_and_validate_settings(settings_file)
    if not active_session_path:
        return

    session_id, session_folder_path = get_session_id_and_path(active_session_path)
    if not session_id or not session_folder_path:
        return

    blob_service_client, container_name = create_blob_service_and_container(session_id)

    all_files_in_session = os.listdir(session_folder_path)

    if not validate_file_size_and_extensions(session_folder_path, all_files_in_session, max_total_file_size, acceptable_file_extensions):
        return

    if not validate_critical_files(all_files_in_session, critical_files_to_upload):
        return

    create_others_file(session_folder_path, all_files_in_session, critical_files_to_upload)

    upload_files(blob_service_client, container_name, session_folder_path, all_files_in_session)

if __name__ == "__main__":
    settings_file_path = "Uploader\\settings.txt"
    acceptable_file_extensions = ['.txt', '.csv', '.mp4', '.mp3', '.jpg', '.jpeg', '.png', '.xml', '.json', '.html']
    critical_files_to_upload = ['user.json', 'player.json', 'hardware.json', 'setup.json', 'events.csv', 'system.csv', 'recording.mp4']

    try:
        main(settings_file_path, acceptable_file_extensions, critical_files_to_upload)

    except Exception as ex:
        print('Exception:')
        print(ex)
