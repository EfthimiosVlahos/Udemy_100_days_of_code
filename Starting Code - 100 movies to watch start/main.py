import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response= requests.get(URL)
em_webpage=response.text #raw HTML text
soup=BeautifulSoup(em_webpage,"html.parser")

movies=soup.find_all(name="h3",class_="title")
updated_movies=[movie.getText() for movie in movies]
reversed_updated_movies=updated_movies[::-1]
print(reversed_updated_movies)


with open("movies.txt","w") as f:
    for movie in reversed_updated_movies:
        f.write(f"{movie}\n")



