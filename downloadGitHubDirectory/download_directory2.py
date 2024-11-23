import requests
import zipfile
import os
from io import BytesIO

# URL of the repository ZIP file
repo_url = "https://github.com/pradeepselvakumar/oopl/archive/refs/heads/main.zip"
# Directory to extract
target_dir = "oopl-main/HW4-Json"
# Output directory
output_dir = "HW4-Json"

# Download the repository ZIP file
response = requests.get(repo_url)
if response.status_code == 200:
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        # Extract the specific directory
        for member in z.namelist():
            if member.startswith(target_dir):
                # Extract the file
                z.extract(member, output_dir)
                # Move the file to the correct location
                extracted_path = os.path.join(output_dir, member)
                final_path = os.path.join(output_dir, os.path.relpath(member, target_dir))
                if not os.path.exists(final_path):
                    os.makedirs(os.path.dirname(final_path), exist_ok=True)
                    os.rename(extracted_path, final_path)
                else:
                    print(f"Path already exists: {final_path}")
        # Clean up the empty directories
        for root, dirs, files in os.walk(output_dir):
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
    print(f"Directory '{target_dir}' has been downloaded and extracted to '{output_dir}'")
else:
    print(f"Failed to download the repository: {response.status_code}")
