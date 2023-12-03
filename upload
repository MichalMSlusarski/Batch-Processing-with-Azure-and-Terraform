import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContentSettings

def upload_files_to_blob_storage(session_id, temp_folder_path):
    # Azure Blob Storage credentials
    connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a container named after the session ID if it doesn't exist
    container_name = session_id.lower()  # Ensure lowercase for container name
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
        file_path = os.path.join(temp_folder_path, file_name)
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
        # You can also notify the user or handle the missing files according to your requirements

# Usage
if __name__ == "__main__":
    session_id = "YOUR_SESSION_ID"  # Replace with your session ID
    temp_folder_path = "PATH_TO_TEMP_FOLDER"  # Replace with your temporary folder path

    upload_files_to_blob_storage(session_id, temp_folder_path)
