*presents, regions = open("2025/inputs/12.txt").read().split("\n\n")



def part_one(presents, regions):
    # this works for the actual input not the example
    total = 0
    for region in regions.splitlines():
        r, counts = region.split(": ")
        r = list(map(int, r.split("x")))
        counts= list(map(int, counts.split()))

        if r[0] // 3 * r[1] // 3 >= sum(counts):
            total += 1
    
    print(total)

def part_two():

    print("DONE!")


if __name__ == "__main__":

    print("Part One:")
    part_one(presents, regions)

    print("Part Two:")
    part_two()
