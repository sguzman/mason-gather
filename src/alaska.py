import requests
import bs4

url = 'http://www.grandlodgeofalaska.org/lodges'
body = requests.get(url).text

soup = bs4.BeautifulSoup(body, "html.parser")

rows = soup.select('p.font_8 > span[style="text-decoration:underline;"] > a')

for r in rows:
    href = r['href']
    req = requests.get(href).text
    lodge_soup = bs4.BeautifulSoup(req, "html.parser")

    name_tag = lodge_soup.select_one('h2.font_2')
    name_childs = list(name_tag.children)
    name = name_tag.text
    print(name)

