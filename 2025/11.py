from functools import cache

lines = open("2025/inputs/11.txt").read().splitlines()

devices_dict = {l.split(": ")[0]: l.split(": ")[1].split() for l in lines}



def part_one(devices_dict):

    @cache
    def find_path(s):
        if s == "out": 
            return 1
        return sum(find_path(d) for d in devices_dict[s])

    S = "you"
    print(find_path(S))


def part_two(devices_dict):

    @cache
    def find_path(s, e):
        if s == e: 
            return 1
        return sum(find_path(d, e) for d in devices_dict.get(s, []))
    
    S = "svr"
    E = "out"

    sdfe = find_path(S, "dac") * find_path("dac", "fft") * find_path("fft", E)
    sfde = find_path(S, "fft") * find_path("fft", "dac") * find_path("dac", E)
    print(sdfe + sfde)

if __name__ == "__main__":

    print("Part One:")
    part_one(devices_dict)

    print("Part Two:")
    part_two(devices_dict)
