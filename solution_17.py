ROCKS = '''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''


def collides(tower, rock, Y, X):
    for y in range(len(rock)):
        abs_y = Y + y
        for x in range(len(rock[0])):
            abs_x = X + x
            if abs_x < 0 or abs_x >= 7 or abs_y < 0:
                return True
            if Y + y < len(tower):
                if tower[abs_y][abs_x] == '#' and rock[y][x] == '#':
                    return True
    return False


def drop(rocks, jets, rock_count):
    tower = []
    jet_index = 0
    max_y = -1
    memo = {}
    rock_index = 0
    extra = 0
    while rock_index < rock_count:

        rock = rocks[rock_index % len(rocks)]
        for y in range((max_y + 5) - len(tower)):
            tower.append(['.' for x in range(7)])

        X = 2
        Y = len(tower) - 1

        # part 2 solved with great help from https://github.com/TimHuisman1703/AdventOfCode/blob/master/2022/Day%2017/aoc17_2.py
        key = (rock_index % len(rocks), jet_index % len(jets))
        if key in memo:
            prev_rock, prev_y = memo[key]
            drock = rock_index - prev_rock
            dy = Y - prev_y
            div = (rock_count - rock_index) // drock
            rock_index += drock * div
            extra = (dy * div)
            memo = {}
        elif rock_index > 1000:
            memo[key] = (rock_index, Y)

        while True:
            jet = jets[jet_index % len(jets)]
            jet_index += 1

            dx = -1 if jet == "<" else 1
            if not collides(tower, rock, Y, X + dx):
                # we can slide left/right
                X += dx
            if not collides(tower, rock, Y - 1, X):
                # we can fall
                Y -= 1
            else:
                for y in range(len(rock)):
                    max_y = max(max_y, Y + y)
                    for x in range(len(rock[y])):
                        if tower[Y + y][X + x] != "#":
                            tower[Y + y][X + x] = rock[y][x]
                break
        rock_index += 1
    return max_y + extra + 1


def solve(puzzle_input):
    rocks = [list(reversed([y for y in x.split("\n")]))
             for x in ROCKS.strip().split("\n\n")]
    jets = [x for x in puzzle_input.strip()]

    print(drop(rocks, jets, 2022))
    print(drop(rocks, jets, 1000000000000))
    return


solve('''
>>><<<>>>><<<>>>><<<<>>><<<>><<<<><<<<>><<<<><<<><>>>><<<>>><<<<>>><>>>><<<>>>><>>><>>><<<<>>>><<>>><>>><>>>><<<<>>>><<<>>><>><<<>>><<<>>>><<<>>><>>>><<>>>><<<<>>><<>>>><<<>>>><>>><<<>><<>>>><<>>>><><<<>><<<>>>><><>>>><<><<<<>>>><<<>>>><<<><>>><<<>>>><<<>>><<<>><<<<>><<<<><<<>><<><>>><<<<>>>><<<<>><<>>>><<<<>><<<<>><<<<><<<>><<<>><<<>><<>><<>>><<<<>>><<<<>><<<><<<>><>>>><<<<>>><><<<<>><<<<><<><<<>>>><<<<>><>><<<<>>><<<>>>><<<>>><<<><<><<<>>>><<<<><><<<>>><<<<>>>><<<<>>><<<>>>><<<<><<<>>><<>><<<><>>>><<<<>>>><<<>><<<>>><<<><<<><<<<>>>><<>>>><<<>>>><><>>>><<>>>><<<>><>>>><<<<>>><<<><>>><<<><<<<>>><<<><<<>>><>>><<<>>>><>>><<<>><><>><<<<>><>>><>>>><<>><<<>><<>>><<>>>><<<<>>>><<<<>>>><<<>>><<>>>><<><<>>><<>>><<<<>>><<>><>>>><><><<<<>>>><<<<>><<<<><<<<>>>><<<>>><<><<<>>>><<><><<>>><<>><<<>>><>><<<>><<<<>>><><<>><<<>>><<<<>><>>><<>><>>><<<><>><<>>>><>>><<>>><<<<>><<<<>>>><>>><<<><<<<>>><<>>><>>><<<<>>>><<<<>><<<>>>><<>>><>>><>>><<<>><<<<>>><<<<>>>><>>><>>>><<<<><<><<<<>>>><>><>>>><<<><<<>>><>>><<<<><>>><<<>><<<>>><<<>>>><>>><>>>><<>><<>>><<<<>>>><><<<<>><<<>><<>>><>><><<>><<>>>><<<<>>>><<<>>><<>><>>><<<<><<<<>><<>>>><<<<>>>><<<>><><<<<>>>><><<<><<<<>>>><>>>><<<>>><<<<>>>><<<>>>><<>>>><<><<>><<<<>><<>>>><<<><<>><<<<>>><<<>>><<>>><<<>>>><<>>>><<>>><<<<>>><<<>>>><<>>>><<<<>>><<<>><<<>><<><<<<>><>><>><<<><<>>>><<<<><>>>><<<<><<>>><<>>>><<>>><>>><><<><<<<>>>><<>>>><<<>><<>>>><<<>>><<<>>><<<><<<<>><<<>><<<<><<>>><<<>>><<<>><<<>>>><<><>><<<><<<<>><<>><<<>><<<<>><<<>>>><>><<>>>><<<><<>>>><<<>>>><>>><<<>>>><<<<>>><<<><<>>><<<>>><<>><<>>>><<<<>>><<<><<<><>><>>><<<<><<<<><<<<>><<<<>>><<<<><<><<>>><<<<>><<<>><><>>>><>><<<<>><<>>>><><>>><><<>>><>><<<<>><>>><>><<<<><<<>>><>><<<>>>><><>>><<<>>>><<><><<<<>>><<>><<<>><<><<<<>>>><<>><>>><<>>><<>>>><<<>>><<>>>><<<<>>>><<<<>><<<<>>>><<<<>>><<<><<<>>><>>>><>>>><<<><<<<>>><><<<<>>>><>><<>>>><<<<>>><<>>><><<<<>>><<<<>>>><<<<>>>><<><>>>><<><<>>><<><<<<>>>><<<<>><<<><>>>><>>>><<>>><<<<><><<>>><<>>><><><><>>><<><<>>><>>><<<<>>>><><<<>>>><>>><<<>>><<<>>>><<<>>>><<>>><>>>><<>><<<>>><<<>><<<<><<>>>><<<<>>><<<<>>><>>><<<<>><<<<>><<<<>><<<><<<>>>><<<>>>><>>><<>><<<<><<<>>>><<<>>><<<<>>>><>><<<><<>>>><<>>><<<<>>><>>><<<>><<<<>>>><<<>><<<>>>><>>>><<<><<<<>>>><>>>><<<<>>>><<<<><<>>>><<>>><>>>><<<<>>><>>><>><<<>>><>>>><<<<>><<>>><<<>>>><<>>><<><<<<><<<>><<><<>><<<><<><<<<>><<<<><<><<>>><<<>><<>>>><<>>><<>>>><<<<>>><<<>>><<>>>><<>>>><<<<>>><><>>>><<>>>><<>><<>>><<<>><<<>><>>><<<>><<<>><<<>>><<<<><<<<>>><<<<>>>><<<>>><<>><<>>><<<><<><<>><<<<>><<><<<<>><<<<>>>><>>>><><<<>>>><<<<>>><>><<<>>>><<>>>><>>><<<>><>>>><>><>>>><<<<>>><<><><<<>>><<<<>>>><<<><>><>><<<>>>><>>>><>>>><><<<<>><<<<><><<<>>>><<>>><<<<>>><<<>>>><>>><<><<>>>><<>><<>><<<<>>>><<>>>><><<<<><<><<<<>><<>><<<<><<<><<<<>>>><<<>><<<<>><<<<>>>><<>>><<<>><>>><>>><<>><>>>><><<>><<<><<>>>><<>>><<>>><<>>><<<<>>>><<>>><>><>>><<<><<<>><<>>>><<<<>>>><<<<>>>><<>>><<<>>>><<<<>><<<<>>>><>>>><>>><>>>><<<<>><><<><<<<>>><<<>>><<>>>><>><><<<>>>><<<<>>>><<>><<>><<<><<<<><<<<>><<<<>>>><>>>><>>>><<>>><<<>>><<<>>>><<>><<<>><<<><>>><<>>>><<<><>>>><><<<<><<>><><>><>><<<>><<>>>><<>>><<<><<>>>><<<<>>>><>>>><<<<>>><<<<>>><<><<<<>><>>>><<>>>><>>>><<<>>><>><<<>><<><<<<>><<<>>>><<<<>><<<<>>><<<>>><<<>>>><<<<>>><<<>><<<<>>><<<>>>><>>>><<><>><<>>>><<<<>>><><<<<>>><><>>>><>><<<<>>><<<<>>>><<><<<>>><>>>><<<>><<>>>><<<<>><><<>>><<>>>><>><<<><<>>><<<>>><<<<>><><<><><<<<>><<<<>><<>>><<<>>>><<<<>><<<>><<<>>><<><<<<>>><<<>>><>><>>><>><>><<<<>>>><>><<<<>><<>>>><>>>><>>>><<<<>>><<<<><<>>><>>><<<<>>>><<<>>>><<>>>><<<><<<><<<<><>>>><<<>><<<>>>><<<<>><<>>><<<>>>><<<><<<>>><<><><<>>><<<>><<<<><<<<>>><<><<<>><><>>>><<>><<<<><<<<>><<<><<><<<<>>>><<>>>><<<<>><<<>>><<><>>>><<>><>><<<<>><<<>>>><>><<<<>>><><<<><<>>><>>>><<<<>>><<<><>>><>>>><<<<>>><<>><<>>><<<<><<<<>><<><<><<>><>>><<<>>>><>>><>>>><<<<><<>><>>><<<>>><>>>><<<<>>>><<>>><>>><<<<>>>><<>>>><<<>>><<<>>>><<<>><>>><<>>><<<><<<<>>>><<<>>><<>><<<<>><>>>><<>>><<<<>><<<>>>><<>>>><<>><><<<<>>><<<<>><<<>><<<<>>>><<>>><<><<>>><<>><>><>>>><<<<><<>>><<<<><<<<>><<><<>>><<<>>><<<<>><<<<>>><>><<<<>>><<<>>>><>>><>><<<>>><<>>>><<<<>>>><<>>><<<<>><<><>>><<>>><<<<>>><<<<><<>><<<<><<<>>>><<>>>><>><<<><<<<>>>><<<<>><<<<><<>>>><<<>>>><>>><>><<<<><<<<>>>><<<>>><<<>>>><><>>><<<<><<<<>>>><<<>>><<>>>><<><>><<><<<<>>>><>>>><<<>><<<>><<<<>>><<<<>><<<>><>>><<<>>>><<<<>><<<<>>>><<>>><<<>>>><<<<>>>><<<>><>><<>><><<<<>><<><><<>><<>><<<<>>><<>>>><<<<>>>><<><<<<>>>><<<>><<<<>>>><<<>>><<><>>>><<<>>><>>>><<<<>>>><>><<><<<<>>><<>>><<<<>><<<>>>><<>>>><<<><<<>>>><<<<><<<>><<<<>>><<<>><<<><<<>><>>><<<<>>><<<>>><<<>><<<>>>><<<<>>><<<<>>>><<<<>><<<<><<<>>><><<<>><<<>><<<>><<<>>><<<><<<>>>><<<>><<<<>>>><><<<<>><<<<>>><<<<>><<><<<>>>><>>><><<<<>>><>>><<<<>>>><<<<>>><<<>>>><><<>><><<><<<<><<<<>>><>><>>>><<<<><<<<>><<<><>>>><<>>><<><<>>><<>>>><<<<>>>><<><>>>><<<<><<>><<><<>><<<<>>><<<<>><<<<>>>><>><<><<<>>>><<<>><<>>>><<<><<<<>>>><<<>>><<>><<<>>>><<>><<<<>>>><<<<>><<<>>>><>><<<<><<<>>>><<<><<<>><>>><<>>>><<<<>>><<<><<><>><<><>><<<><><<<><<<<>>><<>><<<><<>><<<><<<>><<<>>><>>>><<<>>>><<<<>>>><<<>><>><<>>><<<><>>><<<>><<<><<>><>>>><><>>>><<<>>><<<>>>><>>><<<<>>><>>>><<<>>>><<>>><<>>>><<>><><>>>><<<>>>><>>><>><<>>><<>>>><>><<>>><<><>>>><<<>><<>>><><<<>><<>>>><<<<>>>><>>><<<<>><>>><<>><<><<<>>><>><<<><<>><<>>><<><><<<<>>>><<<>>><>>>><>><<<>>><<<>>><<<<>>>><><<<<>>><<<<><<<>><<<<>>>><>>>><<>><<<<>>>><<>>><>><<><<<>>><<<>>>><<<<>>><<<>>><>>><<<>>><<<<>><<<><<>>>><><<><<>><>><<<<>>>><>><<>><<<<>>><<>>>><<<>><<<>>><<<>>><<<<>>><<<<>>>><<<<>><>>>><<<<>>>><>>>><>>><<<<><<<<>>><><<>>><<>>>><<<<>><<<<>>><<<>><<<>>>><<<<>>><<<>>>><<<><>>>><>>><<>>>><<<><<<><>>>><<<>>>><<>>>><>>>><<><<<<>><<<<><>>>><<><<<<>>>><>>><<<<>>><<>>>><<<><<<<><><<>>><<<>>><<>><<<>>>><>>>><<<<>>>><<<>>><<<>><<><<<>>>><<<<>><<<>>><>>><>><<<>>>><<<<>>>><<><<<>>>><>>>><<<>>>><<>><<<<>>><<<>>><><><<<<>>>><<<>>>><><<>><<>>>><<<<>>>><<<><<>>>><>>><<<<>><<>><<<>><><<<<>>><><<<>>>><<<><<<>>><<<<>><<<<>>>><<<>>>><<>><<<>>><<<<>>><><<>><<<<>>>><<<<>>><<>>><<<<><>><>>><<<<><>>>><<>><>><<<>>>><<<>>><<>><<><>>>><<<>>>><<<<>>>><<>>>><<<<>>>><<<>>>><<<>><<<>>><>>><>>><>>>><<>>>><<<>>><<<<>>><<>><<<><<<<>><>>><<<>>><<<>>><><<>>><>>>><<<<>>><<>>>><<<>>>><<<<>>><<<<>>>><<<>>><<><<>>><<>>>><<<>>><<><<<>>>><><<<<><><<><<>><>>>><<>>><><<><<<<>>><<<>>><<<<>>>><>><<<<>><<<<>><<><<<>>><>>>><>>>><<<<>>>><<<<><><<<><>>><<<<>><>><><<<<>>><<<><<><<<<>><<><>>>><>>>><<<>>>><<><<>>><<>><<<<>>><<<<>>>><>>>><<<<>><<>>><<<>>>><<<>>>><<<>>>><<<<>>><<<><<<><>>><<<><>>><<<><>>><>><<<>>><<<>>><<<<>>>><<>><<<>><>><<<<>>><<<>>>><<><<<>>>><<<<><><>>>><<>><>>>><<>>><<>>>><<>>>><>>><>>><<<>>><<>>><>><>>>><<<>>><>><>>>><<<>>><<><<<>>>><<<>><<><<<>>><<<<>>><<<<><<<<>>>><<<>><<<<>>><<<<>>><<>><<<<><<<><<<<>>>><<<<><>>>><>>>><<><<<<>><<>><<>>><>>><>>>><<<>>>><>><<<<>>>><<<<>><<<<>><<<>><<<<><>>>><>><<<>>><>><>>><>>><<<<>>><<>><<<>>><<<<>>><<><<<>>><<<>>>><<>>><<<<>><<<<>>><<><<>>><<<<>>><<<>>><<<<>>><<>>><<<>><<<>>>><<<>><<<<>>>><<>><>>>><<>>><>><<<>><<<<>>>><<>><<<<><<<>>>><<<>>><<>><<<>>>><<>>><<<<>><<>><<>><<<<>>>><<<>>><<<<>>>><<<>>><>>>><<<>>>><<>><<<<>><<>>>><<<<><<<>><<<<><<>>>><<<<>>>><<>>><<<<><<<>>>><<<>><<><<<<><><<>>>><><<<<><<<><<<<>><<><<<<><<<<>><<<>><<>><<<<><<>>><<><<<>><<>>><<<>>>><<>><<>><<<<>>><<<<>><<>>>><<<>>><<<<>><<>>><<><><<><<>>>><>><>>><<<><<<<>><<><<>>><<<<><<>>><>>>><<<><<><<>>>><><>>>><<>><<><>>><<><<<<>><<>>>><<>>><<<>>>><<<><>>><<>>>><>><<><<>><<<><<<>><<>><>><><><<>>>><<<>>><>>><<<<>>><<<>>><<<>><>>><<<<>><><<<><>>>><<>>><>>><<<>>><<<>><>>>><<>>><<<><<<>>>><><<<<>>><<<<>><<>><<<><<<<>><<<>>>><<<><>><<<<><<<<>>><<<>>>><<<<><<<>>><>>>><<<<>>><<><<>>>><<><<>><<>><>><<>>>><<<<>>><>>>><<>>>><<><<<>>><>>><<<>>>><<<<>><<<<><<<><<<><<<><<<>>>><<><<><><>><>>><<<>><>>><<<><>>><<>>><<<<><<<>>><<<<>>><<<<>>><<>>>><<<>>>><<<>><<<<><<<<>><<<><<<><<<>><<>>>><<<>><<<><>>><>>><<><<<>>><<<<>><<<>>>><>><<<>><>>><><<<><<<<><<<><<<>>><<><<>>>><<>>><><<<<>>>><<<>>>><<>><<<>><<>>><<><<<>><<>><<>><<<<>><<<<>><<<>>>><>>>><<>>><<<<><<>><<<>><<>>>><<<<>>><>><>><<<>>>><>>><<<>>><<>><<<<>><<><<<><<<<>><<<<><>><<<>>>><<<>>>><<>>><>><<>>>><<<>><<<>>>><><<<><<>><>><<>><<>>>><<>>><<<<><<><>>><><<<>>><<>>><<<>>><<<>>>><>>><<<<>>>><<<>>><<>><<<>>><<<>>><>>>><<><<<<>>>><<<><<<<>>><<<<>>><>><<<>>>><<><<><<<>>>><><<<>><<<<><<<>>><>>><>><<><<>><<<<>>>><>>><><<<<>>><<>><<<>>><><<<>>>><<<<>>><<>><<<><<><<<<>>>><<<>>>><<<>>>><><>><<<>>>><<><>>>><<<<>>>><<<>>>><<>>><<<<>>>><>>><>>><<>>>><<<><<>>>><><<<<>><<<>>>><<><<<<>>>><<>>>><><<<>>>><>><<<>>>><<>>><<>>><><<<>>><<<>><><<<<>>><<>>>><>>><<<>>><<>>>><<>><<<<><<>><<<>><<<<>>><>><<<<>>><<<>>>><>>>><<<>>>><>>><<<<>>><>><<<<><<<>><>>><>>>><<>>>><<>><<<>><<>>><<<>><<<<><<>><<<<>><<<<>><<<><>>>><>><><<<><<><>>><<<<><<<>><<>>><>>><<<<>><<<><<<>><>>>><<<<><><<>><<<<>><<<<>><>>>><><<<><>>><<<<>>>><<<>>><<>>>><<<>><<<>><>><<<><<<<>>><<<>>>><<<<>>>><<<>><<<<>>><>><<<<>><><<<<>><><<<<>><<>><<<<>>><>>>><<<<>>>><>>><>><>>>><<<>>>><><<<><<<>><<<<>>><<<<>><<<>>><<<<><<<>>><<<>>><><>>>><<<><<<<><<<>><<<<>>><<><<<<>><>>><<<<>>><>><>>>><><<<>>>><<><>>>><<><<<>>><<>>><<<<><>>><<><<>>><<<>>><><<<>>><>>><<<<>>>><<<>>>><<>>><<<<>>>><<>><<<<>><<<<><<>><<<<><<<>>>><<<><>>>><<>>>><<<>>>><<<>><<<>>><<>>>><>>><<<<>><<<<>><>>><<<<>><<>>><<<<><<<<>><<<<>>><<>><<><<<>><<>>>><<<<>><<<<>>><>>>><<>><>>>><<<><<<<>>><>>>><<<>><<<<>><<>>><<<>><<><>><<><>>>><>>>><<<<><>>><>><<<<>>>><<<>>>><<<>>>><<<>>>><<<><<<>>><<<>><<<<><<<><<>><<<>>>><<<>>>><<<<><>>><<><<<<>>>><>><<>>>><<>>>><>>><<<>>>><<><<<<>>>><>><><<<<>><>>><>>>><<<>>><<<<>>><<<<><<<>>>><>><<<><>>><<<<>>><>><>>><<<>><>><<><<<>><>>>><<><<<>>>><><<<>>>><<>><<>>>><>><><<<<><<<>>>><<<><<<>><<<<>><<><<>><>>>><<<<>>>><>><<<<>>>><<<<><>>>><<<><<<<><>><<>><<<>>><>><<<<>>><><<<>>><>><<>><<>>>><<<<>>><<<>>>><<<<><>><<<><<<><<><<<><<<<>>>><><><<><<>>><<>>><<>><>>><>>>><<><<<><>>><<<<>><<><<>><<<<>><<>>>><<<>>>><>>><<<>>><<<>>><<<>><>><<<<>>>><<>>>><<<>>>><>><<<>>>><<<>>>><<<>>><<>><<>><<<<><<><>><><<>><<>>>><<<>><>>><><<><<<><<>><<>>><<<>>>><<><>>>><<<<><<>>><><<<<>><<<>><<<<><<><<>>><>><>>>><<>>>><<<>>><<>>>><<<<>>>><<<>>>><>>>><>>><<<><>><<><>><<<<>>><<<<>>>><<<<>>>><>><><<<>>>><<<<>><<>>>><<<<><><<<>>>
''')
