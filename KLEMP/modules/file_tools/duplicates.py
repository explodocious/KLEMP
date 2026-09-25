from pathlib import Path
import hashlib


def get_hash(file):
    hasher = hashlib.md5()

    with open(file, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder):
    folder = Path(folder)

    if not folder.exists():
        print("Folder doesn't exist.")
        return

    hashes = {}

    for item in folder.iterdir():
        if item.is_file():
            file_hash = get_hash(item)

            print(f"{item.name} → {file_hash}")

            if file_hash in hashes:
                print(f"DUPLICATE: {item.name}")
            else:
                hashes[file_hash] = item.name