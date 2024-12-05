def read_input():
    lines = open("2024/inputs/5.txt").read()

    rules, updates = lines.split("\n\n")

    return rules.split("\n"), updates.split("\n")


def get_rules_dict(rules):
    rules_dict = {}
    for rule in rules:
        n1, n2 = map(int, rule.split("|"))
        if n1 not in rules_dict.keys():
            rules_dict[n1] = [n2]
        else:
            rules_dict[n1].append(n2)

    return rules_dict


def part_one():

    rules, updates = read_input()
    rules_dict = get_rules_dict(rules)
    ok_updates = []
    not_ok_updates = []

    for update in updates:
        pages = list(map(int, update.split(",")))
        is_ok = True
        for i, page in enumerate(pages, 1):
            if not all(page not in rules_dict.get(p, []) for p in pages[i:]):
                is_ok = False
                not_ok_updates.append(pages)
                break

        if is_ok:
            ok_updates.append(pages)

    print(sum([update[int(len(update) / 2)] for update in ok_updates]))

    return not_ok_updates


def part_two():
    rules, updates = read_input()
    not_ok_updates = part_one()

    for update in not_ok_updates:
        print(update)

    print(sum([update[int(len(update) / 2)] for update in not_ok_updates]))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
