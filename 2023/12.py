

lines = open("12.txt").read().splitlines()

def part_one():
    for line in lines:
        springs, numbers = line.split()
        numbers =  tuple(map(int, numbers.split(",")))
        for num in numbers[::-1]:
            cur_group = springs[-num:]


def part_two():
    pass


if __name__ == "__main__":

    part_one()
    part_two()