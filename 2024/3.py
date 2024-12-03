with open("2024/inputs/3.txt", "r") as f:
    lines = f.read()


def mul(x, y):
    return x * y


def part_one(lines):
    sections = lines.split("mul(")
    sum_all = 0
    for section in sections:
        oper = "mul("
        for ch in section:
            if ch.isdigit() or ch == ",":
                oper += ch
            elif ch == ")":
                oper += ch
                break
            else:
                break

        try:
            sum_all += eval(oper)
        except:
            continue

    print(sum_all)


def part_two():
    new_lines = ""
    for s in lines.split("do()"):
        new_lines += s.split("don't()")[0]

    part_one(new_lines)


if __name__ == "__main__":

    print("Part One:")
    part_one(lines)

    print("Part Two:")
    part_two()
