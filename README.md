# Movie-list-creator
This code creates a movie list by web scraping
This Python script demonstrates web scraping using BeautifulSoup and Selenium to extract data from HTML web pages. Let's break down what each part of the code does:

Using BeautifulSoup with local HTML file:

It opens a local HTML file named "website.html" and reads its content.
BeautifulSoup is used to parse the HTML content.
Various operations like printing the title, accessing specific tags, finding all anchor tags, selecting elements by class or ID, and extracting information are performed using BeautifulSoup methods.
Using BeautifulSoup with an online website (Hacker News):

Requests library fetches the HTML content of the Hacker News website.
BeautifulSoup parses the HTML content.
It extracts information such as the title, article texts, links, and votes of articles on Hacker News.
Writing data to a file:

It writes the article titles extracted from Hacker News to a file named "movies.txt".
Using Selenium with Chrome WebDriver:

It launches a headless Chrome browser using Selenium to access the Empire Online website.
After the page is loaded, it waits for a specified amount of time (5 seconds in this case) for JavaScript content to load.
It retrieves the page source after JavaScript execution.
BeautifulSoup is then used to parse this page source.
It finds and extracts movie titles from the parsed HTML.
It writes the movie titles to a file named "movies.txt".
Overall, the script demonstrates how to use BeautifulSoup for parsing HTML content, fetching data from websites, and extracting specific information. Additionally, it showcases the usage of Selenium for automating interactions with websites that rely heavily on JavaScript for content rendering.






