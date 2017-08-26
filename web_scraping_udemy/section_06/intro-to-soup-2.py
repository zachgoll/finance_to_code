import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Create a 'fake browser'
ua = UserAgent()

# The request header is a string that allows a certain browser to be identified 
header = {'user-agent':ua.chrome}

# Get the webpage using Google Chrome fake user agent
google_page = requests.get('https://www.google.com',headers=header)
content = google_page.content

# Build our html soup
soup = BeautifulSoup(content,'lxml') # html.parser

print(soup.prettify())

