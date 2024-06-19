# Project

This project contains large data files that are not stored directly in the repository due to their size. To download the original files, please follow the instructions below:

## Download Files

1. Ensure you have `gdown` installed. If not, you can install it using `pip`:

    ```sh
    pip install gdown
    ```

2. Run the `download_files.py` script to download the files from Google Drive:

    ```sh
    python download_files.py
    ```

   This script will download all the required files into the `data/` directory.

## Script Details

The `download_files.py` script includes a list of Google Drive file IDs and their respective output filenames. The script uses these IDs to download the files and save them in the specified directory. Below is the content of the `download_files.py` script:

```python
import gdown
import os

# List of Google Drive file IDs and their corresponding output names
files = [
    {"id": "1Toaeg1spKMOMvFMLRUaFcjH0rRStGQK0", "name": "data/fondo_Co_1200V_170t1_5min.dat"},
    {"id": "1YSUqibib-JbuSJAjgLLqp-pn-GbyJwgv", "name": "data/fondo_10cm_plomo_1200V_170t1_5min.dat"},
    {"id": "1ABCD3EFG4HIJK5LMNOP6QRST7UVWX8YZ", "name": "data/file3.ext"},
    {"id": "1ABCDE2FGHIJK3LMNOP4QRST5UVWXY6Z7", "name": "data/file4.ext"},
    {"id": "1ABCDEFG2HIJKLM3NOPQRST4UVWXY5Z6", "name": "data/file5.ext"},
    {"id": "1ABCDEFGH2IJKL3MNOPQRST4UVWXY5Z6", "name": "data/file6.ext"},
]

# Create the 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Download each file
for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    gdown.download(url, output, quiet=False)

print("All files have been downloaded.")


