import time


# Rekursif
def str_len(line: str) -> int:
    if line == "":
        return 0
    else:
        return str_len(line[1:]) + 1


# CSV Parser
def split_line(line: str) -> list:
    arr = []
    i = 0
    while i < str_len(line):
        if line[i] == ";" or line[i] == "\n":
            arr = arr + [line[:i]]
            line = line[i+1:]
            i = 0
        else:
            i += 1
    return arr


def load(path: str, arr: list) -> list:
    with open(path, "r") as file:
        for line in file:
            arr = arr + [split_line(line)]
    return arr


def check_username(username: str, users: list) -> bool:
    for user in users:
        if username == user[0]:
            return True
    return False


def check_password(password: str) -> bool:
    return 5 <= str_len(password) <= 25


def panggil_jin(users: list, jenis_jin: str) -> list:
    while True:
        username_jin = input("Masukkan username jin: ")
        if check_username(username_jin, users):
            print()
            print(f'Username "{username_jin}" sudah diambil!')
            print()
            continue
        else:
            while True:
                password_jin = input("Masukkan password jin: ")
                if check_password(password_jin):
                    print()
                    print("Mengumpulkan sesajen...")
                    print("Menyerahkan sesajen...")
                    print("Membacakan mantra...")
                    print()
                    print(
                        f"Jin {username_jin} berhasil dipanggil!")
                    users = users + [[username_jin, password_jin, jenis_jin]]
                    return users
                else:
                    print()
                    print("Password panjangnya harus 5-25 karakter!")
                    print()


def check_tipe(username: str, users: list) -> str:
    for user in users:
        if username == user[0]:
            return user[2]


def list_len(arr: list) -> int:
    total = 0
    for i in arr:
        total += 1
    return total


# B01 - Random Number Generator
# START
def rand(seed: int, a: int, c: int, m: int) -> int:
    return (a * seed + c) % m


def randrange(low: int, high: int) -> int:
    return low + rand(int(time.time_ns()), 22695477, 1, 2**32) % (high - low + 1)
# END
