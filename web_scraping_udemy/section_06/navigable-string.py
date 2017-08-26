from bs4 import BeautifulSoup

def read_file():
    file = open('tags.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

body = soup.body

# By using the '.string' method we can get the string within a tag
div_string = body.div.p.string

print (div_string)

# We can replace the text within a string

soup.body.div.p.string.replace_with("new text")
print (body.div.p.string)
