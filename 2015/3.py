line = open("2015\inputs\\3.txt").read()

direction = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}


def part_one():

    houses = set()
    cur_house = (0, 0)
    houses.add(cur_house)
    for ch in line:
        cur_house = (cur_house[0] + direction[ch][0], cur_house[1] + direction[ch][1])
        houses.add(cur_house)

    print(len(houses))


def part_two():

    santa_houses = set()
    robot_houses = set()
    s_cur_house = (0, 0)
    r_cur_house = (0, 0)

    santa_houses.add(s_cur_house)
    robot_houses.add(r_cur_house)

    for s_ch, r_ch in zip(line[::2], line[1::2]):

        s_cur_house = (
            s_cur_house[0] + direction[s_ch][0],
            s_cur_house[1] + direction[s_ch][1],
        )
        r_cur_house = (
            r_cur_house[0] + direction[r_ch][0],
            r_cur_house[1] + direction[r_ch][1],
        )
        santa_houses.add(s_cur_house)
        robot_houses.add(r_cur_house)

    print(len(santa_houses.union(robot_houses)))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
