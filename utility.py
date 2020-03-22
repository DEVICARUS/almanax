import requests
from bs4 import BeautifulSoup

def getnsoup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    return soup