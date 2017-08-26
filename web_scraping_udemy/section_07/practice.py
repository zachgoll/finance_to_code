list = ['one', 'two', 'three', 'four']

indexed_list = tuple(enumerate(list))

for x, y in indexed_list:
    print(x,y)
