import requests
import bs4
import re
import usaddress


def phone_idx(split):
    for i in range(len(split)):
        reg = re.compile("\(\d{3}\) \d{3}-\d{4}")
        if len(reg.findall(split[i])) == 1:
            return i

    return -2


def clean_mail_to(split):
    for i in range(len(split)):
        line = split[i]
        stripped = line.strip()

        if stripped.startswith('(Mail to:') or stripped.startswith('(mail to:'):
            del split[i]
            j = i
            while j < len(split):
                if split[j].strip().endswith(')'):
                    for k in range(i, j + 1):
                        del split[i]
                j += 1
            return


def clean_empty_lines(split):
    i = 0
    while i < len(split):
        line = split[i]
        if len(line.strip()) == 0:
            del split[i]
        else:
            i += 1


def scrape_width(soup, width):
    lodges = []
    for row in soup.findAll('td', width=width):
        if row is None or row.text == ' "Mainstream"':
            continue

        text = row.text
        split = text.split('\n')

        clean_mail_to(split)
        clean_empty_lines(split)

        last_idx = phone_idx(split)
        number = split[last_idx].strip()
        site = split[last_idx + 1].strip()
        addr_str = '\n'.join(split[:last_idx])

        addr = usaddress.tag(addr_str)
        lodges.append((number, site, addr))

    return lodges


def main():
    url = 'http://www.masonicinfo.com/grandlodges.htm'
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    widths = ['465', '462', '360', '461', '337']

    grand_lodges = []

    for w in widths:
        lodges = scrape_width(soup, w)
        grand_lodges.extend(lodges)

    for g in grand_lodges:
        print(g)


main()
