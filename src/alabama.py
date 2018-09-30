import requests
import bs4


def get_lodge_num(soup):
    a_href = soup.select_one('a[href^="lodges2"]')
    if a_href is None:
        return None

    return a_href['href']


def get_lodge(path):
    url = f'http://www.alafreemasonry.org/bluelodges/{path}'
    req = requests.get(url)
    text = req.text
    soup = bs4.BeautifulSoup(text, "html.parser")

    return soup


def get_lodge_name(soup):
    name = soup.find('td', class_='pagetitle')
    text = name.text
    return text[:text.find('#') - 1].strip()


def get_init_list():
    url = 'http://www.alafreemasonry.org/bluelodges/lodges1.php?list=ac'
    req = requests.get(url)
    text = req.text
    soup = bs4.BeautifulSoup(text, "html.parser")

    rows = soup.findAll('tr')[1:]

    nums = set()
    for r in rows:
        num = get_lodge_num(r)

        if num is not None:
            nums.add(num)

    nums = list(nums)
    nums.sort()
    return nums


def get_lodge_city(soup):
    return soup.find('h3').text.lstrip('City - ')


def main():
    rows = get_init_list()

    for p in rows:
        soup = get_lodge(p)

        name = get_lodge_name(soup)
        h3 = get_lodge_city(soup)

        rows_again = soup.findAll('h3')
        master = ''
        master_number = ''

        secretary = ''
        secretary_number = ''

        for rr in rows_again:
            parent = rr.parent
            if rr.text == 'Worshipful Master':
                master = parent.text.lstrip('Worshipful Master')
                master_idx = 0
                for i in range(len(master)):
                    if master[i].isdigit():
                        master_idx = i
                        break

                master_number = master[master_idx:]
                master = master[:master_idx]


            if rr.text == 'Secretary':
                secretary = parent.text.lstrip('Secretary')
                secretary_idx = 0
                for i in range(len(secretary)):
                    if secretary[i].isdigit():
                        secretary_idx = i
                        break

                secretary_number = secretary[secretary_idx:]
                secretary = secretary[:secretary_idx]

        print(name, h3, 'Alabama', master, master_number, secretary, secretary_number)


main()
