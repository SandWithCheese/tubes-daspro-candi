import data
import commands
import argparse
import os
import time

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
    elif masukan == "hapusjin" and isLoggedIn and user[2] == "bandung_bondowoso":
        username_jin = input("Masukkan username jin: ")
        if data.check_username(username_jin, users):
            yakin_hapus = input(
                f"Apakah anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)? ")
            print()
            if yakin_hapus == "Y":
                users = commands.hapus_jin(username_jin, users)
                print("Jin telah berhasil dihapus dari alam gaib.")
            elif yakin_hapus == "N":
                print("Jin tidak dihapus dari alam gaib.")
            else:
                print("Masukan tidak valid.")
        else:
            print()
            print("Tidak ada jin dengan username tersebut.")
    elif masukan == "ubahjin" and isLoggedIn and user[2] == "bandung_bondowoso":
        username_jin = input("Masukkan username jin: ")
        if data.check_username(username_jin, users):
            tipe_jin = data.check_tipe(username_jin, users)
            if tipe_jin == "jin_pengumpul":
                yakin_ubah = input(
                    'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ')
            else:
                yakin_ubah = input(
                    'Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ')
            print()
            if yakin_ubah == "Y":
                users = commands.ubah_tipe_jin(username_jin, users, tipe_jin)
                print("Jin telah berhasil diubah.")
            elif yakin_ubah == "N":
                print("Jin tidak diubah.")
            else:
                print("Masukan tidak valid.")
        else:
            print()
            print("Tidak ada jin dengan username tersebut.")
    elif masukan == "bangun":
        pass
    elif masukan == "kumpul" and isLoggedIn and user[2] == "jin_pengumpul":
        bahan = []
        for i in range(3):
            time.sleep(5/1000)
            bahan = bahan + [data.randrange(0, 5)]
        print(
            f"Jin menemukan {bahan[0]} pasir, {bahan[1]} batu, dan {bahan[2]} air.")
        bahan_bangunan = commands.kumpul(
            bahan[0], bahan[1], bahan[2], bahan_bangunan)
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
    # ONLY FOR DEBUG
    print(users)
