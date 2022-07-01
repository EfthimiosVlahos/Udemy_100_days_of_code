from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL="vlahos89@gmail.com"
PASSWORD="Timmy123!"
PHONE="5166060942"

driver=webdriver.Chrome(executable_path="/Users/Vlahonator/Downloads/chromedriver")
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&f_JT=I&f_WT=2%2C1&geoId=105080838&keywords=data"
           "%20analyst&location=New%20York%2C%20United%20States&sortBy=R")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

email=driver.find_element_by_id("username")
email.send_keys(EMAIL)

password=driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()



