import data
import time


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
        nomor_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        print()
        if nomor_jin == "1":
            print('Memilih jin "Pengumpul".')
            print()
            users = data.panggil_jin(users, "jin_pengumpul")
            return users
        elif nomor_jin == "2":
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
    if data.length(bahan_bangunan) == 1:
        bahan_bangunan = bahan_bangunan + [["pasir", "Pasir alami dari sungai terdekat", 0], [
            "batu", "Batu alami yang kokoh", 0], ["air", "Air jernih dari sungai terdekat", 0]]

    bahan_bangunan[1][2] += pasir
    bahan_bangunan[2][2] += batu
    bahan_bangunan[3][2] += air
    return bahan_bangunan
# END


# F06 - Jin Pembangun
# START
def bangun(pasir: int, batu: int, air: int, candi: list, user: str) -> list:
    if data.length(candi) == 1:
        candi = candi + [[1, user, pasir, batu, air]]
    else:
        for i in candi:
            if i == []:
                candi = candi + [[i[-1][0] + 1, user, pasir, batu, air]]
                break
        else:
            candi = candi + [[candi[-1][0] + 1, user, pasir, batu, air]]

    return candi
# END


# F08 - Batch Kumpul/Bangun
# START
def batchkumpul(bahan_bangunan: list, users: list) -> list:
    total_pengumpul = 0
    for user in users:
        if user[2] == "jin_pengumpul":
            total_pengumpul += 1

    if total_pengumpul > 0:
        print(f"Mengerahkan {total_pengumpul} jin untuk mengumpulkan bahan.")
        total_bahan = [0, 0, 0]
        for i in range(total_pengumpul):
            bahan = []
            for j in range(3):
                time.sleep(5/1000)
                bahan = bahan + [data.randrange(0, 5)]

            total_bahan[0] += bahan[0]
            total_bahan[1] += bahan[1]
            total_bahan[2] += bahan[2]
            bahan_bangunan = kumpul(
                bahan[0], bahan[1], bahan[2], bahan_bangunan)

        print(
            f"Jin menemukan total {total_bahan[0]} pasir, {total_bahan[1]} batu, dan {total_bahan[2]} air.")
    else:
        print(
            "Kumpul gagal. Anda tidak punya jin pengumpul. Silakan summon terlebih dahulu.")

    print(bahan_bangunan)
    return bahan_bangunan


def batchbangun(bahan_bangunan: list, candi: list, users: str) -> tuple:
    total_pembangun = 0
    list_user = []
    for user in users:
        if user[2] == "jin_pembangun":
            total_pembangun += 1
            list_user = list_user + [user[0]]
    if total_pembangun > 0:
        total_bahan = [0, 0, 0]
        list_bahan = []
        for i in range(total_pembangun):
            bahan = []
            for j in range(3):
                time.sleep(5/1000)
                bahan = bahan + [data.randrange(0, 5)]

            total_bahan[0] += bahan[0]
            total_bahan[1] += bahan[1]
            total_bahan[2] += bahan[2]
            list_bahan = list_bahan + [bahan]

        print(
            f"Mengerahkan {total_pembangun} jin untuk membangun candi dengan total bahan {total_bahan[0]} pasir, {total_bahan[1]} batu, dan {total_bahan[0]} air.")

        if bahan_bangunan[1][2] >= total_bahan[0] and bahan_bangunan[2][2] >= total_bahan[1] and bahan_bangunan[3][2] >= total_bahan[2]:
            bahan_bangunan[1][2] -= total_bahan[0]
            bahan_bangunan[2][2] -= total_bahan[1]
            bahan_bangunan[3][2] -= total_bahan[2]

            for k in range(total_pembangun):
                candi = bangun(
                    list_bahan[k][0], list_bahan[k][1], list_bahan[k][2], candi, list_user[k])

            print(f"Jin berhasil membangun total {total_pembangun} candi.")
        else:
            if total_bahan[0] > bahan_bangunan[1][2] and total_bahan[1] > bahan_bangunan[2][2] and total_bahan[2] > bahan_bangunan[3][2]:
                print(
                    f"Bangun gagal. Kurang {total_bahan[0] - bahan_bangunan[1][2]} pasir, {total_bahan[1] - bahan_bangunan[2][2]} batu, dan {total_bahan[2] > bahan_bangunan[3][2]} air.")
            elif total_bahan[0] > bahan_bangunan[1][2] and total_bahan[1] > bahan_bangunan[2][2]:
                print(
                    f"Bangun gagal. Kurang {total_bahan[0] - bahan_bangunan[1][2]} pasir dan {total_bahan[1] - bahan_bangunan[2][2]} batu.")
            elif total_bahan[0] > bahan_bangunan[1][2] and total_bahan[2] > bahan_bangunan[3][2]:
                print(
                    f"Bangun gagal. Kurang {total_bahan[0] - bahan_bangunan[1][2]} pasir dan {total_bahan[2] > bahan_bangunan[3][2]} air.")
            elif total_bahan[1] > bahan_bangunan[2][2] and total_bahan[2] > bahan_bangunan[3][2]:
                print(
                    f"Bangun gagal. Kurang {total_bahan[1] - bahan_bangunan[2][2]} batu dan {total_bahan[2] > bahan_bangunan[3][2]} air.")
            elif total_bahan[0] > bahan_bangunan[1][2]:
                print(
                    f"Bangun gagal. Kurang {total_bahan[0] - bahan_bangunan[1][2]} pasir.")
            elif total_bahan[1] > bahan_bangunan[2][2]:
                print(
                    f"Bangun gagal. Kurang {total_bahan[1] - bahan_bangunan[2][2]} batu.")
            elif total_bahan[2] > bahan_bangunan[3][2]:
                print(
                    f"Bangun gagal. Kurang {total_bahan[2] - bahan_bangunan[3][2]} air.")
    else:
        print(
            "Bangun gagal. Anda tidak punya jin pembangun. Silakan summon terlebih dahulu.")
    return (bahan_bangunan, candi)
# END


# F09 - Ambil Laporan Jin
# START
def laporan_jin(users: list, candi: list, bahan_bangunan: list):
    total_jin = 0
    total_jin_pengumpul = 0
    total_jin_pembangun = 0
    list_pembangun = ["" for i in range(data.length(users))]
    for i in range(data.length(users)):
        if users[i][2] == "jin_pengumpul":
            total_jin += 1
            total_jin_pengumpul += 1
        if users[i][2] == "jin_pembangun":
            total_jin += 1
            total_jin_pembangun += 1
            list_pembangun[i] = users[i][0]

    print()
    print(f"> Total Jin: {total_jin}")
    print(f"> Total Jin Pengumpul: {total_jin_pengumpul}")
    print(f"> Total Jin Pembangun: {total_jin_pembangun}")

    data_jin_pembangun = [["", 0] for i in range(total_jin_pembangun)]
    for i in range(data.length(users)):
        if list_pembangun == "":
            continue
        user_jin = list_pembangun[i]
        total_kerajinan = 0
        for j in range(data.length(candi)):
            if user_jin == candi[j][1]:
                total_kerajinan += 1

        for j in range(data.length(data_jin_pembangun)):
            if data_jin_pembangun[j] == ["", 0]:
                data_jin_pembangun[j][0] = user_jin
                data_jin_pembangun[j][1] = total_kerajinan
                break

    jin_rajin = data_jin_pembangun[0][0]
    jin_malas = data_jin_pembangun[0][0]
    max_jin_rajin = data_jin_pembangun[0][1]
    min_jin_malas = data_jin_pembangun[0][1]
    for i in range(total_jin_pembangun):
        if data_jin_pembangun[i][1] > max_jin_rajin:
            max_jin_rajin = data_jin_pembangun[i][1]
            jin_rajin = data_jin_pembangun[i][0]
        if data_jin_pembangun[i][1] < min_jin_malas:
            min_jin_malas = data_jin_pembangun[i][1]
            jin_malas = data_jin_pembangun[i][0]

    if total_jin_pembangun == 0:
        jin_rajin = "-"
        jin_malas = "-"

    print(f"> Jin Terajin: {jin_rajin}")
    print(f"> Jin Termalas: {jin_malas}")
    print(f"> Jumlah Pasir: {bahan_bangunan[1][2]}")
    print(f"> Jumlah Air: {bahan_bangunan[2][2]}")
    print(f"> Jumlah Batu: {bahan_bangunan[3][2]}")
# END


# F10 - Ambil Laporan Candi
# START
def laporan_candi(candi: list):
    print(f"> Total Candi: {data.length(candi) - 1}")

    pasir = 0
    batu = 0
    air = 0
    list_harga_candi = [[0, 0] for i in range(data.length(candi))]
    for i in range(1, data.length(candi)):
        pasir += candi[i][2]
        batu += candi[i][3]
        air += candi[i][4]

        list_harga_candi[i][0] = candi[i][0]
        list_harga_candi[i][1] = candi[i][2]*10000 + \
            candi[i][3]*15000 + candi[i][4]*7500

    print(f"> Total Pasir yang digunakan: {pasir}")
    print(f"> Total Batu yang digunakan: {batu}")
    print(f"> Total Air yang digunakan: {air}")

    if data.length(candi) == 1:
        print("ID Candi Termahal: -")
        print("ID Candi Termurah: -")
    else:
        id_candi_mahal = list_harga_candi[1][0]
        candi_mahal = list_harga_candi[1][1]
        id_candi_murah = list_harga_candi[1][0]
        candi_murah = list_harga_candi[1][1]
        for i in range(1, data.length(candi)):
            if candi_mahal < list_harga_candi[i][1]:
                id_candi_mahal = list_harga_candi[i][0]
                candi_mahal = list_harga_candi[i][1]
            if candi_murah > list_harga_candi[i][1]:
                id_candi_murah = list_harga_candi[i][0]
                candi_murah = list_harga_candi[i][1]

        print(f"ID Candi Termahal: {id_candi_mahal}")
        print(f"ID Candi Termurah: {id_candi_murah}")
# END
