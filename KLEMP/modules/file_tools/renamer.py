from pathlib import Path

def rename_files(folder):
    folder = Path(folder)

    if not folder.exists():
        print("Folder doesn't exist.")
        return

    prefix = input("Enter prefix: ")

    files = []

    for item in folder.iterdir():
        if item.is_file():
            files.append(item)

    if not files:
        print("No files found.")
        return

    print("\n=== PREVIEW ===")

    for item in files:
        old_name = item.name
        new_name = prefix + old_name

        print(f"{old_name} → {new_name}")

    confirm = input("\nRename these files? [y/N]: ")

    if confirm.lower() != "y":
        print("Cancelled.")
        return

    print("\n=== RENAMING ===")

    for item in files:
        old_name = item.name
        new_name = prefix + old_name

        item.rename(folder / new_name)

        print(f"{old_name} → {new_name}")

    print("\nDone!")