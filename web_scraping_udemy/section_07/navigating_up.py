from bs4 import BeautifulSoup


def open_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(open_file(), 'lxml')

first_p = soup.p

print (first_p)

parent_of_p = first_p.parent

print (parent_of_p.name)
