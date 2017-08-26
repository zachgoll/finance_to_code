from bs4 import BeautifulSoup


def read_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

body = soup.body

# Returns a LIST of children
# the .contents method only returns the direct child of the object
for child in body.contents:
    print(child if child is not None else '')

# Returns an iterator of children
for child in body.children:
    print(child if child is not None else '')

# .descendants returns all of the children
for index, child in enumerate(body.descendants):
    print (index)
    print (child if child != '\n' else '\\n')
