if __name__ == '__main__':

    # get first input string, turn to integer
    n = int(input())

    # split string, typecast each to integer, then put in a tuple
    integer_list = tuple(map(int, input().split()))

    # print hash of integer_list (built in function)
    print (hash(integer_list))
