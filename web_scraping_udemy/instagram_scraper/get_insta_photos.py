from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import getpass
import os, requests, shutil

class App:
    # Must redefine 'path' to your desired photo download location 
    def __init__(self, username, password,
                path='/Users/Zach/Desktop/instaphotos'):

        self.username = username
        self.password = password
        self.error_flag = False
        self.target_username = username
        self.path = path

        # Must specify path to chromedriver executable here
        self.driver = webdriver.Chrome('/Users/Zach/Desktop/chromedriver')

        self.driver.get('https://www.instagram.com')
        sleep(1)
        if self.error_flag == False:
            self.log_in()
        if self.error_flag == False:
            self.open_target_profile()
        sleep(1)
        if self.error_flag == False:
            self.scroll_down()
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.download_images()
        self.driver.close()


    def download_images(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml') 
        images = soup.find_all('img', src=True)
        image_links = [image.get('src') for image in images]
        for i,image in enumerate(image_links):
            print("downloading image...")
            file_name = ("insta_" + str(i) + ".jpg")
            path = os.path.join(self.path,file_name)
            response = requests.get(image, stream=True)
            sleep(1)
            try:
                with open(path, 'wb') as image:
                    shutil.copyfileobj(response.raw, image)
            except Exception:
                print ("error downloading image")
                self.error_flag = True

    def scroll_down(self):
        try:
            self.num_posts = int(self.driver.find_element_by_xpath(
                        "//span[@class='_bkw5z']").text)
            if self.num_posts > 12:
                load_more = self.driver.find_element_by_link_text('Load more')
                load_more.click()
                sleep(3)
                num_scrolls = self.num_posts - 12
                num_scrolls = int(num_scrolls/12) + 2
                try:
                    for i in range(num_scrolls):
                        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                        sleep(2)
                except Exception:
                    print ("Scrolling error")
                    self.error_flag = True
        except Exception:
            print ("Scrolling error")
            self.error_flag = True

    def log_in(self):
        try: 
            log_in_button = self.driver.find_element_by_link_text('Log in')
            log_in_button.click()
            try:
                username_field = self.driver.find_element_by_xpath(
                                "//input[@placeholder='Username']")
                username_field.send_keys(self.username)
                password_field = self.driver.find_element_by_xpath(
                                "//input[@placeholder='Password']")
                password_field.send_keys(self.password)
                password_field.submit()
                sleep(3)
            except Exception:
                print ("Credentials error")
                self.error_flag = True
        except Exception:
            print ("Couldn't find login button")
            self.error_flag = True

    def open_target_profile(self):
        try:
            self.driver.get('http://www.instagram.com/' + self.username + '/')
        except Exception:
            print ("Error opening target profile")
            self.error_flag = True

if __name__ == "__main__":
    username = input("Instagram Username:")
    password = getpass.getpass("Instagram Password:") 
    app = App(username, password)
