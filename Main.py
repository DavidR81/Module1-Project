import numpy as np
import pandas as pd
import re
import requests


if __name__ == '__main__':
    url = 'https://cnnespanol.cnn.com/2019/06/18/los-13-tsunamis-mas-mortales-de-la-historia/'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content

        file = open('cnnespanol.html', 'wb')
        file.write(content)
        file.close()







    