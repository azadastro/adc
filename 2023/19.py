
def get_input():
    lines = open("19.txt").read().splitlines()

    lines_dict = {
        "workflows": [],
        "ratings": []
    }
    k = "workflows"
    for line in lines:
        if line == "":
            k = "ratings"
            continue
        lines_dict[k].append(line)
    
    workflows = {}
    for w in lines_dict["workflows"]:
        k, r = w.split("{")
        workflows[k] = r[:-1].split(",")

    ratings = []
    for w in lines_dict["ratings"]:
        ratings.append(w[1:-1].split(","))

    return workflows, ratings

def valid_rating(rating, workflow, w_n):

    while True:
        flage = True
        for w in workflow[w_n][:-1]:
            p1, p2 = w.split(":")
            rule = f"{rating[p1[0]]}" + p1[1:]
            if eval(rule):
                w_n = p2
                flage = False
                break
        if flage:
            w_n = workflow[w_n][-1]

        if w_n == "A":
            return True
        if w_n == "R":
            return False



def part_one(workflows, ratings):

    total = 0
    for rating in ratings:
        rating_dict = {r.split("=")[0]: int(r.split("=")[1]) for r in rating}
        
        if valid_rating(rating_dict, workflows, "in"):
            total += sum(list(rating_dict.values()))
        

    print(total)

def part_two():
    pass

if __name__ == "__main__":

    w, r = get_input()
    part_one(w, r)
    part_two()