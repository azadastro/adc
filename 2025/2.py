ranges = [list(map(int, r.split("-"))) for r in open("2025/inputs/2.txt").read().split(",")]


def part_one(ranges):
    invalids = []
    for (s, e) in ranges:
        for i in range(s, e+1):
            s_i = str(i)
            h = len(s_i)
            if h % 2 == 0 and s_i[:h//2]==s_i[h//2:]:
                invalids.append(i)

    print(sum(invalids))

def part_two(ranges):

    invalids = set()
    for (s, e) in ranges:
        for i in range(s, e+1):
            s_i = str(i)
            h = len(s_i)
            for l in range(1, h//2+1):
                if h % l == 0 and s_i[:l]*(h // l) == s_i:
                    invalids.add(i)

    print(sum(list(invalids)))


if __name__ == "__main__":

    print("Part One:")
    part_one(ranges)

    print("Part Two:")
    part_two(ranges)
