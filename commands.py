import data


# F01 - Login
# START
def login(username: str, password: str, users: list) -> list:
    valid_user = []
    for user in users:
        if username == user[0]:
            valid_user = valid_user + [username]
            break
    else:
        valid_user = valid_user + [False]

    for user in users:
        if username == user[0] and password == user[1]:
            valid_user = valid_user + [password]
            valid_user = valid_user + [user[2]]
            break
    else:
        valid_user = valid_user + [False]

    return valid_user
# END


# F02 - Logout
# START
def logout() -> list:
    return []
# END


# F15 - Help
# START
def help(user: list):
    print("=========== HELP ===========")
    if user == []:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. help")
        print("   Untuk menampilkan semua command yang dapat digunakan")
        print("4. exit")
        print("   Untuk keluar dari permainan")
    elif user[2] == "bandung_bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin dari dunia lain")
        print("3. hapusjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengerahkan seluruh pasukan jin untuk membangun candi")
        print("7. laporanjin")
        print("   Untuk mengambil laporan jin untuk mengetahui kinerja para jin")
        print("8. laporancandi")
        print("   Untuk mengambil laporan candi untuk mengetahui proses pembangunan candi")
        print("9. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("10.save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        print("11.help")
        print("   Untuk menampilkan semua command yang dapat digunakan")
        print("12.exit")
        print("   Untuk keluar dari permainan")
    elif user[2] == "roro_jonggrang":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari")
        print("4. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("5. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        print("6. help")
        print("   Untuk menampilkan semua command yang dapat digunakan")
        print("7. exit")
        print("   Untuk keluar dari permainan")
    elif user[2] == "jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")
        print("3. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("4. help")
        print("   Untuk menampilkan semua command yang dapat digunakan")
        print("5. exit")
        print("   Untuk keluar dari permainan")
    elif user[2] == "jin_pembangun":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")
        print("3. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("4. help")
        print("   Untuk menampilkan semua command yang dapat digunakan")
        print("5. exit")
        print("   Untuk keluar dari permainan")
# END


# F03 - Summon Jin
# START
def summon_jin(users: list) -> list:
    while True:
        nomor_jin = int(
            input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        print()
        if nomor_jin == 1:
            print('Memilih jin "Pengumpul".')
            print()
            users = data.panggil_jin(users, "jin_pengumpul")
            return users
        elif nomor_jin == 2:
            print('Memilih jin "Pembangun".')
            print()
            users = data.panggil_jin(users, "jin_pembangun")
            return users
        else:
            print(f'Tidak ada jenis jin bernomor "{nomor_jin}"!')
            print()
# END


# F04 - Hilangkan Jin
# START
def hapus_jin(username: str, users: list) -> list:
    new_users = []
    for user in users:
        if user[0] == username:
            continue
        new_users = new_users + [user]
    return new_users
# END


# F05 - Ubah Tipe Jin
# START
def ubah_tipe_jin(username: str, users: list, tipe_jin: str) -> list:
    for user in users:
        for user in users:
            if user[0] == username:
                if tipe_jin == "jin_pengumpul":
                    user[2] = "jin_pembangun"
                else:
                    user[2] = "jin_pengumpul"
    return users
# END


# F07 - Jin Pengumpul
# START
def kumpul(pasir: int, batu: int, air: int, bahan_bangunan: list) -> list:
    if data.list_len(bahan_bangunan) == 1:
        bahan_bangunan = bahan_bangunan + [["pasir", "Pasir alami dari sungai terdekat", 0], [
            "batu", "Batu alami yang kokoh", 0], ["air", "Air jernih dari sungai terdekat", 0]]

    bahan_bangunan[1][2] += pasir
    bahan_bangunan[2][2] += batu
    bahan_bangunan[3][2] += air
    return bahan_bangunan
# END
