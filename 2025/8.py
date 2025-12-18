import math

lines = open("2025/inputs/8.txt").read().splitlines()

jboxes = [list(map(int, line.split(","))) for line in lines]

distances = {}
for i in range(len(jboxes)):
    for j in range(i+1, len(jboxes)):
        distances[(i, j)] = math.dist(jboxes[i], jboxes[j])

distances = list(sorted(distances.items(), key=lambda item: item[1]))

def merge_circuts(circuits):
    while True:
        new_circuits = []
        seen = []
        for i in range(len(circuits)):
            c_1 = circuits[i]
            if c_1 in seen:continue
            for j in range(i+1, len(circuits)):
                c_2 = circuits[j]
                if any(c in c_1 for c in c_2):
                    c_1 = c_1.union(c_2)
                    seen.append(c_2)
            new_circuits.append(c_1)
        if len(new_circuits) == len(circuits): break
        circuits = new_circuits

    new_circuits.sort(key=lambda x: -len(x))
    return new_circuits


def part_one():

    n = 1000
    
    circuits = []
    for i in range(n):
        cur_link = distances[i][0]
        for circut in circuits:
            if any(j in circut for j in cur_link):
                circut.add(cur_link[0])
                circut.add(cur_link[1])
                break
        else:
            circuits.append(set(cur_link))
    
    circuits = merge_circuts(circuits)

    print(len(circuits[0])*len(circuits[1])*len(circuits[2]))

def part_two():
    
    circuits = []
    for i in range(len(distances)):
        cur_link = distances[i][0]
        for circut in circuits:
            if any(j in circut for j in cur_link):
                circut.add(cur_link[0])
                circut.add(cur_link[1])
                break
        else:
            circuits.append(set(cur_link))
        circuits = merge_circuts(circuits)
        if len(circuits[0]) == len(jboxes):
            print(jboxes[cur_link[0]][0]*jboxes[cur_link[1]][0])
            break



if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
