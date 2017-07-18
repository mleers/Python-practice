import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/style/2017/06/katharine-graham-washington-post-marthas-vineyard"
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html, "html.parser")

for lines in soup.find_all(class_ = "content-section"):
	for i in lines.find_all("p"):
		print(i.text)
