def read_input():
    part1, part2 = open("2024/inputs/24.txt").read().split("\n\n")

    wires = {}
    for line in part1.splitlines():
        k, v = line.split(": ")
        wires[k] = v

    gates = []
    for line in part2.splitlines():
        g = line.split()
        gates.append({"ins": (g[0], g[2]), "op": g[1], "out": g[4]})

    return wires, gates


ops = {"AND": lambda i, j: i & j, "OR": lambda i, j: i | j, "XOR": lambda i, j: i ^ j}


def part_one():

    wires, gates = read_input()

    while len(gates) > 0:
        gate = gates[0]

        if all(g in wires for g in gate["ins"]):
            g_out = ops[gate["op"]](
                int(wires[gate["ins"][0]]), int(wires[gate["ins"][1]])
            )
            wires[gate["out"]] = str(g_out)
            gates.pop(0)
        else:
            gates.pop(0)
            gates.append(gate)

    bin_num = [
        v if k.startswith("z") else "" for k, v in dict(sorted(wires.items())).items()
    ]
    bin_str = "".join(bin_num[::-1])

    print(int(bin_str, 2))


def part_two():

    pass


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
