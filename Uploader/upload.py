import os
from azure.storage.blob import BlobServiceClient
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

def upload_files_to_blob_storage(settings_file):
    # Read settings from settings file
    settings = read_settings_file(settings_file)
    active_session_path = settings.get('active_session_path')

    if not active_session_path:
        print("Error: 'active_session_path' not found in settings.")
        return

    active_session_folders = os.listdir(active_session_path)

    if len(active_session_folders) != 1: 
        print(f"Error: There should be exactly one folder inside 'active_session'. Found: {len(active_session_folders)}")
        return

    session_id = active_session_folders[0]
    session_folder_path = os.path.join(active_session_path, session_id)

    # Create a BlobServiceClient
    connection_string = AzureConfig.CONNECTION_STRING
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a container named after the session ID if it doesn't exist
    container_name = session_id.lower()
    container_client = blob_service_client.get_container_client(container_name)
    if not container_client.exists():
        container_client.create_container()
    
    all_files_in_session = os.listdir(session_folder_path)
    final_list_of_files_to_upload = []

    # Total file size should not exceed 2 GB.
    total_file_size = get_total_size(session_folder_path)
    max_total_file_size = 2000000000 # 2 GB

    if total_file_size > max_total_file_size:
        print("Error: Total file size exceeds 2 GB.")
        return
    
    # Scan folder for unacceptable file extensions
    acceptable_file_extensions = ['.txt', '.csv', '.mp4', '.mp3', '.jpg', '.jpeg', '.png', '.xml', '.json', '.html']
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
            return
    
    # Scan folder for critical files
    critical_files_to_upload = ['user.txt', 'player.txt', 'hardware.txt', 'setup.txt', 'events.csv', 'system.csv', 'recording.mp4']
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
                return

    # Inside the session_folder_path create an 'others.txt' file with a list of all other files in the session folder that are not critical files
    other_files = [file_name for file_name in all_files_in_session if file_name not in critical_files_to_upload]
    with open(os.path.join(session_folder_path, 'others.txt'), 'w') as file:
        for file_name in other_files:
            file.write(file_name + '\n')

    # Upload all files in session folder
    print("Uploading files...")

    for file_name in all_files_in_session:
        file_path = os.path.join(session_folder_path, file_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"Uploaded '{file_name}' to '{container_name}' container.")
    
    # Delete the session folder after successful upload
    # if os.path.exists(session_folder_path):
    #     os.rmdir(session_folder_path)
    #     print(f"Session folder '{session_id}' deleted after successful upload.")

if __name__ == "__main__":
    settings_file_path = "settings.txt"

    upload_files_to_blob_storage(settings_file_path)
