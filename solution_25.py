def from_snafu(number, index=0):
    if index == len(number) - 1:
        return int(number[len(number) - 1 - index]) * pow(5, index)
    add = 0
    digit = number[len(number) - 1 - index]
    if digit == "-":
        add = -1
    elif digit == "=":
        add = -2
    else:
        add = int(digit)
    value = from_snafu(number, index + 1)
    return value + (pow(5, index) * add)


def resolve_digit(number, power):
    place = pow(5, power)
    max_sub_number = sum([2 * pow(5, x) for x in range(power)])
    if place - max_sub_number > abs(number):
        return "0"
    if number < 0:
        if place * 2 + number <= max_sub_number:
            return "="
        return "-"
    else:
        if place + max_sub_number >= number:
            return "1"
        return "2"


def to_snafu(number, power=0):
    max = 0
    max_power = 0
    while True:
        max += pow(5, max_power)
        if max >= number or max * 2 >= number:
            break
        max_power += 1
    power = max_power
    snafu = ""
    remainder = number
    while power >= 0:
        snafu += resolve_digit(remainder, power)
        value = from_snafu(snafu, 0)
        value *= pow(5, power)
        remainder = number - value
        power -= 1
    return snafu


def solve(puzzle_input):
    numbers = [x for x in puzzle_input.strip().split("\n")]
    total = 0
    for number in numbers:
        value = from_snafu(number)
        total += value
    print(to_snafu(total))
    return


solve('''
21020=22-2=11002=2
2--221202=102-
22120-
1=0000=1-2=
10=221
110=1121002-10--=
10=00==--121==0=
202=-1221
101-01-
12==-
221101-=110=0
1=-=2-12-2202=
1=0-02-=0102-=-12
1==-0
1=212--00
202
1-11121--21-21=-2
22--2-=-2
2-00-0=---2-==-
1=2=-2-=0--1-22
1=000=0-112
121=-001=0
110-=-020--=0
1=0-1
2=0--==0
102=21=201=-21=21
11-22=-22=1-0=
1011----1----2-1
2===-00022
12-
20=0
10=011=00=0-
20-=0-0-1=2====0-2
2000-01011=001=
1=0-01
2=-1
12=10--=-1-
2=21=12=
22=21-0
1==-02202==--
1===
210020-122222202=
102-20211212==11---
1020=221-00=01
1=2=1=0---10
111-
1=02
10-10=-2-0=11
1002-
1-
2=12112-
20=202-=01=2-1
1=-
1=-=222221=1102012
20-1=02=--
2=2-=
1=1
1-0==1122-02==2=
1-20-0-=0=0
1=022-11-122-0010
1021===1
1=2020--
2=0==00-==0011
1--220-0=-=1-2=01---
2=1=021010=2=1=-
21=2-==22-==0=-010
200-=1
212-
21---=-022-22
1121211-110-00-10
22-=1
1=-=2-2100--=1=02
1=0
11102-202==122-=00
2=1-=
1=11--00
211-012--2
1=1021012100
12-101==-110102
1==--2-==-==1-=-
1===21-
2---1100112010202
1200-112=11=-0
1220--00-21--11
12-=0-00-=
100122==---=0
2221-==-210101==
202-1=1
100==12101=2=
102
210=20=11
12-=-=2--1-=---=20=
2222001
12=0
2--=20-10--10
2-1020000-1=1-
1-1
1101-111-
1==201=--==
2=
2=0=
12=
11=
1==
1-10000-2=
21=-21
10-=--20-2-00===
202122-
1=02--10011
1==-0-1=2111-12=2-2
20
1==-
2=-0-=222=-02=
1110=1-=1022-
122=2==0=2222--12
10111000-=2--=0--0
1-22
2=10-0=--21
1===-
1=022-
1=2===2-
22211=--10120120=0
101--=111101-=11
1212=10
20100
12=112=11==01
202111=--2===0
''')
