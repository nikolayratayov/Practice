import requests
import re
from bs4 import BeautifulSoup

# Junior jobs with python
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


# Junior jobs with java
page = 1
url = 'https://dev.bg/company/jobs/java'
java = requests.get(url).text.lower()
while True:
    page += 1
    url += '/page/' + str(page)

    temp = requests.get(url).text.lower()
    soup = BeautifulSoup(temp, 'html.parser')
    if len(soup.find_all(string=re.compile('404'))) > 0:
        break

    java += requests.get(url).text.lower()
    url = 'https://dev.bg/company/jobs/java'

eee = BeautifulSoup(java, 'html.parser')
java_list = eee.find_all(string=re.compile('junior'))

print(f'Java junior jobs - {len(java_list)}')


# Junior jobs with javascript
page = 1
url = 'https://dev.bg/company/jobs/javascript'
javascript = requests.get(url).text.lower()
while True:
    page += 1
    url += '/page/' + str(page)

    temp = requests.get(url).text.lower()
    soup = BeautifulSoup(temp, 'html.parser')
    if len(soup.find_all(string=re.compile('404'))) > 0:
        break

    javascript += requests.get(url).text.lower()
    url = 'https://dev.bg/company/jobs/javascript'

eee = BeautifulSoup(javascript, 'html.parser')
javascript_list = eee.find_all(string=re.compile('junior'))

print(f'Javascript junior jobs - {len(javascript_list)}')
