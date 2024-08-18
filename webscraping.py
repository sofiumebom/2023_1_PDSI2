import requests
from bs4 import BeautifulSoup
from classes import Menu

def menu_scraping():

    resposta = requests.get('https://ufu.br/')

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, 'html.parser')
        barra_esquerda = soup.find('ul', class_='menu nav')
        linhas_barra_esquerda = barra_esquerda.find_all('li')
        links_barra_esquerda = barra_esquerda.find_all('a')
        
        menu_items = []
        for linha, link in zip(linhas_barra_esquerda, links_barra_esquerda):
            menu_item = Menu(menuNav=linha.text, link="https://ufu.br" + link.get('href'))
            menu_items.append(menu_item)

        return menu_items