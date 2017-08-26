from bs4 import BeautifulSoup

def read_file():
    file = open('tags.html')
    data = file.read()
    file.close()
    return data

html_file = read_file()

# Make a 'soup' which represents an html file
soup = BeautifulSoup(html_file, 'lxml')

body = soup.body

# prints the value of the attribute 'class' but only the first instance of it
print (body.get('class'))

# we can get tags within tags (body->div)
print(body.div)

# we can get attributes within tags within tags within tags
# (body->div->p->'style')
print(body.div.p.get('style'))
