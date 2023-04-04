import data
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

users = data.load(f"{folder_directory}/user.csv", users)
candi = data.load(f"{folder_directory}/candi.csv", candi)
bahan_bangunan = data.load(
    f"{folder_directory}/bahan_bangunan.csv", bahan_bangunan)

user = []
isLoggedIn = False

while True:
    masukan = input(">>> ")
    # commands.run(masukan)
    if masukan == "login" and not isLoggedIn:
        username = input("Username: ")
        password = input("Password: ")
        user = commands.login(username, password, users)

        if user[0] and user[1]:
            print()
            print(f"Selamat datang, {user[0]}")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            isLoggedIn = True
        elif not user[0]:
            print()
            print("Username tidak terdaftar!")
        elif not user[1]:
            print()
            print("Password salah!")
    elif masukan == "logout" and isLoggedIn:
        user = commands.logout()
        isLoggedIn = False
    elif masukan == "summonjin" and isLoggedIn and user[2] == "bandung_bondowoso":
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        print()
        users = commands.summon_jin(users)

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
        commands.help(user)
    elif masukan == "exit":
        pass
    else:
        print("Masukan tidak valid")
