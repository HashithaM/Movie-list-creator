from bs4 import BeautifulSoup
import requests
import lxml
import selenium

with open("website.html", encoding="utf-8") as file:
    content = file.read()

import lxml
soup = BeautifulSoup(content, "lxml")

soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print("\n")

print(soup)
print(soup.prettify())

print("\n")

print(soup.a)
print(soup.li)
print(soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.prettify())
print("\n")
print(soup.title)

article_text = soup.find(name="a", rel="noreferrer")
print(article_text)
# print(article_text.getText())
# print(article_text.get("href"))
article_upvote = soup.find(name="span", class_="score", id="score_36944978").getText()
# article_upvote = soup.find("/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/span/span[1]") This is xpath but it is not giving desired output
print(article_upvote)

article_texts = []
article_links = []
articles = soup.find_all(name="a", rel="noreferrer")
for article in articles:
    article_text = (article.getText())
    article_texts.append(article_text)
    article_link = (article.get("href"))
    article_links.append(article_link)

article_votes = [int(score.get_text().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_votes)

largest_number = max(article_votes)
largest_index = article_votes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# https://news.ycombinator.com/robots.txt

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text
soup = BeautifulSoup("website_html", "html.parser")

all_movies = soup.find_all(name="h3", class_="jsx-1913936986")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


import time
from bs4 import BeautifulSoup
from selenium import webdriver

# Launch a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=options)

url = "https://www.empireonline.com/movies/features/best-movies-2/"
driver.get(url)

# Wait for the page to load (you might need to adjust the waiting time)
time.sleep(5)

# Get the page source after waiting for JavaScript to load
website_html = driver.page_source

# Close the browser
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie titles
all_movies = soup.find_all(name="h3", class_="jsx-1913936986")

movie_titles = [movie.getText() for movie in all_movies]

movies = movie_titles[::-1]

print(movies)

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
