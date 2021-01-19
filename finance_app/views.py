from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

finam_domen = 'https://www.finam.ru'
it_capital_domen = 'https://iticapital.ru'
finam_list = []
capital_list = []

finam = 'https://www.finam.ru/analytics/label/ezhednevnye-obzory'
it_capital = 'https://iticapital.ru/analytics/international-stock-markets/'

def get_finam():
    r = requests.get(finam).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.findAll('div', class_='ReviewNote__container--2Jl')
    for post in posts:
        title = post.find('div', class_='ReviewNote__reviewTitle--1lt').text
        url = post.find('a').get('href')
        full_url = finam_domen + url
        description = post.find('div', class_='ReviewNote__body--1IH').find('div', attrs={'class': None}).find('a').text
        data = {'title':title,
                'url':full_url,
                'description':description}
        finam_list.append(data)

def get_capital():
    r = requests.get(it_capital).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.findAll('div', attrs={'class': 'analitics-item'})
    for post in posts:
        title = post.find('div', class_='analitics-item__title').text
        url = post.find('a').get('href')
        full_url = it_capital_domen + url
        description = post.find('div', class_='analitics-item__descr').text
        data = {'title':title,
                'url':full_url,
                'description':description}
        capital_list.append(data)



get_finam()
get_capital()

def home(requests):
    context = {
        'finam_list':finam_list,
        'capital_list':capital_list,
    }
    return render(requests, "finance_app/home.html", context)