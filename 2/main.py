import re

def run():

    # rules = {"red": 12, "green":13, "blue":14}
    res = 0
    with open("input.txt") as f:
        for line in f:
            line_split = re.split('Game \n|:|;', line)
            game_id = line_split[0][4:]
            powers = {}
            for i in range(1, len(line_split)):
                for group in line_split[i].split(','):
                    num, color = group.strip().split(' ')
                    num = int(num)
                    if color in powers:
                        powers[color] = max(powers[color], num)
                    else:
                        powers[color] = num
            product = 1
            for i in powers.values():
                product *= i
            res += product
                
    print(res)

run()