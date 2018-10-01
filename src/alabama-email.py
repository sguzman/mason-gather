import requests
import bs4


url = 'http://emason.alafreemasonry.org/?empf=Search'

for i in range(65, 91):
    char = chr(i)

    params = {
        'first': char,
        'search': '1'
    }

    req = requests.post(url, data=params)
    soup = bs4.BeautifulSoup(req.text, 'html.parser')

    cells = soup.findAll('td')
    for td in cells:
        a = td.contents[0]
        href = a['href']

        person_url = f'http://emason.alafreemasonry.org/{href}'
        person_req = requests.get(person_url)
        person_soup = bs4.BeautifulSoup(person_req.text, 'html.parser')

        para = person_soup.select_one('p > a > span')
        if para is None:
            print('')
        else:
            name = para.text
            print(name)


