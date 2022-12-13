def to_height(char):
    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'
    return ord(char) - 97


def walk(grid, start, end, up):
    came_from = {}

    frontier = set([start])
    came_from[start] = (start, 0)
    while len(frontier) > 0:
        frontier_list = list(frontier)
        frontier_list.sort(key=lambda x: came_from[x][1])

        cell = frontier_list.pop(0)
        frontier = set(frontier_list)
        distance = came_from[cell][1]
        height = to_height(grid[cell[0]][cell[1]])

        if cell == end:
            break

        ADJACENT_CELLS = [(cell[0] - 1, cell[1]),  # UP
                          (cell[0], cell[1] + 1),  # RIGHT
                          (cell[0] + 1, cell[1]),  # DOWN
                          (cell[0], cell[1] - 1)]  # LEFT
        for A in ADJACENT_CELLS:

            # only visit an adjacent cell if:
            #   - it is a valid cell
            #   - it is low enough to be reached from current level
            #   - we haven't already visited it with a shorter path

            if A[0] < 0 or A[0] >= len(grid) or A[1] < 0 or A[1] >= len(grid[A[0]]):
                continue

            NEXT_HEIGHT = to_height(grid[A[0]][A[1]])
            if up:
                if NEXT_HEIGHT - height > 1:
                    continue
            else:
                if height - NEXT_HEIGHT > 1:
                    continue

            if A not in came_from or came_from[A][1] > distance + 1:
                came_from[A] = (cell, distance + 1)
                frontier.add(A)

    return came_from


def solve(puzzle_input):
    grid = [[y for y in x] for x in puzzle_input.strip().split("\n")]

    END = START = (0, 0)
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 'S':
                START = (y, x)
            elif grid[y][x] == 'E':
                END = (y, x)

    distances = walk(grid, START, END, True)
    print(distances[END][1])

    min_distance = 1_000_000  # lol
    distances = walk(grid, END, None, False)
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 'a' and (y, x) in distances:
                min_distance = min(min_distance, distances[(y, x)][1])
    print(min_distance)

    return


solve('''
abcccaaaaaaccccccccaaaaaccccccaaaaaaccccccaaaaaaaacccaaaaaaaccaaaacccccccccccccccccccccccccaaaaaacccccccccccccccccccccccccccccaaaaaa
abcccaaaaaacccccccaaaaaaccccaaaaaaaacccccccaaaaaaaaaaaaaaaaccaaaaacccccccccccccccccccccccccaaaaaacccccccccccccccccccccccccccccaaaaaa
abccccaaaaacaaaccaaaaaaaacccaaaaaaaaacccccccaaaaaaaaaaaaaaaacaaaaaacccccccccaaacccccccccccaaaaaaaaccccccccccaaccccccccccccccccaaaaaa
abccccaaaaccaaaaaaaaaaaaacccaaaaaaaaaacccccaaaaaaaaaaaaaaaaaaacaaaacccccccccaaaacccccccccaaaaaaaaaacccccccccaaaccccccccccccccccccaaa
abcccccccccaaaaaacccaacccccccccaaacaaaccccccaacccccccaaaaaaaaacaacccccccccccaaaacccccccccaaaaaaaaaacccccccccaaaccacaaccccccccccccaaa
abcccccccccaaaaaacccaacccccccccaaacccccccccccccccccccaaaacaaaacccccccaacaaccaaaccccccccccaccaaaaacacccccccccaaaacaaaaccccccccccccaac
abccccccccccaaaaacccccccccccccccacccaaaacccccccccccccaaaacccccccccccccaaaacccccccccccaacccccaaaaccccccccjjjjaaaaaaaaaccccccccccccccc
abccccccccccaaaacccccccccccccccccccaaaaacccccccccccccaaaccccccccccccccaaaaacccccccccaaaaaacccaaccccccccjjjjjjkkaaaacccccccccaacccccc
abcccccaaccccccccccccccccccccccccccaaaaaacccccccccccccaacccccccccccccaaaaaaccccccccccaaaaaccccccccccccjjjjjjjkkkkaacccccaacaaacccccc
abccaaaacccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccaaaacaccccccccaaaaaaaccccaacccccjjjjoooookkkkkkkklllaaaaaaacccc
abccaaaaaacccccccccccccccccccccccccaaaaacccccccccccccccccccccccccccccccaaccccccccccaaaaaaaaccaaaaccccjjjoooooookkkkkkkllllaaaaaacccc
abcccaaaaacccccccccccccccccccccccccccaaaccccccccaaaacccccccccccccccccccccccccccccccaaaaaaaaccaaaaccccjjooooooooppkkppplllllaccaacccc
abccaaaaaccccccccccccaccccccccccccccccccccccccccaaaacccccccccccccccccccccccccccccccccaaacacccaaaacccijjooouuuuoppppppppplllccccccccc
abcccccaacccccccccccaaaaaaaaccccccccccccccccccccaaaaccccaaccccccccaaacccccccccccccaacaaccccccccccccciijoouuuuuuppppppppplllcccaccccc
abcccccccccccccccccccaaaaaaccccccccccccccccccccccaaccccaaaacccccccaaaaccccccccccaaaaaaccccccccccccciiiiootuuuuuupuuuvvpppllccccccccc
abcccccccccccccccccccaaaaaaccaaaaacccccccccccccccccccccaaaacccccccaaaaccccccccccaaaaaaccccccccccccciiinnotuuxxxuuuuvvvpppllccccccccc
abccccccccccccccacccaaaaaaaacaaaaaaacccccccccccccccccccaaaacccccccaaacccccaaaaccaaaaaccccaaccccccciiiinnnttxxxxuuyyyvvqqqllccccccccc
abcccccccccccaaaaccaaaaaaaaaaaaaaaaaaccaacccccccccccccccccccccccccccccccccaaaacccaaaaaccaaacccccciiinnnnnttxxxxxyyyyvvqqqllccccccccc
abaaaacccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccaaaacccaaaaaacaaaccccciiinnnnttttxxxxxyyyyvvqqmmmccccccccc
abaaaaccccccccaaaaacccaaaaacaaaaaacaaaaaaccccccccccccccccaaccccccccccccccccaacccccccaaaaaaaaaaciiinnnnttttxxxxxyyyyvvqqqmmmccccccccc
SbaaaacccccccaaaaaccccaaaaaccaaaaaaaaaaaccccccccccccccccaaacaacccccccccccccccccccccccaaaaaaaaachhhnnntttxxxEzzzzyyvvvqqqmmmccccccccc
abaaaacccccccaacaacccccaaaaaaaacaaaaaaaaaccccccccccccccccaaaaaccccccccccccccccccccccccaaaaaaacchhhnnntttxxxxxyyyyyyvvvqqmmmdddcccccc
abaaaacccccccccccccccccccaaaaaacaaaaaaaaaacccccccccccccaaaaaaccccccccaaaccccccccccccccaaaaaaccchhhnnntttxxxxywyyyyyyvvvqqmmmdddccccc
abaacccccccccccccccccccaaaaaaacccccaaaaaaacccccccccccccaaaaaaaacccccaaaacccccccccccccaaaaaaacaahhhmmmttttxxwwyyyyyyyvvvqqmmmdddccccc
abcccccccccccccccccccccaaaaaaacaaccaaacccccccccccccccccaacaaaaacccccaaaacccccccccccccaaacaaaaaahhhmmmmtsssswwyywwwwvvvvqqqmmdddccccc
abcccccccccccccccaaaccccaaaaaaaaaacaaccaaccccccccccccccccaaacaccccccaaaacccccccccccccccccaaaaacahhhmmmmmsssswwywwwwwvvrrqqmmdddccccc
abcccccccccccccaaaaaaccccaaaaaaaaaccaaaacccccccccccccccccaacccccccccccccccccccccccaaaccccaaaaaaahhhhhmmmmssswwwwwrrrrrrrrmmmmddccccc
abcccccccccccccaaaaaaccccaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccaaaaaacccccaaaaachhhhhmmmmsswwwwrrrrrrrrrkkmdddccccc
abccccccccccccccaaaaaccccccaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccaaaaaaccccaaaaacccchhggmmmssswwrrrrrkkkkkkkkdddacccc
abccaaaacccccccaaaaacccccccccaaaaaacaaaaacccccccccccccccccccccccccccccccccccccccaaaaaaccccaacaaaccccggggmmsssssrrlkkkkkkkkkdddaccccc
abccaaaacccccccaaaaacccccccccaaaaaaccccaacccccccccccccccccccccccccccccccccccccccaaaaaccccccccaaccccccgggmllssssrllkkkkkkkeeeddaccccc
abccaaaacccccccaaacccccccccccaaaaaacccccccccccccccccccaacccccccccccccccccccccccaaaaaacccccccccccccccccggllllssslllkkeeeeeeeeeaaacccc
abcccaaccccccccaaacaaaccccccaaaaaaaaaaacccccccccccccaaaaaacccccccccccccccccccccaaacaaacccccaacccccccccggglllllllllfeeeeeeeeaaaaacccc
abccccccccccaaaaaaaaaaccccccccccccaccaaaccacccccccccaaaaaaccccaaccaacccaaccccccaaaaaaacccccaaccccccccccggglllllllfffeeecccaaaaaacccc
abccccccccccaaaaaaaaacccccccccccccccaaaaaaaccccccccccaaaaaccccaaaaaacccaaaaaaccaaaaaacccaaaaaaaacccccccggggllllfffffccccccaacccccccc
abcccccccccccaaaaaaacccccccccccccccccaaaaaaccaacccccaaaaaccccccaaaaacccaaaaaacaaaaaaacccaaaaaaaaccccccccgggffffffffccccccccccccccccc
abccccccccccccaaaaaaacccccccccccccaaaaaaaaacaaaaccccaaaaacaaaaaaaaaacaaaaaaacaaaaaaaaaccccaaaacccccccccccggffffffacccccccccccccccaaa
abccccccccccccaaaaaaacaaccccccccccaaaaaaaaacaaaacccccaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaacccaaaaacccccccccccaffffaaaaccccccccccccccaaa
abccccccccccccaaacaaaaaacccccccccccaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaacaaaaaaacccaaacaaaccaaaaaacccccccccccccccccaaaccccccccccccccaaa
abccccccccccccaaccaaaaaccccccccccccccaaaaaaaccccaaaaaaaaaaaaccccaacccccaaaaaacccaaaccccccaaccaacccccccccccccccccaaacccccccccccaaaaaa
abcccccccccccccccaaaaaaaaccccccccccccaacccacccccccaaaaaaaaaaccccaacccccaaccccccccaccccccccccccccccccccccccccccccccccccccccccccaaaaaa
''')
