import json
from pathlib import Path
from models.user import User
from models.book import Book
from models.library import Library


def create_backup_folder():
    save_folder = Path(__file__).parent.parent / "DATA"
    if not save_folder.exists():
        save_folder.mkdir(parents=True)
    return save_folder


BACKUP_FOLDER = create_backup_folder()


def save_users(users):
    try:
        with open(BACKUP_FOLDER / "users.json", "w", encoding="utf-8") as file:
            json.dump([user.to_dict() for user in users], file, indent=4)
    except Exception as e:
        print(f"Error saving users: {e}")


def load_users():
    try:
        with open(BACKUP_FOLDER / "users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
            return [User.from_dict(user) for user in users]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON decoding error when loading users")
        return []


def save_books(books):
    try:
        with open(BACKUP_FOLDER / "books.json", "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in books], file, indent=4)
    except Exception as e:
        print(f"Error saving books: {e}")


def load_books():
    try:
        with open(BACKUP_FOLDER / "books.json", "r", encoding="utf-8") as file:
            books = json.load(file)
            return [Book.from_dict(book) for book in books]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON decoding error when loading books")
        return []


def save_library(library):
    try:
        with open(BACKUP_FOLDER / "library.json", "w", encoding="utf-8") as file:
            json.dump(library.to_dict(), file, indent=4)
    except Exception as e:
        print(f"Error saving library: {e}")


def load_library():
    try:
        with open(BACKUP_FOLDER / "library.json", "r", encoding="utf-8") as file:
            library = json.load(file)
            return [Library.from_dict(library)]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON decoding error when loading library")
        return []


if __name__ == "__main__":
    pass
