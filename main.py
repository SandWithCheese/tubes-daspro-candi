from data import load
import commands
import argparse
import os

# F13 - Load
# START
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", nargs="?")
args = parser.parse_args()
folder_directory = args.nama_folder

list_of_directories = os.listdir(".")
if folder_directory in os.listdir("."):
    print("Loading...")
    print('Selamat datang di program "Manajerial Candi"')
    print("Silahkan masukkan username Anda")
elif folder_directory:
    print(f'Folder "{folder_directory}" tidak ditemukan.')
    quit()
else:
    print("Tidak ada nama folder yang diberikan!")
    print()
    print("Usage: python main.py <nama_folder>")
    quit()
# END

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = []  # Matriks data user
candi = []  # Matriks data candi
bahan_bangunan = []  # Data bahan bangunan

load(f"{folder_directory}/user.csv", users)
load(f"{folder_directory}/candi.csv", candi)
load(f"{folder_directory}/bahan_bangunan.csv", bahan_bangunan)

while True:
    masukan = input(">>> ")
    # commands.run(masukan)
    if masukan == "login":
        pass
    elif masukan == "logout":
        pass
    elif masukan == "summonjin":
        pass
    elif masukan == "hapusjin":
        pass
    elif masukan == "ubahjin":
        pass
    elif masukan == "bangun":
        pass
    elif masukan == "kumpul":
        pass
    elif masukan == "batchkumpul":
        pass
    elif masukan == "batchbangun":
        pass
    elif masukan == "laporanjin":
        pass
    elif masukan == "laporancandi":
        pass
    elif masukan == "hancurkancandi":
        pass
    elif masukan == "ayamberkokok":
        pass
    elif masukan == "save":
        pass
    elif masukan == "help":
        pass
    elif masukan == "exit":
        pass
