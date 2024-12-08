lines = open("2024/inputs/7.txt").read().splitlines()


def part_one(print_result=True):

    not_possible = []
    total_calibration = 0
    for equation in lines:
        test_value, c = equation.split(":")
        test_value = int(test_value)
        configs = list(map(int, c.split()))

        cur_conf = [configs[0]]
        for i in range(1, len(configs)):
            temp_c = []
            for conf in cur_conf:
                temp_c.append(conf + configs[i])
                temp_c.append(conf * configs[i])

            cur_conf = temp_c

        if test_value in temp_c:
            total_calibration += test_value
        else:
            not_possible.append((test_value, configs))

    if print_result:
        print(total_calibration)

    return total_calibration, not_possible


def part_two():

    total_calibration, not_possible = part_one(False)

    for test_value, configs in not_possible:
        cur_conf = [configs[0]]
        for i in range(1, len(configs)):
            temp_c = []
            for conf in cur_conf:
                temp_c.append(conf + configs[i])
                temp_c.append(conf * configs[i])
                temp_c.append(int(str(conf) + str(configs[i])))

            cur_conf = temp_c

        if test_value in temp_c:
            total_calibration += test_value

    print(total_calibration)


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
