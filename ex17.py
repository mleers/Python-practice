import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"
r = requests.get(url)

r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")

titles = soup.find_all("h2", {"class": "story-heading"})

for item in titles:
	print(item.text.strip())

