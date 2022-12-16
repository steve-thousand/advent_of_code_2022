import re


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def scan_y(Y, data):
    beacon_manhattan_distances = {}
    beacons = set()
    beacons_at_y = set()
    for row in data:
        beacon_manhattan_distances[(row[0], row[1])] = manhattan_distance(
            (row[0], row[1]), (row[2], row[3]))
        beacons.add(((row[2], row[3])))
        if row[3] == Y:
            beacons_at_y.add(row[2])

    ranges_without_beacons = []
    for sensor in beacon_manhattan_distances:
        X = sensor[0]
        beacon_distance = beacon_manhattan_distances[sensor]
        if Y <= sensor[1] + beacon_distance and Y >= sensor[1] - beacon_distance:
            # range of covered cells at given Y
            diff = abs(beacon_distance - abs(sensor[1] - Y))
            ranges_without_beacons.append((X - diff, X + diff))

    # collapse ranges
    ranges_without_beacons.sort(key=lambda x: x[0])
    new_ranges_without_beacons = [ranges_without_beacons[0]]
    i = 1
    while i < len(ranges_without_beacons):
        range1 = new_ranges_without_beacons.pop()
        range2 = ranges_without_beacons[i]
        if (range1[1] >= range2[0] and range1[0] <= range2[1]) or (range1[1] == range2[0] - 1):
            new_range = (min(range1[0], range2[0]),
                         max(range1[1], range2[1]))
            new_ranges_without_beacons.append(new_range)
        else:
            new_ranges_without_beacons.extend([range1, range2])
        i += 1
    ranges_without_beacons = new_ranges_without_beacons

    found_space = None
    if len(ranges_without_beacons) > 1:
        found_space = (ranges_without_beacons[0][1] + 1, Y)

    # split regions by present beacons
    if len(ranges_without_beacons) > 0:
        split_by_range = []
        for x in beacons_at_y:
            for this_range in ranges_without_beacons:
                if this_range[0] <= x and this_range[1] >= x:
                    split_by_range.append((this_range[0], x - 1))
                    split_by_range.append((x + 1, this_range[1]))
                else:
                    split_by_range.append(this_range)
            ranges_without_beacons = split_by_range

    total_empty_cells = 0
    for ranges in ranges_without_beacons:
        total_empty_cells += ranges[1] - ranges[0] + 1

    return (total_empty_cells, found_space)


def solve(puzzle_input):
    data = [[int(y) for y in re.search(r'Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)', x).groups()]
            for x in puzzle_input.strip().split("\n")]
    result = scan_y(2000000, data)
    print(result[0])

    # kinda slow but i dont care
    for y in range(0, 4000000):
        result = scan_y(y, data)
        if result[1] is not None:
            print(result[1][0] * 4000000 + result[1][1])
            break

    return


solve('''
Sensor at x=3907621, y=2895218: closest beacon is at x=3790542, y=2949630
Sensor at x=1701067, y=3075142: closest beacon is at x=2275951, y=3717327
Sensor at x=3532369, y=884718: closest beacon is at x=2733699, y=2000000
Sensor at x=2362427, y=41763: closest beacon is at x=2999439, y=-958188
Sensor at x=398408, y=3688691: closest beacon is at x=2275951, y=3717327
Sensor at x=1727615, y=1744968: closest beacon is at x=2733699, y=2000000
Sensor at x=2778183, y=3611924: closest beacon is at x=2275951, y=3717327
Sensor at x=2452818, y=2533012: closest beacon is at x=2733699, y=2000000
Sensor at x=88162, y=2057063: closest beacon is at x=-109096, y=390805
Sensor at x=2985370, y=2315046: closest beacon is at x=2733699, y=2000000
Sensor at x=2758780, y=3000106: closest beacon is at x=3279264, y=2775610
Sensor at x=3501114, y=3193710: closest beacon is at x=3790542, y=2949630
Sensor at x=313171, y=1016326: closest beacon is at x=-109096, y=390805
Sensor at x=3997998, y=3576392: closest beacon is at x=3691556, y=3980872
Sensor at x=84142, y=102550: closest beacon is at x=-109096, y=390805
Sensor at x=3768533, y=3985372: closest beacon is at x=3691556, y=3980872
Sensor at x=2999744, y=3998031: closest beacon is at x=3691556, y=3980872
Sensor at x=3380504, y=2720962: closest beacon is at x=3279264, y=2775610
Sensor at x=3357940, y=3730208: closest beacon is at x=3691556, y=3980872
Sensor at x=1242851, y=838744: closest beacon is at x=-109096, y=390805
Sensor at x=3991401, y=2367688: closest beacon is at x=3790542, y=2949630
Sensor at x=3292286, y=2624894: closest beacon is at x=3279264, y=2775610
Sensor at x=2194423, y=3990859: closest beacon is at x=2275951, y=3717327
''')
