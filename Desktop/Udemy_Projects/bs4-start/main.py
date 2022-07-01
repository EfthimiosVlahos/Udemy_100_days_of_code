from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,"html.parser")

articles=soup.find_all(name="a", class_="titlelink")
article_texts=[]
article_links=[]
for article_tag in articles:
    article_text=article_tag.getText()
    article_texts.append(article_text)
    article_link=article_tag.get("href")
    article_links.append(article_link)

article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

print(article_texts) #ordered list of texts
print(article_links) #ordered list of links
print(article_upvotes) #ordered list of points
maximum= max(article_upvotes)
index= article_upvotes.index(maximum)
print(article_texts[index])
print(article_links[index])
























# with open("website.html") as file:
#     contents=file.read()
#
# soup=BeautifulSoup(contents,'html.parser') #reads html file and converts into a python object, which is soup
# print(soup.title) #prints out whole tag
# print(soup.title.name) #prints tyoe of tage
# print(soup.title.string) #prints out string inside tag
# print(soup) #prints out whole html website/file
# print(soup.prettify()) #same thing as above but makes it more neat and indented correctly
# print(soup.a) #prints out first anchor tag it finds in website
# all_anchor_tags=soup.find_all(name="a") #returns list of all anchor tags (links). Searches by tag name.
# print(all_anchor_tags)
# for tag in all_anchor_tags:
    # print(tag.getText()) #gets text inside tags
    # print(tag.get("href")) #gets href (links) inside tags

# heading=soup.find(name="h1", id="name") #finds one element with specific name and id
# print(heading)

# section_heading=soup.find(name="h3",class_="heading") #finds one element with specific name and class
# company_url=soup.select_one(selector="p a") #uses CSS to find an <a> tag that is sitting inside a <p> tag. String
#                                             # is CSS selctor. select_one finds first element with specified arguments
# print(company_url)


