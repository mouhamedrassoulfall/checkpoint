from bs4 import BeautifulSoup
import requests

"1"
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")


soup = BeautifulSoup(page.content, 'html.parser')


print(soup.prettify())

"2"
print("le titre du sute est : ")
for titre in soup.find_all('title'):
    print(titre.get_text())

"3"
text = []
for tag in soup.find_all('h2')[1:]:
    texth2=tag.text.strip()
    text.append(texth2)
    for item in tag.find_next_siblings('p'):
        if texth2 in item.find_previous_siblings('h2')[0].text.strip():
            text.append(item.text.strip())

"4"
urls = []
for lien in soup.find_all('a'):
    print(lien.get('href'))