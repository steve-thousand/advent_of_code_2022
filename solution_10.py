cycle = 0
X = 1
signal_strengths = []
pixel_buffer = []


def signal_strength(cycle):
    if abs(cycle - 20) % 40 == 0:
        signal_strengths.append(cycle * X)


def draw():
    global pixel_buffer
    pixel = len(pixel_buffer)
    if abs(X - pixel) <= 1:
        pixel_buffer.append("#")
    else:
        pixel_buffer.append(".")
    pixel += 1
    if len(pixel_buffer) == 40:
        print(''.join(pixel_buffer))
        pixel_buffer = []
        pixel = 1


def run_cycle():
    global cycle
    cycle += 1
    signal_strength(cycle)
    draw()


def solve(puzzle_input):
    instructions = [[y for y in x.split(" ")]
                    for x in puzzle_input.strip().split("\n")]

    global X

    for instruction in instructions:
        if instruction[0] == 'noop':
            run_cycle()
        elif instruction[0] == 'addx':
            run_cycle()
            run_cycle()
            X += int(instruction[1])

    print(sum(signal_strengths))
    return


solve('''
addx 2
addx 3
noop
noop
addx 1
addx 5
addx -1
addx 5
addx 1
noop
noop
addx 4
noop
noop
addx 5
addx -5
addx 6
addx 3
addx 1
addx 5
addx 1
noop
addx -38
addx 41
addx -22
addx -14
addx 7
noop
noop
addx 3
addx -2
addx 2
noop
addx 17
addx -12
addx 5
addx 2
addx -16
addx 17
addx 2
addx 5
addx 2
addx -30
noop
addx -6
addx 1
noop
addx 5
noop
noop
noop
addx 5
addx -12
addx 17
noop
noop
noop
noop
addx 5
addx 10
addx -9
addx 2
addx 5
addx 2
addx -5
addx 6
addx 4
noop
noop
addx -37
noop
noop
addx 17
addx -12
addx 30
addx -23
addx 2
noop
addx 3
addx -17
addx 22
noop
noop
noop
addx 5
noop
addx -10
addx 11
addx 4
noop
addx 5
addx -2
noop
addx -6
addx -29
addx 37
addx -30
addx 27
addx -2
addx -22
noop
addx 3
addx 2
noop
addx 7
addx -2
addx 2
addx 5
addx -5
addx 6
addx 2
addx 2
addx 5
addx -25
noop
addx -10
noop
addx 1
noop
addx 2
noop
noop
noop
noop
addx 7
addx 1
addx 4
addx 1
noop
addx 2
noop
addx 3
addx 5
addx -1
noop
addx 3
addx 5
addx 2
addx 1
noop
noop
noop
noop
''')
