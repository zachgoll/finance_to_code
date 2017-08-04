def get_largest(array):
    largest = array[0]
    for i in range(len(array)):
        if (array[i] >= largest):
            largest = array[i]
    return largest


def rep_largest(array, largest):
    while largest in array: array.remove(largest)
    return array


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    largest = get_largest(array)
    new_array = rep_largest(array, largest)
    print (get_largest(new_array))
