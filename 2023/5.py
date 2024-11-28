
import re
from collections import defaultdict


def get_inputs():
    with open("5.txt", "r") as f:
        lines = f.readlines()

    lines_dict = defaultdict(list)
    for line in lines:
        line = line.replace("\n", "")
        if len(line) < 1 : continue
        if "seeds" in line:
            dict_key, seed_numbers = line.split(":")
            lines_dict[dict_key] = [int(n.group()) for n in list(re.finditer(r"\d+", seed_numbers))]
            continue

        if "map" in line:
            dict_key = line.replace(":", "")
            continue

        lines_dict[dict_key].append(line)

    return lines_dict


def get_map(str_maps, in_num):

    dst_num = in_num

    for m in str_maps:
        dst, src, rng = re.findall(r"\d+", m)

        dst, src, rng = int(dst), int(src), int(rng)
        if in_num >= src and in_num < src + rng:
            dst_num = dst + (in_num - src)
            return dst_num

    return dst_num


def part_one(inputs):

    map_keys = list(inputs.keys())
    map_keys.remove("seeds")
    locations = []
    for seed in inputs["seeds"]:
        loc_num = seed
        for k in map_keys:
            #print(k)
            loc_num = get_map(inputs[k], loc_num)
        
        locations.append(loc_num)

    print(min(locations))


def get_reverse_map(str_maps, dst_num):

    in_num = dst_num

    for m in str_maps:
        dst, src, rng = re.findall(r"\d+", m)
        dst, src, rng = int(dst), int(src), int(rng)

        if dst_num >= dst and dst_num < dst + rng:
            in_num = src + (dst_num - dst)
            return in_num

    return in_num


def part_two(inputs):

    map_keys = list(inputs.keys())
    map_keys.remove("seeds")
    map_keys.reverse()

    r_location = []
    for m in inputs[map_keys[0]]:
        dst, src, rng = re.findall(r"\d+", m)
        dst, src, rng = int(dst), int(src), int(rng)
        r_location.append(dst+rng)

    locations = range(0, max(r_location))

    for loc in locations:
        #print(loc, end="\r")
        seed_num = loc
        for k in map_keys:
            #print(k)
            seed_num = get_reverse_map(inputs[k], seed_num)
        
        for i in range(0, len(inputs["seeds"]), 2):
            s_seed = inputs["seeds"][i]
            e_seed = inputs["seeds"][i] + inputs["seeds"][i+1]

            if seed_num in range(s_seed, e_seed):
                print()
                print(loc)
                return



if __name__ == "__main__":
    
    lines_dict = get_inputs()
    part_one(lines_dict)
    part_two(lines_dict)