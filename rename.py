import os

# Set the target folder
# folder = "defense"  # Change this to your folder path
# folder_path = os.path.join("\dataset", folder)
folder_path = "dataset/passing"
# Ensure the folder exists
print(folder_path)

if not os.path.exists(folder_path):
    print("Error: Folder does not exist.")
    exit()

# Get all files in the folder
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Sort files (optional: sorts by name to ensure ordered numbering)
files.sort()

# Rename files in the format {filename}_{num}
for index, file in enumerate(files, start=1):
    file_name, file_ext = os.path.splitext(file)  # Extract name and extension
    prefix = folder_path.split("/")[1]
    # prefix = "temp"
    new_name = f"{prefix}_{index}{file_ext}"  # Append number
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {file} → {new_name}")

print("Renaming completed!")
