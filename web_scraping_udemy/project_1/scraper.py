import requests
from fake_useragent import UserAgent

def get_html(url, filename):
    user_agent = UserAgent()
    page = requests.get(url, headers={'user-agent':user_agent.chrome})
    with open(filename, 'w') as file:
        file.write(page.content.decode('utf-8')) \
                if type(page.content) == bytes \
                else file.write(page.content)

def read_file(filename):
    file = open(filename)
    data = file.read()
    file.close()
    return data

def get_data(url, filename):
    get_html(url, filename)
    return (read_file(filename))
