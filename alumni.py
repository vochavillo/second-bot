from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def make_soup(url):
    resp = requests.get(url)
    txt = resp.text
    soup = BeautifulSoup(txt, 'lxml')
    return soup



main_url = 'http://www.policylink.org/about/staff?division=All'
src_url = 'http://www.policylink.org'
main_soup = make_soup(main_url)

alumni_list = []
alumni_dict = {}

for link in main_soup.select('a'):
    atts = link.attrs
    href = atts.get('href')
    if '/staff' in href:
        href_url = urljoin(src_url, href)
        staff_soup = make_soup(href_url)
        staff_bio = staff_soup.find_all('p')[0]
        staff_bio_text = staff_bio.text.lower()
        if 'stanford' in staff_bio_text:
            alumni_list.append(link.text)
            alumni_dict[link.text] = href_url
    else:
        pass

if alumni_list.amount() > 0:
    print('There are alumni working at this organization. Here are their names and links to their bios:')
    for alumni in alumni_list:
        print(alumni)
        print(alumni_dict[alumni])

else:
    print('There are no alumni working at this organization.')
