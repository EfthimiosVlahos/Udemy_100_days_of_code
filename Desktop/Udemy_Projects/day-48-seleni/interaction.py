from selenium import webdriver
from selenium.webdriver.common.keys import Keys #the class Keys contains a bunch of constants

#Chrome driver is bridege from selenium package to chrome brower.
driver=webdriver.Chrome(executable_path="/Users/Vlahonator/Downloads/chromedriver")

driver.get("https://en.wikipedia.org/wiki/Main_Page")

#finds element, in this case link, on website via css selector arguments
article_count=driver.find_element_by_css_selector("#articlecount a")
#clicks on element on webpage automatically
# article_count.click()

#finds element/link whos text is inside the parenthesis
# all_portals=driver.find_element_by_link_text("All portals")
# allportals.click()

search=driver.find_element_by_name("search")
#sends keys from the keyboard that u want to send to particular element
search.send_keys("Python")
search.send_keys(Keys.ENTER) #presses enter on search bar on website

# driver.quit()