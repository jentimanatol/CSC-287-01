import os
import json
import shutil
import sys
from datetime import datetime

REPLACEMENTS = {
    "enabled": {"status": "enabled", "since": "2024-10-01"},
    "disabled": {"status": "disabled", "since": "2024-10-01"},
    "manage_users": {"permission": "manage_users", "granted_at": "2024-10-05", "level": "full"},
    "view_content": {"permission": "view_content", "granted_at": "2024-09-25", "level": "read-only"}
}

def parse_args():
    if len(sys.argv) != 2:
        print("Usage: python batch_update_profiles.py <path_to_user_profiles>")
        sys.exit(1)
    return sys.argv[1]

def create_output_dir():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f"user_profiles_updated_{timestamp}"
    os.makedirs(output_dir)
    return output_dir

def update_profile_data(profile_data):
    def replace_value(value):
        if isinstance(value, str) and '@company.com' in value:
            return value.replace('@company.com', '@newcompany.com')
        elif value in REPLACEMENTS:
            return REPLACEMENTS[value]
        elif isinstance(value, list):
            return [replace_value(item) for item in value]
        elif isinstance(value, dict):
            return {k: replace_value(v) for k, v in value.items()}
        return value
    
    return {k: replace_value(v) for k, v in profile_data.items()}

def process_user_profiles(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        print(f"Checking directory: {root}")  # Log the directory being checked
        for file in files:
            print(f"Found file: {file}")  # Log the files found
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")  # Log the file being processed
                with open(file_path, 'r') as f:
                    try:
                        profile_data = json.load(f)
                    except json.JSONDecodeError as e:
                        print(f"Error reading JSON file {file_path}: {e}")
                        continue

                updated_data = update_profile_data(profile_data)

                output_path = os.path.join(output_dir, os.path.relpath(file_path, input_dir))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w') as f:
                    json.dump(updated_data, f, indent=4)
                print(f"Updated file saved to: {output_path}")  # Log the output file path

if __name__ == "__main__":
    input_dir = parse_args()
    output_dir = create_output_dir()
    process_user_profiles(input_dir, output_dir)
    print(f"Updated profiles have been saved to {output_dir}")
