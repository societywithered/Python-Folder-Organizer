from pathlib import Path
import shutil


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".md"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
}


def get_folder_name(file_path):
    """Choose a folder based on the file's extension."""
    extension = file_path.suffix.lower()

    for folder_name, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder_name

    return "Other"


def organize_folder(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.is_dir():
        print("That folder doesn't exist. Check the path and try again.")
        return

    moved_files = 0

    for item in folder.iterdir():
        # Only move files, not folders.
        if not item.is_file():
            continue

        destination_folder = folder / get_folder_name(item)
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / item.name

        # Avoid overwriting a file with the same name.
        if destination.exists():
            print(f"Skipped {item.name}: a file with that name already exists.")
            continue

        shutil.move(str(item), str(destination))
        print(f"Moved {item.name} into {destination_folder.name}/")
        moved_files += 1

    print(f"\nFinished! Organized {moved_files} file(s).")


def main():
    print("Folder Organizer")
    folder_path = input("Enter the folder path to organize: ").strip().strip('"')
    organize_folder(folder_path)


if __name__ == "__main__":
    main()