import requests
# from bs4 import BeautifulSoup
from lxml import etree

r = requests.get("https://www.mirrormedia.mg/")


print(r.text)