valid_move ={
                "N": ["|", "7", "F"] ,
                "S": ["|", "L", "J"] ,
                "W": ["-", "L", "F"] ,
                "E": ["-", "J", "7"]
            }

moves = {
    "|": {"S":["S", (+1, 0)], "N": ["N", (-1, 0)]},
    "-": {"E": ["E", (0, +1)], "W": ["W", (0, -1)]},
    "L": {"W": ["N", (-1, 0)], "S": ["E", (0,+1)]},
    "J": {"E": ["N", (-1, 0)], "S": ["W", (0,-1)]},
    "7": {"N": ["W", (0, -1)], "E": ["S", (+1,0)]},
    "F": {"N": ["E", (0, +1)], "W": ["S", (+1,0)]}
}
with open("10.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

def get_window(p, max_r, max_c):
    next_p = []
     
    next_p.append(("N", (max(p[0]-1, 0), p[1])))
    next_p.append(("S", (min(p[0]+1, max_r), p[1])))
    next_p.append(("W", (p[0], max(p[1]-1, 0))))
    next_p.append(("E", (p[0], min(p[1]+1, max_c))))
    
    return(next_p)

def get_move(p, s, d):
    m = moves[s][d]
    new_p = (p[0] + m[1][0], p[1] + m[1][1])
    return new_p, m[0]


def part_one():

    for r, line in enumerate(lines):
        max_c = len(line)
        if "S" in line:
            start_point = (r, line.index("S"))
            break
    
    next_points = get_window(start_point, len(lines), max_c)
    
    for direction, point in next_points:
        current_point = point
        num_steps = 1
        while True:
            step = lines[current_point[0]][current_point[1]]
            print(step, valid_move[direction])
            if step in valid_move[direction]:
                current_point, direction = get_move(current_point, step, direction)
                num_steps += 1
            else:
                break
        
        print(num_steps/2)

if __name__ == "__main__":

    part_one()
