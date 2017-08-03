if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # The long way to make this list using for loops
    new_list1 = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i + j + k) != n):
                    new_list1.append([i, j, k])

    print (new_list1)

    # The shortened version (list comprehension)

    new_list2 = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if ((i + j + k) != n)
    ]
    print ("")
    print (new_list2)
