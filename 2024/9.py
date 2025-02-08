input = open("2024/inputs/9.txt").read()


def get_blocks():
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

    return blocks


def get_last_num(input):

    for i, b in enumerate(input[::-1], 1):
        if b[1] != -1:
            return b

    return (0, -1)


def part_one():
    blocks = get_blocks()

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


def temp_part_2():
    files = {}
    blanks = []

    fid = 0
    pos = 0

    for i, char in enumerate(open("2024/inputs/9.txt").read()):
        x = int(char)
        if i % 2 == 0:
            if x == 0:
                raise ValueError("unexpected x=0 for file")
            files[fid] = (pos, x)
            fid += 1
        else:
            if x != 0:
                blanks.append((pos, x))
        pos += x

    while fid > 0:
        fid -= 1
        pos, size = files[fid]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[fid] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break

    total = 0

    for fid, (pos, size) in files.items():
        for x in range(pos, pos + size):
            total += fid * x

    print(total)


def part_two():
    blocks = get_blocks()
    new_blocks = []

    cur_id = blocks[0][1]
    count = 0
    for block in blocks:
        if cur_id == block[1]:
            count += 1
        else:
            new_blocks.append((cur_id, count))
            cur_id = block[1]
            count = 1
    new_blocks.append((cur_id, count))
    id = len(new_blocks) - 1
    while True:
        cur_file = new_blocks[id]

        if cur_file[0] == -1:
            id -= 1
            continue

        for i, block in enumerate(new_blocks):
            if block[0] == -1 and block[1] >= cur_file[1]:
                new_blocks.pop(id)
                new_blocks.pop(i)
                if block[1] - cur_file[1] != 0:
                    new_blocks.insert(i, (-1, block[1] - cur_file[1]))
                else:
                    id -= 1

                new_blocks.insert(i, cur_file)
                break
        else:
            id -= 1


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    temp_part_2()
