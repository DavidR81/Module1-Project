import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://cnnespanol.cnn.com/2019/06/18/los-13-tsunamis-mas-mortales-de-la-historia/'

def page(url=URL):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    columna = soup.select('body > div.normalizecss.template--20 > article > div > div > div > div > div')
    fechas = []
    fechas1 = []
    for i in columna:
        parrafo = i.select('p')
        fechas.append(parrafo)  
    for i in range(5,18):
        fechas1.append(fechas[0][i].text.split("—"))

    d = {}
    for i in range(0,len(fechas1)):
        d[fechas1[i][0]]=fechas1[i][1]

    df = pd.DataFrame([[key, d[key]] for key in d.keys()], columns=['Fechas', 'Descripción'])
    return df
    
    

