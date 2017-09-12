import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"
r = requests.get(url)

r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")

titles = soup.find_all("h2", {"class": "story-heading"})

filename = str(input("What name/ format do you want for NYT headlines?: "))

with open(filename, "w") as open_file:
	for item in titles:
        	open_file.write(item.text.strip())




