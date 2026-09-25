from modules.file_tools.organizer import organize
from modules.file_tools.renamer import rename_files
from modules.file_tools.duplicates import find_duplicates

from modules.utility_tools.calculator import calculate
from modules.utility_tools.converter import convert
from tkinter import Tk, filedialog
def file_tools():
    while True:
        print("\n=== FILE TOOLS ===")
        print("1. Organize Files")
        print("2. Rename Files")
        print("3. Find Duplicates")
        print("0. Back to Main Menu")
        choice = input("\nSelect: ")

        if choice == "1":
            root = Tk()
            root.withdraw()

            folder = filedialog.askdirectory(title="Select folder to organize")

            root.destroy()

            if folder:
                organize(folder)

        elif choice == "2":
            print("DEBUG 1: Option 2 works")

            root = Tk()
            root.withdraw()

            print("DEBUG 2: Folder picker starting")

            folder = filedialog.askdirectory(
                title="Select folder to rename files"
            )

            print("DEBUG 3: Picker finished")
            print("Selected folder:", folder)

            root.destroy()

            if folder:
                print("DEBUG 4: Calling rename_files")
                rename_files(folder)
            else:
                print("DEBUG 4: No folder selected")

        elif choice == "3":
            root = Tk()
            root.withdraw()

            folder = filedialog.askdirectory(title="Select folder to check for duplicates")

            root.destroy()

            if folder:
                find_duplicates(folder)
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def utility_tools():
    while True:
        print("\n=== UTILITY TOOLS ===")
        print("1. Calculator")
        print("2. Tool 2")
        print("3. Tool 3")
        print("0. Back to Main Menu")
        choice = input("\nSelect: ")

        if choice == "1":
            print("calculator selected.")
            calculate()

        elif choice == "2":
            print("Converter selected.")
            convert()
        elif choice == "3":
            print("Tool 3 selected.")
            # Add functionality for Tool 3 here

        elif choice == "0":
            break
        else:
            print("Invalid option.")

def start():
    while True:
        print("""   
        ██╗  ██╗██╗     ███████╗███╗   ███╗██████╗
        ██║ ██╔╝██║     ██╔════╝████╗ ████║██╔══██╗
        █████╔╝ ██║     █████╗  ██╔████╔██║██████╔╝
        ██╔═██╗ ██║     ██╔══╝  ██║╚██╔╝██║██╔═══╝
        ██║  ██╗███████╗███████╗██║ ╚═╝ ██║██║
        ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝
        """)
        print("1. File Tools")
        print("2. System Tools")
        print("3. Network Tools")
        print("4. Security Tools")
        print("5. Utility Tools")
        print("6. Python Tools")
        print("0. Exit")

        choice = input("\nSelect: ")

        if choice == "1":
            file_tools()
        elif choice == "5":
            utility_tools()

        elif choice == "0":
            print("KLEMP shutting down...")
            break

        else:
            print("Invalid option.")
