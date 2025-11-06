from azure.storage.blob import BlobServiceClient
import os

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container = "price-data"

service = BlobServiceClient.from_connection_string(connect_str)
client = service.get_container_client(container)
client.upload_blob(
    name="recommendations.csv",
    data=open("data/processed/recommendations.csv", "rb"),
    overwrite=True
)
print("📤 Uploaded recommendations.csv to Azure Data Lake container.")
