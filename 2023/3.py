import re

with open("2023/inputs/3.txt", "r") as f:
    lines = f.readlines()


def part_one():
    symbols = set()
    engine_parts = []
    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))
    for i, line in enumerate(lines[1:-1], 1):
        line = "." + line.replace("\n", ".")
        pre_line = "." + lines[i - 1].replace("\n", ".")
        nxt_line = "." + lines[i + 1].replace("\n", ".")

        numbers = re.findall(r"\d+", line)
        for number in numbers:
            index = line.index(number)
            start_ind = index - 1
            end_ind = index + len(number) + 1

            all_lines = "".join(
                [i for i in line[start_ind:end_ind].replace(".", "") if not i.isdigit()]
            )
            all_lines += "".join(
                [
                    i
                    for i in pre_line[start_ind:end_ind].replace(".", "")
                    if not i.isdigit()
                ]
            )
            all_lines += "".join(
                [
                    i
                    for i in nxt_line[start_ind:end_ind].replace(".", "")
                    if not i.isdigit()
                ]
            )

            if len(all_lines) > 0:
                symbols.add(all_lines)
                engine_parts.append(int(number))

    print(sum(engine_parts))
    return engine_parts


def other_sol():
    grid = open("3.txt").read().splitlines()
    cs = set()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for dr in range(r - 1, r + 2):
                for dc in range(c - 1, c + 2):
                    if (
                        dr < 0
                        or dr >= len(grid)
                        or dc < 0
                        or dc >= len(grid[dr])
                        or not grid[dr][dc].isdigit()
                    ):
                        continue
                    while dc > 0 and grid[dr][dc - 1].isdigit():
                        dc -= 1
                    cs.add((dr, dc))

    ns = []

    for r, c in cs:
        s = ""
        while c < len(grid[r]) and grid[r][c].isdigit():
            s += grid[r][c]
            c += 1
        ns.append(int(s))

    print(sum(ns))
    return ns


if __name__ == "__main__":

    a = part_one()

    b = other_sol()

    print("hello")
