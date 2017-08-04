def get_largest(array):
    largest = array[len(array) - 1]
    for i in range(len(array) - 1):
        if (array[i] > array[i+1]):
            largest = array[i]
    return largest


def rep_largest(array, largest):
    for i in range(len(array)):
        if (array[i] == largest):
            array[i] = 0
    return array


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    largest = get_largest(array)
    new_array = rep_largest(array, largest)
    print (get_largest(new_array))
