
with open("inputs\prob1.txt", "r") as f:
    input = f.readlines()

def part_one():

    all_cal_num = []

    for line in input:
        cal_num = []
        for ch in line:
            if ch.isnumeric():
                cal_num.append(ch)
        all_cal_num.append(int(cal_num[0]+cal_num[-1]))

    print(sum(all_cal_num))
    
    return



if __name__ != "main":
    part_one()