import requests
import re
from bs4 import BeautifulSoup

page = 1
url = 'https://dev.bg/company/jobs/python'
python = requests.get(url).text.lower()
while True:
    page += 1
    url += '/page/' + str(page)

    temp = requests.get(url).text.lower()
    soup = BeautifulSoup(temp, 'html.parser')
    if len(soup.find_all(string=re.compile('404'))) > 0:
        break

    python += requests.get(url).text.lower()
    url = 'https://dev.bg/company/jobs/python'

eee = BeautifulSoup(python, 'html.parser')
python_list = eee.find_all(string=re.compile('junior'))

print(f'Python junior jobs - {len(python_list)}')