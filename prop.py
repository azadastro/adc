import re
import numpy as np

lines = open("2023/inputs/3.txt").read().splitlines()


def find_number(string):
    numbers = dict(
        (m.group(), (m.start(), m.end())) for m in re.finditer(r"\d+", string)
    )
    return numbers


def part_one():
    new_grid = []
    len_line = len(lines[0]) + 2
    new_grid.append("." * len_line)
    for line in lines:
        new_grid.append("." + line + ".")
    new_grid.append("." * len_line)

    symbols = set()
    engine_parts = []

    for i, (pre_line, line, nxt_line) in enumerate(
        zip(new_grid[0:-2], new_grid[1:-1], new_grid[2:]), 1
    ):
        numbers = find_number(line)
        for number, (s, e) in numbers.items():
            s = s - 1
            e = e + 1

            all_lines = "".join(
                [ch for ch in line[s:e].replace(".", "") if not ch.isdigit()]
            )
            all_lines += "".join(
                [ch for ch in pre_line[s:e].replace(".", "") if not ch.isdigit()]
            )
            all_lines += "".join(
                [ch for ch in nxt_line[s:e].replace(".", "") if not ch.isdigit()]
            )

            if len(all_lines) > 0:
                symbols.add(all_lines)
                engine_parts.append(int(number))

    print(sum(engine_parts))
    return engine_parts


def part_two():
    pass


if __name__ == "__main__":
    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
