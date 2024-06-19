import gdown
import os

files = [
    {"id": "1Toaeg1spKMOMvFMLRUaFcjH0rRStGQK0", "name": "data/fondo_Co_1200V_170t1_5min.dat"},
    {"id": "1YSUqibib-JbuSJAjgLLqp-pn-GbyJwgv", "name": "data/fondo_10cm_plomo_1200V_170t1_5min.dat"},
    {"id": "18a_Xpv6HfIspJCy1q5FFHE4BL1SJ4MAF", "name": "data/fondo_10cm_noplomo_1200V_170t1_5min.dat"},
    {"id": "1BOnxVzMR0ZX0zUn6hZP1n8YLCKfACcps", "name": "data/Co_1200V_170t1_5min.dat"},
    {"id": "1BsmEN-1ruPRchGM0RLmtCo8cl8vQmhd5", "name": "data/AmBe_30cm_10cm_plomo_1200V_650t1_5min.dat"},
    {"id": "1AT9OqZ95KrGwCKV7Myjt-q_3nSkloNyL", "name": "data/AmBe_30cm_10cm_noplomo_1200V_650t1_5min.dat"},
]

if not os.path.exists('data'):
    os.makedirs('data')

for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    output = file["name"]
    gdown.download(url, output, quiet=False)

print("All files have been downloaded")
