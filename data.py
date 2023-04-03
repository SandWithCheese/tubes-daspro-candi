def str_len(line: str) -> int:
    i = 0
    for j in line:
        i += 1
    return i


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
