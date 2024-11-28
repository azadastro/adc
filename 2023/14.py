

lines = open("14.txt").read().splitlines()

def part_one():
    for r, line in enumerate(lines[1:], 1):
        if "O" not in line: continue
        for c, ch in enumerate(line):
            if ch == "O":
                temp_r = r
                while temp_r-1 >= 0:
                    if lines[temp_r-1][c] != ".":
                        break
                    else:
                        lines[temp_r-1] = lines[temp_r-1][:c] + "O" + lines[temp_r-1][c + 1:]
                        lines[temp_r] = lines[temp_r][:c] + "." + lines[temp_r][c + 1:]
                        temp_r -= 1

    total_w = 0
    for w, line in enumerate(lines[::-1], 1):
        total_w += line.count("O") * w

    print(total_w)


def part_two():
    pass

if __name__ == "__main__":

    part_one()
    part_two()