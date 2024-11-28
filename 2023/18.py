from shapely.geometry import Polygon


lines = open("18.txt").read().splitlines()


moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}


def part_one():

    points = [(0,0)]
    l_p = 0
    for line in lines:
        d, s, c = line.split()
        v_m, h_m = moves[d]
        s = int(s)
        cur_p = points[-1]
        l_p += s
        points.append((cur_p[0]+v_m*s, cur_p[1]+h_m*s))

    assert points[0] == points[-1]
    points.pop()
    pgon = Polygon(points) 

    area = pgon.area

    temp = area - l_p//2 +1

    print(temp + l_p)

def part_two():
    points = [(0,0)]
    l_p = 0
    for line in lines:
        _, _, c = line.split()
        c = c[2:-1]
        d = "RDLU"[int(c[-1])]
        s = int(c[:-1], 16)
        l_p += s
        v_m, h_m = moves[d]
        cur_p = points[-1]
        points.append((cur_p[0]+v_m*s, cur_p[1]+h_m*s))

    assert points[0] == points[-1]
    points.pop()
    pgon = Polygon(points) 

    area = pgon.area

    temp = area - l_p//2 +1

    print(temp + l_p)


if __name__ == "__main__":

    part_one()
    part_two()