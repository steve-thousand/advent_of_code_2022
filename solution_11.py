def parse_monkey(monkey):
    parts = [line.strip() for line in monkey.split('\n')]

    rhs = parts[2][23:]
    if parts[2][21:22] == "+":
        if rhs == "old":
            def operation(x):
                return x + x
        else:
            rhs = int(rhs)

            def operation(x):
                return x + rhs
    else:
        if rhs == "old":
            def operation(x):
                return x * x
        else:
            rhs = int(rhs)

            def operation(x):
                return x * rhs

    return (int(parts[0][7:-1]), [int(x) for x in parts[1][16:].split(", ")], operation, int(parts[3][19:]), int(parts[4][25:]), int(parts[5][26:]))


def simulate(monkeys, worry_divisor=3, rounds=20):
    inspections = []
    common_denominator = 1
    for i in range(0, len(monkeys)):
        inspections.append(0)
        common_denominator *= monkeys[i][3]

    for i in range(0, rounds):
        for monkey in monkeys:
            while len(monkey[1]) > 0:
                item = monkey[1].pop(0) % common_denominator
                inspections[monkey[0]] += 1
                worry = int(monkey[2](item) / worry_divisor)
                if worry % monkey[3] == 0:
                    monkeys[monkey[4]][1].append(worry)
                else:
                    monkeys[monkey[5]][1].append(worry)

    inspections.sort()
    return inspections[-1] * inspections[-2]


def solve(puzzle_input):
    monkeys = [parse_monkey(monkey)
               for monkey in puzzle_input.strip().split('\n\n')]
    print(simulate(monkeys))

    monkeys = [parse_monkey(monkey)
               for monkey in puzzle_input.strip().split('\n\n')]
    print(simulate(monkeys, 1, 10000))
    return


solve('''
Monkey 0:
  Starting items: 52, 78, 79, 63, 51, 94
  Operation: new = old * 13
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 1:
  Starting items: 77, 94, 70, 83, 53
  Operation: new = old + 3
  Test: divisible by 7
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 2:
  Starting items: 98, 50, 76
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 3:
  Starting items: 92, 91, 61, 75, 99, 63, 84, 69
  Operation: new = old + 5
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 4:
  Starting items: 51, 53, 83, 52
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 76, 76
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 75, 59, 93, 69, 76, 96, 65
  Operation: new = old * 19
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 7:
  Starting items: 89
  Operation: new = old + 2
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 4
''')
