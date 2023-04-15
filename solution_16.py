import re


def parse_line(line):
    valve = line[6:8]
    flow_rate = int(re.search(r'(\d+)', line).group(0))
    leads_to = re.search(r'to valves? ([A-Z,\s]+)', line).group(1).split(", ")
    return [valve, flow_rate, leads_to]


def dynamic(valves, valves_with_pressure, distances, open_valves, current_valve, minutes, elephant=None):
    pressure_relieved_so_far = 0
    for valve in open_valves:
        pressure_relieved_so_far += valves[valve][0] * \
            (30 - open_valves[valve])

    if minutes == 30 or len(open_valves) == len(valves_with_pressure):
        return pressure_relieved_so_far

    pressures_relieved = [pressure_relieved_so_far]

    for next_valve in distances[current_valve]:
        for next_valve_elephant in [None] if elephant is None else distances[current_valve]:
            if next_valve not in open_valves and next_valve in valves_with_pressure:
                open_valves_clone = open_valves.copy()
                minutes_to_open = distances[current_valve][next_valve] + 1
                if minutes + minutes_to_open <= 30:
                    open_valves_clone[next_valve] = minutes + minutes_to_open
                    pressure_relieved = dynamic(
                        valves, valves_with_pressure, distances, open_valves_clone, next_valve, minutes + minutes_to_open, elephant)
                    if pressure_relieved is not None:
                        pressures_relieved.append(pressure_relieved)

    return max(pressures_relieved)


def solve(puzzle_input):
    valves = {i[0]: i[1:]
              for i in list(map(parse_line, puzzle_input.strip().split("\n")))}

    valves_with_pressure = [x for x in list(valves.keys()) if valves[x][0] > 0]

    distances = {}
    for valve in valves:
        if valve not in distances:
            distances[valve] = {}
        frontier = [(valve, 0)]
        while len(frontier) > 0:
            frontier_node = frontier.pop(0)
            frontier_valve = frontier_node[0]
            frontier_distance = frontier_node[1]
            if frontier_valve != valve:
                distances[valve][frontier_valve] = frontier_distance
            for next_valve in valves[frontier_valve][1]:
                if next_valve not in distances[valve] or distances[valve][next_valve] > frontier_distance + 1:
                    frontier.append((next_valve, frontier_distance + 1))

    print(dynamic(valves, valves_with_pressure, distances, {}, 'AA', 0))

    print("HAVEN'T SOLVED PART 2 YET")
    # print(dynamic(valves, valves_with_pressure, distances, {}, 'AA', 4, 'AA'))

    return


solve('''
Valve FY has flow rate=0; tunnels lead to valves TG, CD
Valve EK has flow rate=12; tunnels lead to valves JE, VE, PJ, CS, IX
Valve NU has flow rate=0; tunnels lead to valves FG, HJ
Valve AY has flow rate=0; tunnels lead to valves EG, KR
Valve DH has flow rate=0; tunnels lead to valves FX, VW
Valve IX has flow rate=0; tunnels lead to valves VW, EK
Valve DZ has flow rate=0; tunnels lead to valves HT, FG
Valve YE has flow rate=0; tunnels lead to valves CI, MS
Valve OO has flow rate=0; tunnels lead to valves FX, CS
Valve SB has flow rate=0; tunnels lead to valves RR, AP
Valve HT has flow rate=4; tunnels lead to valves DZ, GA, CI, DE, JS
Valve MS has flow rate=11; tunnels lead to valves PJ, WG, CA, YE
Valve CD has flow rate=0; tunnels lead to valves UW, FY
Valve IZ has flow rate=0; tunnels lead to valves XF, AP
Valve JE has flow rate=0; tunnels lead to valves EK, TQ
Valve DN has flow rate=0; tunnels lead to valves KR, VE
Valve VW has flow rate=13; tunnels lead to valves DH, IX
Valve UH has flow rate=0; tunnels lead to valves MN, TQ
Valve TB has flow rate=0; tunnels lead to valves AP, BJ
Valve XT has flow rate=0; tunnels lead to valves TQ, UW
Valve RR has flow rate=0; tunnels lead to valves FG, SB
Valve BJ has flow rate=0; tunnels lead to valves TB, AA
Valve DE has flow rate=0; tunnels lead to valves HT, WI
Valve MT has flow rate=0; tunnels lead to valves EW, FG
Valve HJ has flow rate=0; tunnels lead to valves KS, NU
Valve WI has flow rate=3; tunnels lead to valves XF, DX, DE, EW
Valve KI has flow rate=0; tunnels lead to valves GW, TQ
Valve JS has flow rate=0; tunnels lead to valves UW, HT
Valve XF has flow rate=0; tunnels lead to valves WI, IZ
Valve VE has flow rate=0; tunnels lead to valves DN, EK
Valve CI has flow rate=0; tunnels lead to valves YE, HT
Valve GW has flow rate=0; tunnels lead to valves EG, KI
Valve TQ has flow rate=14; tunnels lead to valves WG, KI, JE, UH, XT
Valve AA has flow rate=0; tunnels lead to valves BJ, CF, DX, RB, AQ
Valve EW has flow rate=0; tunnels lead to valves MT, WI
Valve UW has flow rate=6; tunnels lead to valves XT, CD, NZ, JS
Valve MN has flow rate=0; tunnels lead to valves KR, UH
Valve FG has flow rate=8; tunnels lead to valves NU, RR, MT, MK, DZ
Valve RB has flow rate=0; tunnels lead to valves NZ, AA
Valve AQ has flow rate=0; tunnels lead to valves AA, MK
Valve WG has flow rate=0; tunnels lead to valves TQ, MS
Valve YW has flow rate=0; tunnels lead to valves CA, KR
Valve CA has flow rate=0; tunnels lead to valves YW, MS
Valve PJ has flow rate=0; tunnels lead to valves MS, EK
Valve EG has flow rate=23; tunnels lead to valves AY, GW
Valve NC has flow rate=0; tunnels lead to valves TG, KS
Valve WY has flow rate=16; tunnel leads to valve VQ
Valve AP has flow rate=7; tunnels lead to valves IZ, VQ, TB, SB
Valve CF has flow rate=0; tunnels lead to valves GA, AA
Valve FX has flow rate=20; tunnels lead to valves DH, OO
Valve NZ has flow rate=0; tunnels lead to valves RB, UW
Valve KS has flow rate=19; tunnels lead to valves NC, HJ
Valve VQ has flow rate=0; tunnels lead to valves WY, AP
Valve TG has flow rate=17; tunnels lead to valves NC, FY
Valve GA has flow rate=0; tunnels lead to valves CF, HT
Valve CS has flow rate=0; tunnels lead to valves OO, EK
Valve MK has flow rate=0; tunnels lead to valves AQ, FG
Valve KR has flow rate=18; tunnels lead to valves MN, DN, YW, AY
Valve DX has flow rate=0; tunnels lead to valves AA, WI
''')
