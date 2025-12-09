import math

lines = open("2025/inputs/6.txt").read().splitlines()


def part_one(lines):

    in_list =[[] for _ in range(len(lines[1].split()))]
    for line in lines[:-1]:
        for i, l in enumerate(line.split()):
            in_list[i].append(int(l))

    op_out = []
    for i, o in enumerate(lines[-1].split()):
        if o == "+":
            op_out.append(sum(in_list[i]))
        elif o == "*":
            op_out.append(math.prod(in_list[i]))
        else:
            print("Unknown Operator")
    
    print(sum(op_out))

def part_two():

    pass


if __name__ == "__main__":

    print("Part One:")
    part_one(lines)

    print("Part Two:")
    part_two()
