import requests
import bs4

url = 'http://www.grandlodgeofalaska.org/lodges'
body = requests.get(url).text

soup = bs4.BeautifulSoup(body, "html.parser")
rows = soup.select('p.font_8 > span[style="text-decoration:underline;"] > a')


def get_name(lodge_soup):
    name_tag = lodge_soup.select_one('h2.font_2')
    return name_tag.text


def get_addr(text):
    addr_idx = text.find('ADDRESS: ')
    text = text[addr_idx + 9:]
    addr_delim = text.find('|')
    return text[:addr_delim].strip()


def get_city(text):
    idx = text.find('|')
    text = text[idx + 1:]

    comma_idx = text.find(',')
    return text[:comma_idx].strip()


def get_zip(text):
    split = text.split('AK')
    zip_raw = split[1].split('\n')
    return zip_raw[0].split()

for r in rows:
    href = r['href']
    req = requests.get(href).text
    lodge_soup = bs4.BeautifulSoup(req, "html.parser")
    name = get_name(lodge_soup)
    if name == 'Mt Verstovia Lodge No. 18':
        print('99825')
        continue

    base = lodge_soup.select_one('h2.font_2')
    text = base.parent.text

    print()
