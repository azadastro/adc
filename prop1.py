with open("inputs\prob1.txt", "r") as f:
    input = f.readlines()


SPELLED_DIGITS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def find_first_digit(in_str: str, flag: bool):
    emp_str = ""
    for ch in in_str:
        emp_str += ch
        if ch.isdigit():
            min_index = 1000
            for i, s_digit in enumerate(SPELLED_DIGITS):
                if flag:
                    s_digit = s_digit[::-1]
                if s_digit in emp_str:
                    if emp_str.find(s_digit) < min_index:
                        min_index = emp_str.find(s_digit)
                        ch = str(i + 1)
            return ch


def part_one():

    all_cal_num = []

    for line in input:
        cal_num = []
        for ch in line:
            if ch.isnumeric():
                cal_num.append(ch)
        all_cal_num.append(int(cal_num[0] + cal_num[-1]))

    print(sum(all_cal_num))


def part_two():
    return


if __name__ == "__main__":
    print("Part One:")
    part_one()
