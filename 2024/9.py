input = open("2024/inputs/9.txt").read()


def get_last_num(input):

    for i, b in enumerate(input[::-1], 1):
        if b[1] != -1:
            return b

    return (0, -1)


def part_one():
    blocks = []
    id = 0
    global_i = 0
    for i, ch in enumerate(input):

        if i % 2 == 0:
            blocks.extend([(global_i + m, id) for m in range(int(ch))])
            global_i += int(ch)
            id += 1
        elif i % 2 != 0:
            blocks.extend([(global_i + m, -1) for m in range(int(ch))])
            global_i += int(ch)

    checksum = 0
    i = 0
    while i < len(blocks):
        block = blocks[i]
        if block[1] == -1:
            last_block = get_last_num(blocks[i:])
            if last_block[1] == -1:
                break
            checksum += block[0] * last_block[1]
            blocks[i] = (block[0], last_block[1])
            blocks = blocks[: last_block[0]]
        else:
            checksum += block[0] * block[1]

        i += 1

    print(checksum)


def part_two():

    pass


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
