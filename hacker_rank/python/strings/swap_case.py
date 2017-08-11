def swap_case(s):
    new = []
    for letter in s:
        if letter.isupper():
            new.append(letter.lower())
        elif letter.islower():
            new.append(letter.upper())
        else:
            new.append(letter)
    return("".join(new))


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
