import re


with open("4.txt", "r") as f:
    lines = f.readlines()

def part_one():
    point_system = [0] + [2**i for i in range(100)]

    card_points = []
    for line in lines:
        first_part, elf_part = line.split("|")
        _, winning_part = first_part.split(":")
        winning_numbers = [int(n.group()) for n in list(re.finditer(r"\d+", winning_part))]
        elf_numbers = [int(n.group()) for n in list(re.finditer(r"\d+", elf_part))]
        card_value = 0
        for i, num in enumerate(elf_numbers):
            if num in winning_numbers:
                card_value += 1

        card_points.append(point_system[card_value])

    print(sum(card_points))

def part_two():
    num_copies = {key: 1 for key in range(len(lines))}
    for index, line in enumerate(lines):
        first_part, elf_part = line.split("|")
        _, winning_part = first_part.split(":")

        winning_numbers = [int(n.group()) for n in list(re.finditer(r"\d+", winning_part))]
        elf_numbers = [int(n.group()) for n in list(re.finditer(r"\d+", elf_part))]
        num_matches = 0
        for num in elf_numbers:
            if num in winning_numbers:
                num_matches += 1

        for i in range(index+1, index+num_matches+1):
            num_copies[i] += 1 * num_copies[index]

    print(sum(num_copies.values()))

if __name__ == '__main__':

    part_one()
    part_two()