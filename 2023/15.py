from collections import defaultdict


with open("15.txt", "r") as f:
    line = f.readline()

def get_hash(seq):
    current_value = 0
    for char in seq:
        current_value +=  ord (char)
        current_value *= 17
        current_value %= 256
    return current_value

def part_one():
    input_seq = line.split(",")

    all_values = []
    for seq in input_seq:
        all_values.append(get_hash(seq))

    print(sum(all_values))

def part_two():
    input_seq = line.split(",")
    boxes = defaultdict(list)
    len_focal_dict = {}
    for seq in input_seq:
        if "=" in seq:
            len_label, len_focal = seq.split("=") 
            index = get_hash(len_label)
            if len_label not in boxes[index]:
                boxes[index].append(len_label)
            
            len_focal_dict[len_label] = int(len_focal)

        else:
            len_label = seq[:-1]
            index = get_hash(len_label)
            if len_label in boxes[index]:
                boxes[index].remove(len_label)
            
    all_focal = 0
    for box_num, box in boxes.items():
        for len_num, len_label in enumerate(box, 1):
            all_focal += (box_num+1) * len_num * len_focal_dict[len_label]
    
    print(all_focal)


if __name__ == "__main__":

    part_one()
    part_two()