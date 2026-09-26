import os
import shutil

CATEGORIES = {
    # executables and scripts
    ".exe": "EXECUTABLES",
    ".msi": "EXECUTABLES",
    ".bat": "EXECUTABLES",
    ".cmd": "EXECUTABLES",
    ".sh": "EXECUTABLES",
    ".vbs": "EXECUTABLES",
    ".ps1": "EXECUTABLES",
    ".apk": "EXECUTABLES",
    ".app": "EXECUTABLES",
    ".gadget": "EXECUTABLES",

    # images
    ".png": "IMAGES",
    ".jpg": "IMAGES",
    ".jpeg": "IMAGES",
    ".gif": "IMAGES",
    ".bmp": "IMAGES",
    ".webp": "IMAGES",
    ".ico": "IMAGES",
    ".tiff": "IMAGES",
    ".tif": "IMAGES",
    ".heic": "IMAGES",
    ".svg": "IMAGES",
    ".psd": "IMAGES",
    ".ai": "IMAGES",
    ".raw": "IMAGES",

    # documents and text
    ".doc": "DOCUMENTS",
    ".docx": "DOCUMENTS",
    ".pdf": "DOCUMENTS",
    ".txt": "DOCUMENTS",
    ".rtf": "DOCUMENTS",
    ".odt": "DOCUMENTS",
    ".pages": "DOCUMENTS",
    ".tex": "DOCUMENTS",
    ".wpd": "DOCUMENTS",

    # tables
    ".xls": "SPREADSHEETS",
    ".xlsx": "SPREADSHEETS",
    ".xlsm": "SPREADSHEETS",
    ".csv": "SPREADSHEETS",
    ".ods": "SPREADSHEETS",

    # presentations
    ".ppt": "PRESENTATIONS",
    ".pptx": "PRESENTATIONS",
    ".pps": "PRESENTATIONS",
    ".key": "PRESENTATIONS",

    # audio
    ".mp3": "AUDIO",
    ".wav": "AUDIO",
    ".flac": "AUDIO",
    ".aac": "AUDIO",
    ".ogg": "AUDIO",
    ".m4a": "AUDIO",
    ".wma": "AUDIO",
    ".mid": "AUDIO",
    ".midi": "AUDIO",

    # video
    ".mp4": "VIDEO",
    ".mkv": "VIDEO",
    ".avi": "VIDEO",
    ".mov": "VIDEO",
    ".wmv": "VIDEO",
    ".flv": "VIDEO",
    ".webm": "VIDEO",
    ".m4v": "VIDEO",
    ".3gp": "VIDEO",
    ".mpeg": "VIDEO",
    ".mpg": "VIDEO",

    # archives
    ".zip": "ARCHIVES",
    ".rar": "ARCHIVES",
    ".7z": "ARCHIVES",
    ".tar": "ARCHIVES",
    ".gz": "ARCHIVES",
    ".bz2": "ARCHIVES",
    ".xz": "ARCHIVES",
    ".iso": "ARCHIVES",
    ".dmg": "ARCHIVES",

    # source code + programs
    ".py": "CODE",
    ".js": "CODE",
    ".html": "CODE",
    ".css": "CODE",
    ".cpp": "CODE",
    ".c": "CODE",
    ".cs": "CODE",
    ".java": "CODE",
    ".json": "CODE",
    ".xml": "CODE",
    ".php": "CODE",
    ".rb": "CODE",
    ".swift": "CODE",
    ".go": "CODE",
    ".ts": "CODE",

    # databases
    ".sql": "DATABASES",
    ".db": "DATABASES",
    ".sqlite": "DATABASES",
    ".mdb": "DATABASES",

    # ebooks
    ".epub": "BOOKS",
    ".fb2": "BOOKS",
    ".mobi": "BOOKS",
    ".djvu": "BOOKS",

    # fonts
    ".ttf": "FONTS",
    ".otf": "FONTS",
    ".woff": "FONTS",
    ".woff2": "FONTS",

    # 3d graphics
    ".obj": "3D_MODELS",
    ".fbx": "3D_MODELS",
    ".stl": "3D_MODELS",
    ".blend": "3D_MODELS",
    ".3ds": "3D_MODELS",

    # torrents and jars
    ".torrent": "TORRENTS",
    ".jar": "JARS",
}


def get_unique_path(folder_path, filename):
    file_path = os.path.join(folder_path, filename)

    if not os.path.exists(file_path):
        return file_path

    name, extension = os.path.splitext(filename)
    counter = 1

    while True:
        new_name = f"{name}_{counter}{extension}"
        new_path = os.path.join(folder_path, new_name)

        if not os.path.exists(new_path):
            return new_path

        counter += 1


def sort(path):
    inside = os.listdir(path)

    for f in inside:
        file_path = os.path.join(path, f)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(f)[1].lower()

        if file_ext in CATEGORIES:
            folder = CATEGORIES[file_ext]
        else:
            folder = "UNKNOWN"

        folder_path = os.path.join(path, folder)
        os.makedirs(folder_path, exist_ok=True)

        destination = get_unique_path(folder_path, f)

        shutil.move(file_path, destination)


# interface
print("- hello, this is SORTER")

sort(input("What folder do you want to sort (insert full path): "))
