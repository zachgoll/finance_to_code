def count_substring(string, sub_string):
    index = 0
    count = 0
    while (index != -1):
        string = string[index:]
        index = string.find(sub_string)
        if (index != -1 and index <= len(string)):
            count += 1
            index += 1
    return (count)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
