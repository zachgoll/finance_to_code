from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

class App:
    def __init__(self, username, password, target_username='z_gollwitzer13',
            path='/Users/Zach/Desktop/instaphotos'):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path
        self.driver = webdriver.Chrome('/Users/Zach/Desktop/chromedriver')
        self.driver.get('https://www.instagram.com')
        sleep(3)
        self.driver.close()
    def log_in(self):
        pass

if __name__ == "__main__":
    username = input("Instagram Username:")
    password = input("Instagram Password:")
    app = App(username, password)
