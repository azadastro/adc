lines = open("2015\inputs\\5.txt").read().splitlines()


VOWELS = list("aeiou")
FORBIDDEN = ["ab", "cd", "pq", "xy"]


def check_vowel(line):
    return sum([1 for ch in line if ch in VOWELS]) >= 3


def check_double(line):
    for ch1, ch2 in zip(line, line[1:]):
        if ch1 == ch2:
            return True
    return False


def check_forbidden(line):
    for f in FORBIDDEN:
        if f in line:
            return False
    return True


def new_check_double(line):
    for ch1, ch2 in zip(line, line[1:]):
        if line.count(ch1 + ch2) >= 2:
            return True
    return False


def chech_three(line):
    for ch1, ch2 in zip(line, line[2:]):
        if ch1 == ch2:
            return True
    return False


def part_one():
    nice_string = []
    for line in lines:
        if check_vowel(line) and check_double(line) and check_forbidden(line):
            nice_string.append(line)

    print(len(nice_string))


def part_two():
    nice_string = []
    for line in lines:
        if new_check_double(line) and chech_three(line):
            nice_string.append(line)

    print(len(nice_string))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
