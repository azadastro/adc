
lines = open("11.txt").read().splitlines()

def clac_dist(p1, p2, w_mat):
    dist = 0
    for r in range(min(p1[0], p2[0]), max(p1[0], p2[0])):
        dist += w_mat[r+1][p1[1]]
    for c in range(min(p1[1], p2[1]), max(p1[1], p2[1])):
        dist += w_mat[p2[0]][c+1]
    return dist

def main(w):
    
    w_lines = []
    for i, line in enumerate(lines):
        if "#" in line:
            w_lines.append([1]*len(line))
        else:
            w_lines.append([w]*len(line))
    
    c=0
    for line in zip(*lines):
        if "#" not in line:
            for r in range(len(line)):
                w_lines[r][c] = w
        c += 1

    galaxies = []
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "#":
                galaxies.append((r, c))
    
    dist = []
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i+1:]:
            dist.append(clac_dist(g1, g2, w_lines))

    print(sum(dist))

if __name__ == "__main__":

    print("part one:")
    main(2)
    print("part two")
    main(1000000)