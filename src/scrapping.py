import requests
from bs4 import BeautifulSoup

url = 'https://www.mercadolivre.com.br/nintendo-switch-32gb-mario-kart-8-deluxe-cor-vermelho-neon-azul-neon-e-preto/p/MLB13576607#polycard_client=storefronts&wid=MLB4592661128&sid=storefronts&type=product&tracking_id=116f1f16-7350-4a7b-91ee-ce01d178bb6c&source=eshops'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

def get_atual_price():
    preco_element = soup.find('span', class_='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact')
    precoatual = preco_element.text
    return precoatual

def get_anterior_price():
    preco_anterior_element = soup.find('span', class_='andes-money-amount__fraction')
    precoanterior = preco_anterior_element.text
    return precoanterior

def get_name():
    nome_produto = soup.find('h1', class_='ui-pdp-title')
    nomeproduto = nome_produto.text
    return nomeproduto

def get_desconto():
    desconto_produto = soup.find('span', class_='andes-money-amount__discount')
    if desconto_produto:
        return desconto_produto.text
    else:
        return "Sem desconto"