buyers = open("2024/inputs/22.txt").read().splitlines()


def calc_secret(secret_num, step):
    secret_nums = [secret_num]
    for i in range(step):
        secret_num = ((secret_num * 64) ^ secret_num) % 16777216
        secret_num = ((secret_num // 32) ^ secret_num) % 16777216
        secret_num = ((secret_num * 2048) ^ secret_num) % 16777216
        secret_nums.append(secret_num)

    return secret_nums


def part_one():

    total = 0
    all_secret_nums = []
    for buyer in buyers:
        secret_number = calc_secret(int(buyer), 2000)
        all_secret_nums.append(secret_number)
        total += secret_number[-1]

    print(total)
    return all_secret_nums


def part_two(all_secret_nums):
    seq_2_prices = {}
    for secret_nums in all_secret_nums:
        all_prices = [s % 10 for s in secret_nums]
        seen = set()
        for i in range(len(all_prices) - 4):
            p1, p2, p3, p4, p5 = all_prices[i : i + 5]
            seq = (p2 - p1, p3 - p2, p4 - p3, p5 - p4)
            if seq in seen:
                continue
            seen.add(seq)
            if seq not in seq_2_prices:
                seq_2_prices[seq] = 0
            seq_2_prices[seq] += p5

    print(max(seq_2_prices.values()))


if __name__ == "__main__":

    print("Part One:")
    all_secret_nums = part_one()

    print("Part Two:")
    part_two(all_secret_nums)
