from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN=150
PROMISED_UP=10
CHRROME_DRIVER_PATH="/Users/Vlahonator/Downloads/chromedriver"
TWITTER_EMAIL="vlahos89@gmail.com"
TWITTER_PASSWORD="Timmy123!"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="/Users/Vlahonator/Downloads/chromedriver")
        self.down= 0
        self.up= 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        self.up=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text




    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")

        time.sleep(2)
        email = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        password = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')

        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

