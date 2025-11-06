from azure.storage.blob import BlobServiceClient
import os
from pathlib import Path

def upload():
    conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if not conn_str:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING not set")

    infile = Path("data/processed/recommendations.csv")
    if not infile.exists():
        raise FileNotFoundError(f"{infile} not found. Run pipeline first.")

    container = os.getenv("AZURE_BLOB_CONTAINER", "price-data")
    client = BlobServiceClient.from_connection_string(conn_str)
    container_client = client.get_container_client(container)
    try:
        container_client.create_container()
    except Exception:
        pass

    with open(infile, "rb") as f:
        container_client.upload_blob(name=infile.name, data=f, overwrite=True)
    print(f"✅ Uploaded {infile} to container {container}")

if __name__ == "__main__":
    upload()
