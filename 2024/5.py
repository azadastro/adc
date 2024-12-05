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


def is_ok(pages, rules):
    for i, page in enumerate(pages, 1):
        if not all(page not in rules.get(p, []) for p in pages[i:]):
            return False

    return True


def part_one(print_result=True):

    rules, updates = read_input()
    rules_dict = get_rules_dict(rules)
    ok_updates = []
    not_ok_updates = []

    for update in updates:
        pages = list(map(int, update.split(",")))

        if is_ok(pages, rules_dict):
            ok_updates.append(pages)
        else:
            not_ok_updates.append(pages)

    if print_result:
        print(sum([update[int(len(update) / 2)] for update in ok_updates]))

    return not_ok_updates


def part_two():
    rules, updates = read_input()
    not_ok_updates = part_one(False)
    rules_dict = get_rules_dict(rules)

    sorted_updates = []

    for pages in not_ok_updates:
        new_update = []
        not_ok_page = []
        for i, page in enumerate(pages, 1):
            if all(page not in rules_dict.get(p, []) for p in pages[i:]):
                new_update.append(page)
            else:
                not_ok_page.append(page)

        for page in not_ok_page:
            for i in range(len(new_update) + 1):
                temp_pages = new_update[:i] + [page] + new_update[i:]
                if is_ok(temp_pages, rules_dict):
                    new_update = temp_pages
                    break
        sorted_updates.append(temp_pages)

    print(sum([update[int(len(update) / 2)] for update in sorted_updates]))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
