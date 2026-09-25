import shutil

from pathlib import Path

FILE_TYPES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".mkv": "Videos",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".py": "Python",
    ".js": "Programming",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
}


def organize(folder):
    folder = Path(folder)

    if not folder.exists():
        print("Folder doesn't exist.")
        return

    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower()
            category = FILE_TYPES.get(extension, "Others")

            category_folder = folder / category
            category_folder.mkdir(exist_ok=True)

            destination = category_folder / item.name
            shutil.move(item, destination)

            print(f"{item.name} → {category}")


        elif item.is_dir():
            print(f"FOLDER: {item.name}")


if __name__ == "__main__":
    organize(r"C:\Users\genki\KLEMP\tests")