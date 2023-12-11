

def run():
    sum = 0
    with open("input.txt") as f:
        for line in f:
            l, r = -1, -1
            for i in line:
                if i.isdigit():
                    if l == -1:
                        l = int(i)
                        r = int(i)
                    else:
                        r = int(i)
            total = (l*10) + r
            sum += total
    print(sum)


def __main__():
    run()

__main__()