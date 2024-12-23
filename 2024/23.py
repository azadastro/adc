lines = open("2024/inputs/23.txt").read().splitlines()


def part_one():

    connections = {}
    for line in lines:
        pc1, pc2 = line.split("-")
        if pc1 not in connections:
            connections[pc1] = set()
        if pc2 not in connections:
            connections[pc2] = set()

        connections[pc1].add(pc2)
        connections[pc2].add(pc1)

    networks = set()
    for pc1, connection in connections.items():
        for main_pc in connection:
            for sec_pc in connection - {main_pc}:
                if sec_pc in connections[main_pc]:
                    networks.add(tuple(sorted([pc1, main_pc, sec_pc])))

    total_t_network = 0
    for network in networks:
        if any(pc.startswith("t") for pc in network):
            total_t_network += 1

    print(total_t_network)


def part_two():

    connections = {}
    for line in lines:
        pc1, pc2 = line.split("-")
        if pc1 not in connections:
            connections[pc1] = {pc1}
        if pc2 not in connections:
            connections[pc2] = {pc2}

        connections[pc1].add(pc2)
        connections[pc2].add(pc1)

    networks = []
    for pc1, connection in connections.items():
        cur_connection = connection
        for pc in connection:
            cur_connection = cur_connection.intersection(connections[pc])

        networks.append(cur_connection)

    total_t_network = 0

    print(total_t_network)


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
