from functools import cache

lines = open("2025/inputs/7.txt").read().splitlines()

grid = [list(line) for line in lines]
S = [(i, j) for i, line in enumerate(lines) for j , c in enumerate(line) if c == "S"][0]
    
def part_one():

    beams = [S]
    seen = set()
    count = 0
    def add_beam(beamset, i, j):
        if (i, j) in seen:
            return beamset
        seen.add((i, j))
        beamset.add((i, j))

        return beamset

    while len(beams) > 0:
        new_beams = set()
        for (i, j)  in beams:
            if grid[i][j] == "^":
                count += 1
                if j-1 >= 0 and grid[i][j-1] != "^":
                    new_beams = add_beam(new_beams, i, j-1)
                if j+1 < len(grid[0]) and grid[i][j+1] != "^":
                    new_beams = add_beam(new_beams, i, j+1)
            else:
                if i+1 < len(grid):
                    new_beams = add_beam(new_beams, i+1, j)
        
        beams = new_beams
        
    print(count)


def part_two():

    @cache
    def quantom_split_beam(i, j):
        if i >= len(grid): return 1

        if 0 <= j < len(grid[0]):
            if grid[i][j] == "^":
                return quantom_split_beam(i, j-1) + quantom_split_beam(i, j+1)
            else:
                return quantom_split_beam(i+1, j)
        else:
            return 0
        
    print(quantom_split_beam(*S))

if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
