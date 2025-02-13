import hashlib

input = "bgvyzdsv"


def part_one():

    i = 1
    while True:
        key2hash = input + str(i)
        hash = hashlib.md5(key2hash.encode()).hexdigest()

        if hash.startswith("00000"):
            print(i)
            break

        i += 1


def part_two():

    i = 1
    while True:
        key2hash = input + str(i)
        hash = hashlib.md5(key2hash.encode()).hexdigest()

        if hash.startswith("000000"):
            print(i)
            break

        i += 1


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
