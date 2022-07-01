from selenium import webdriver
from selenium.webdriver.common.keys import Keys #the class Keys contains a bunch of constants

driver=webdriver.Chrome(executable_path="/Users/Vlahonator/Downloads/chromedriver")
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name=driver.find_element_by_name("fName")
first_name.send_keys("Timmy")

last_name=driver.find_element_by_name("lName")
last_name.send_keys("Vlahos")

email=driver.find_element_by_name("email")
email.send_keys("pooki@thneed.com")

sign_button=driver.find_element_by_css_selector("form button")
sign_button.click()