from selenium import webdriver
import pytest
import requests
from bs4 import BeautifulSoup

def test_browser():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    r = requests.get("https://www.millenniumhotels.com/en/hotels", headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    title = soup.find_all("div", class_="nk2-waterfall-container")
    print(len(title))
    for i in title:
        title1 = i.get("href")


