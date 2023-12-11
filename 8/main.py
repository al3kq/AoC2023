import itertools
import math
from functools import reduce

def check_all_in_set(lst, s):
    return all(item in s for item in lst)

def check_start_filled(start):
    return all(value != 0 for value in start.values())

def main():
    with open('input.txt', 'r') as file:
        direction = list(file.readline().strip())
        direction = [0 if char == 'L' else 1 for char in direction]
        starts = {}
        ends = set()
        mapping = {}
        for line in file:
            if line.strip() != "":
                key, var = line.split(" = ")
                mapping[key] = var.strip().replace('(', '').replace(')', '').split(', ')
                if key[-1] == 'A':
                    starts[key] = 0
                elif key[-1] == 'Z':
                    ends.add(key)

        for curr in starts.keys():
            direction_cycle = itertools.cycle(direction)
            steps = 0
            begin = curr
            while curr not in ends:
                direction_step = next(direction_cycle)
                curr = mapping[curr][direction_step]
                steps += 1
            starts[begin] = steps

        return reduce(lambda a, b: math.lcm(a,b), starts.values())


if __name__ == "__main__":
    print(main())