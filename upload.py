import os
from azure.storage.blob import BlobServiceClient

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
        print("Error: There should be exactly one folder inside 'active_session'.")
        return

    session_id = active_session_folders[0]
    session_folder_path = os.path.join(active_session_path, session_id)

    # Azure Blob Storage credentials
    connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a container named after the session ID if it doesn't exist
    container_name = session_id.lower()
    container_client = blob_service_client.get_container_client(container_name)
    if not container_client.exists():
        container_client.create_container()

    # List of files to upload
    files_to_upload = [
        'user.txt', 'player.json', 'form.json',
        'hardware.json', 'setup.json', 'events.csv', 'system.csv'
    ]

    missing_files = []
    for file_name in files_to_upload:
        file_path = os.path.join(session_folder_path, file_name)
        if os.path.exists(file_path):
            # Upload file to Azure Blob Storage
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
        else:
            missing_files.append(file_name)

    if missing_files:
        print("The following files are missing and were not uploaded to Azure Blob Storage:")
        print(", ".join(missing_files))

    # Delete the session folder after successful upload
    if os.path.exists(session_folder_path):
        os.rmdir(session_folder_path)
        print(f"Session folder '{session_id}' deleted after successful upload.")

if __name__ == "__main__":
    settings_file_path = "settings.txt"

    upload_files_to_blob_storage(settings_file_path)
