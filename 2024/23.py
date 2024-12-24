lines = open("2024/inputs/23.txt").read().splitlines()


def get_connections():
    connections = {}
    for line in lines:
        pc1, pc2 = line.split("-")
        if pc1 not in connections:
            connections[pc1] = set()
        if pc2 not in connections:
            connections[pc2] = set()

        connections[pc1].add(pc2)
        connections[pc2].add(pc1)

    return connections


def part_one():

    connections = get_connections()

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

    connections = get_connections()

    networks = set()

    def find_network(pc, other_pcs):
        key = tuple(sorted(other_pcs))
        if key in networks:
            return
        networks.add(key)
        for neighbor in connections[pc]:
            if neighbor in other_pcs:
                continue
            if not all(neighbor in connections[query] for query in other_pcs):
                continue
            find_network(neighbor, {*other_pcs, neighbor})

    for connection in connections:
        find_network(connection, {connection})

    print(",".join(sorted(max(networks, key=len))))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
