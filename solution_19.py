import re


def find_max_geodes(bp, bots, r, time, memo):
    if time == 0:
        return r[3]

    # we eventually reach an effective resource maximum. once we have enough bots, having more resources than needed to
    # construct any bot type is not necessary, so we can effectively cap it
    max_ore = max(bp[1], bp[2], bp[3], bp[5])
    max_cly = bp[4]
    max_obs = bp[6]

    key = (bots, time)
    if key in memo:
        # ugly stuff going on here, but it works!
        memo_r, memo_geodes = memo[key]
        if memo_r[0] >= r[0] and memo_r[1] >= r[1] and memo_r[2] >= r[2] and memo_r[3] >= r[3]:
            return memo_geodes
        # even if we could make a new geode bot each minute, would it matter?
        geode_bots = bots[3]
        geodes = r[3]
        t = time
        while t > 0:
            geodes += geode_bots
            geode_bots += 1
            t -= 1
        if geodes < memo_geodes:
            return memo_geodes

    if bots[0] >= bp[5] and bots[2] >= bp[6]:
        # we have everything we need to make a geode bot each minute. calculate that
        geode_bots = bots[3]
        geodes = r[3]
        while time > 0:
            geodes += geode_bots
            geode_bots += 1
            time -= 1
        return geodes

    builds = []
    if r[0] >= bp[1] and bots[0] < max_ore:
        # build an ore bot
        builds.append(
            ((bots[0] + 1, bots[1], bots[2], bots[3]), (r[0] - bp[1], r[1], r[2], r[3])))
    if r[0] >= bp[2] and bots[1] < max_cly:
        # build a clay bot
        builds.append(
            ((bots[0], bots[1] + 1, bots[2], bots[3]), (r[0] - bp[2], r[1], r[2], r[3])))
    if r[0] >= bp[3] and r[1] >= bp[4] and bots[3] < max_obs:
        # build an obsidian bot
        builds.append(((bots[0], bots[1], bots[2] + 1, bots[3]),
                       (r[0] - bp[3], r[1] - bp[4], r[2], r[3])))
    if r[0] >= bp[5] and r[2] >= bp[6]:
        # build a geode bot
        builds.append(((bots[0], bots[1], bots[2], bots[3] + 1),
                       (r[0] - bp[5], r[1], r[2] - bp[6], r[3])))

    max_geodes = 0
    for build in builds:
        new_bots = build[0]
        new_r = build[1]

        new_r = (
            new_r[0] + bots[0],
            new_r[1] + bots[1],
            new_r[2] + bots[2],
            new_r[3] + bots[3]
        )

        max_geodes = max(max_geodes, find_max_geodes(
            bp, new_bots, new_r, time - 1, memo))

    new_r = (
        r[0] + bots[0],
        r[1] + bots[1],
        r[2] + bots[2],
        r[3] + bots[3]
    )
    max_geodes = max(max_geodes, find_max_geodes(
        bp, bots, new_r, time - 1, memo))

    memo[key] = (r, max_geodes)
    return max_geodes


def solve(puzzle_input):
    blueprints = [tuple(int(y) for y in re.search(r'(\d+).* (\d+) .* (\d+) .* (\d+) .* (\d+) .* (\d+) .* (\d+)', x).groups())
                  for x in puzzle_input.strip().split("\n")]

    quality_sum = 0
    for bp in blueprints:
        max_geodes = find_max_geodes(
            bp, (1, 0, 0, 0), (0, 0, 0, 0), 24, {})
        quality_level = max_geodes * bp[0]
        quality_sum += quality_level
    print(quality_sum)

    foo = 1
    for bp in blueprints[:3]:
        max_geodes = find_max_geodes(
            bp, (1, 0, 0, 0), (0, 0, 0, 0), 32, {})
        foo *= max_geodes
    print(foo)

    return


solve('''
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 3 ore and 18 obsidian.
Blueprint 2: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 3: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 13 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 5: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 4 ore and 15 obsidian.
Blueprint 6: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 7: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 4 ore and 17 obsidian.
Blueprint 8: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 9: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 2 ore and 13 obsidian.
Blueprint 10: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 7 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 12: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 13: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 14: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 6 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 15: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 16: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 18: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 13 obsidian.
Blueprint 19: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 9 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 20: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 21: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 17 obsidian.
Blueprint 22: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 14 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 23: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 3 ore and 18 obsidian.
Blueprint 24: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 25: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 3 ore and 13 obsidian.
Blueprint 26: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 9 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 27: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 28: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 15 clay. Each geode robot costs 2 ore and 8 obsidian.
Blueprint 29: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 30: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 10 clay. Each geode robot costs 2 ore and 11 obsidian.
''')
