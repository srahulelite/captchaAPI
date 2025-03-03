# Average of n numbers where n is the input of a function

def avg(num1, num2, num3):
    """This function would return the average of 3 numbers """
    return (num1 + num2 + num3)/3


def avgN(*args):
    # print(type(args))
    # print(args)
    total = 0
    count = 0
    for num in args:
        # total = total + num
        total += num
        # count = count + 1
        count += 1
    # print(total)
    # print(count)
    return total/count




