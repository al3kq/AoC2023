

def main():
    res = 0
    with open("input.txt") as f:
        for line in f:
            line = line.split(": ")[1]
            win_nums, my_nums = line.split('|')

            winning_list = [int(i) for i in win_nums.split(" ") if i != '']
            my_numbers = [int(i) for i in my_nums.split(" ") if i != '']
            matching_numbers = len(list(set(winning_list) & set(my_numbers)))
            if matching_numbers > 0:
                res += (2**(matching_numbers-1))

    print(res)
main()