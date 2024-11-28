with open("inputs\prob.txt", "r") as f:
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


def find_first_digit(in_str: str, reversed: bool = False, spelled_lookup: bool = False):
    emp_str = ""
    found_num = False
    for ch in in_str:
        if ch.isdigit():
            found_num = True
        
        if spelled_lookup:
            emp_str += ch
            for j, s_digit in enumerate(SPELLED_DIGITS, 1):
                if reversed:
                    s_digit = s_digit[::-1]
                if s_digit in emp_str:
                    ch = str(j)
                    found_num = True
        
        if found_num:
            return ch
    
    return


def part_one():

    all_cal_num = []

    for line in input:
        frst_num = find_first_digit(line)
        scnd_num = find_first_digit(line[::-1])
        all_cal_num.append(int(frst_num + scnd_num))

    print(sum(all_cal_num))


def part_two():
    all_cal_num = []

    for line in input:
        frst_num = find_first_digit(line, spelled_lookup = True)
        scnd_num = find_first_digit(line[::-1], spelled_lookup= True, reversed=True)
        all_cal_num.append(int(frst_num + scnd_num))

    print(sum(all_cal_num))


if __name__ == "__main__":
    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
