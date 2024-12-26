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
    all_prices = []
    for secret_nums in all_secret_nums:
        all_prices.append([s for s in secret_nums])


if __name__ == "__main__":

    print("Part One:")
    all_secret_nums = part_one()

    print("Part Two:")
    part_two(all_secret_nums)
