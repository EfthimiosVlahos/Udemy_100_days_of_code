from selenium import webdriver

#webdriver is bridege from selenium package to chrome brower.
driver=webdriver.Chrome(executable_path="/Users/Vlahonator/Downloads/chromedriver")

driver.get("https://www.python.org/")
#driver.find_element_by_id("") #selenium method that finds element with class name spicified in ()

# price= driver.find_element_by_class_name("a-offscreen") #selenium method that finds element with class name spicified in ()
# print(price.text)


# search_box = driver.find_element_by_name("q")
# print(search_box.get_attribute("placeholder"))

# logo= driver.find_element_by_class_name("python-logo")
# print(logo.size)

# doc_link= driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

# bug_link=driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a') #if all else fails,use this.
#                                             # Finds HTML elementby path structure
# print(bug_link.text)

# driver.close() #.close closes tab

upcoming_events_times=driver.find_elements_by_css_selector(".event-widget time")
print(upcoming_events_times) #list of selenium objects

for time in upcoming_events_times:
    print(time.text)

upcoming_events=driver.find_elements_by_css_selector(".event-widget li a")

# for name in upcoming_events:
#     print(name.text)

events={}

for n in range(len(upcoming_events_times)):
    events[n]= {
        "time":upcoming_events_times[n].text,
        "name":upcoming_events[n].text,
    }

print(events)

driver.quit() #.quit closes entire browser