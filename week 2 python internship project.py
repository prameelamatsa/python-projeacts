from pathlib import Path
import shutil

# 1. Define category mappings based on file extensions
EXTENSION_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".psd"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".odt", ".epub"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json", ".sql", ".ts"]
}

def get_category(extension):
    """Determine the folder category based on file extension."""
    ext = extension.lower()
    for category, extensions in EXTENSION_MAPPING.items():
        if ext in extensions:
            return category
    return "Others"  # Fallback folder for unknown extensions

def get_unique_destination(dest_path: Path) -> Path:
    """Generate a unique file path if a file with the same name already exists."""
    if not dest_path.exists():
        return dest_path
    
    directory = dest_path.parent
    stem = dest_path.stem
    suffix = dest_path.suffix
    counter = 1
    
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_path = directory / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def organize_files(target_directory):
    """Sorts files in the target directory into category subfolders."""
    target_dir = Path(target_directory)
    
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: {target_directory} is not a valid directory.")
        return

    print(f"\n--- Organizing directory: {target_dir.resolve()} ---")
    
    # Iterate through files in the directory
    for item in target_dir.iterdir():
        # Process files only (skip subfolders so we don't reorganize already sorted folders)
        if item.is_file():
            extension = item.suffix
            category = get_category(extension)
            
            # Create category subfolder if it doesn't exist
            category_dir = target_dir / category
            category_dir.mkdir(exist_ok=True)
            
            # Determine destination path with collision avoidance
            destination = category_dir / item.name
            unique_destination = get_unique_destination(destination)
            
            # Move the file safely
            shutil.move(str(item), str(unique_destination))
            print(f"Moved: {item.name} -> {category}/{unique_destination.name}")

    print("\nOrganization complete!\n")

if __name__ == "__main__":
    # Ask the user to type or paste the path of the folder they want to organize
    print("=== Automatic File Organizer ===")
    user_path = input("Enter the full path of the folder you want to organize: ").strip()
    
    # Remove surrounding quotes if the user dragged and dropped the folder into the terminal
    user_path = user_path.strip('"').strip("'")
    
    if user_path:
        organize_files(user_path)
    else:
        print("No path provided. Exiting program.")