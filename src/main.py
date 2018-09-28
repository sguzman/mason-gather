import requests
import bs4
import usaddress

url = 'http://www.masonicinfo.com/grandlodges.htm'
req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, "html.parser")
for row in soup.findAll('td', width="465"):
    if row is None:
        continue

    text = row.text
    split = text.split('\n')
    if len(split) < 3:
        continue

    site = split[-1]
    number = split[-2]

    addr_str = ','.join(split[:-3])

    addr = usaddress.tag(addr_str)
    print(number, site, addr)




