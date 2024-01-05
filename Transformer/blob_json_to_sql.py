from azure.storage.blob import BlobServiceClient
import os
from sql_generator import generate_insert_from_json

# Azure Blob Storage credentials and container information
connection_string = "CONNECTION_STRING"
container_name = "CONTAINER_NAME"
table_name = 'destination'
example_sql_output_path = "Transformer/output.sql"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

local_directory = "local_directory_path"
os.makedirs(local_directory, exist_ok=True)

# List all blobs in the container
blobs = container_client.list_blobs()
for blob in blobs:
    if blob.name.endswith('.json'):
        blob_client = container_client.get_blob_client(blob)
        download_path = os.path.join(local_directory, blob.name)
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        
        sql_insert = generate_insert_from_json(download_path, table_name)
        with open(example_sql_output_path, 'a') as f:
            f.write(sql_insert + '\n')
