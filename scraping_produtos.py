import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_produtos_html(html, output_csv="produtos.csv"):
    soup = BeautifulSoup(html, 'html.parser')
    produtos = []
    for item in soup.select('.product-item'):
        card = item.select_one('.product-card .card-body')
        if not card:
            continue
        nome = card.select_one('.card-title').get_text(strip=True)
        preco_raw = card.select_one('.card-price').get_text(strip=True)
        preco = preco_raw.split('R$')[-1].replace('&nbsp;', '').replace(',', '.').strip()
        preco = float(preco) if preco else None
        quantidade_raw = card.select_one('[data-qtd]').get_text(strip=True)
        quantidade = int(quantidade_raw.split('Disponível:')[-1].replace('un.', '').strip())
        produtos.append({
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        })
    df = pd.DataFrame(produtos)
    df.to_csv(output_csv, index=False)
    return df

def scrape_produtos_url(url, output_csv="produtos.csv"):
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    return scrape_produtos_html(html, output_csv)