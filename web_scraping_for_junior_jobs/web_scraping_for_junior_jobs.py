import requests
import re
from bs4 import BeautifulSoup

req_python = requests.get('https://dev.bg/company/jobs/python/')
python = req_python.text
python = python.lower()

eee = BeautifulSoup(python, 'html.parser')
print(eee.find_all(string=re.compile('junior')))

