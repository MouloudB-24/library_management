import json
from pathlib import Path
from models.library import Library


def create_backup_folder():
    """
    Create a backup folder if it doesn't exist.
    """
    save_folder = Path(__file__).parent.parent / "DATA"
    if not save_folder.exists():
        save_folder.mkdir(parents=True)
    return save_folder


BACKUP_FOLDER = create_backup_folder()


def save_library(library):
    """
    Save the library in JSON file.
    """
    try:
        with open(BACKUP_FOLDER / "library.json", "w", encoding="utf-8") as file:
            json.dump(library.to_dict(), file, indent=4)
    except Exception as e:
        print(f"Error saving library: {e}")


def load_library():
    """
    Load library from JSON file.
    """
    try:
        with open(BACKUP_FOLDER / "library.json", "r", encoding="utf-8") as file:
            library = json.load(file)
            return Library.from_dict(library)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("JSON decoding error when loading library")
        return {}


if __name__ == "__main__":
    pass
