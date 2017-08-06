def get_highest(grades):
    highest = grades[0][1]
    for value in grades:
        if value[1] > highest:
            highest = value[1]
    return highest


def get_lowest(grades):
    lowest = grades[0][1]
    for value in grades:
        if value[1] < lowest:
            lowest = value[1]
    return (lowest)


def get_second_lowest(grades):
    lowest = get_lowest(grades)
    second_lowest = get_highest(grades)
    for value in grades:
        if value[1] < second_lowest and value[1] != lowest:
            second_lowest = value[1]
    return second_lowest


def get_second_lowest_grades(grades):
    names = []
    if len(grades) < 2:
        return grades[0][0]
    lowest = get_lowest(grades)
    second_lowest = get_second_lowest(grades)
    for value in grades:
        if value[1] == second_lowest:
            names.append(value[0])
    return names


if __name__ == "__main__":
    grades = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
    names = get_second_lowest_grades(grades)
    print (sorted(names))
