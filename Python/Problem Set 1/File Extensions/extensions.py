# extensions.py - By Charan Katyal

# Prompt the user for a file name
filename = input("Enter the name of a file: ").strip().lower()

# Dictionary to map file extensions to their respective media types
media_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Check the file's extension and output the corresponding media type
for ext, media_type in media_types.items():
    if filename.endswith(ext):
        print(media_type)
        break
else:
    print("application/octet-stream")
