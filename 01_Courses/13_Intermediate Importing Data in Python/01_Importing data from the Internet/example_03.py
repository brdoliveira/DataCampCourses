from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/~guido/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)

print(soup.prettify())
print("*" * 60)
print(soup.title)
print("*" * 60)
print(soup.get_text())
print("*" * 60)

for link in soup.find_all('a'):
    print(link.get('href'))