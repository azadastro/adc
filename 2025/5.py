p1, p2 = open("2025/inputs/5.txt").read().split("\n\n")

ranges = []
for line in p1.splitlines():
    s, e = map(int, line.split("-"))
    ranges.append((s, e))

ingredients = [int(i) for i in p2.splitlines()]

def part_one(ranges , ingredients):

    fresh = []
    for ingredient in ingredients:
        for s, e in ranges:
            if ingredient >= s and ingredient <= e:
                fresh.append(ingredient)
                break

    print(len(fresh))


def part_two(ranges):

    ranges.sort()
    
    range = None
    count = 0

    for s, e in ranges:
        if range == None:
            range = (s, e)
        elif range[1] < s:
            count += range[1] - range[0] + 1
            range = (s, e)
        else:
            range = (range[0] , max(range[1], e))

    count += range[1] - range[0] + 1
    print(count)

if __name__ == "__main__":

    print("Part One:")
    part_one(ranges, ingredients)

    print("Part Two:")
    part_two(ranges)
