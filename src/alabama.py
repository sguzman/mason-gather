import requests
import bs4

url = 'http://www.alafreemasonry.org/bluelodges/lodges1.php?list=ac'
req = requests.get(url)
text = req.text

soup = bs4.BeautifulSoup(text, "html.parser")

rows = soup.findAll('tr')[1:]


def get_lodge_num(soup):
    a_href = soup.select_one('a[href^="lodges2"]')
    if a_href is None:
        return None

    return a_href['href']


def get_lodge(path):
    url = f'http://www.alafreemasonry.org/bluelodges/{path}'



def main():
    nums = set()
    for r in rows:
        num = get_lodge_num(r)

        if num is not None:
            nums.add(num)

    nums = list(nums).sort()
