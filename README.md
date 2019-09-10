# Module1-Project

1 - Realizamos limpieza de datos de la tabla sources.csv y waves.csv

2 - Se crea groupby con COUNTRY_FRECUENCY y COUNTRY para ver la frecuencia de Tsunamis por pais

3 - Se crea un diccionario para acotar las zonas y asi crear un grafico con las regiones costeras mas azotadas por los Tsunamis
    los datos salen de la siguiente web:  https://www.ngdc.noaa.gov/nndc/DescribeField.jsp?dataset=101650&search_look=77&field_name=tsevent_vsqp.REGION_CODE 
    
4 - Se crea otro diccionario con los codigos de las causas de los Tsunamis, con el que se crea otro groupby con CAUSES FRECUENCY y CAUSES         para sacar nuevo grafico con las causas de los Tsunamis. los datos salen de la siguiente web: https://www.ngdc.noaa.gov/nndc/DescribeField.jsp?dataset=101650&search_look=77&field_name=tsevent_vsqp.CAUSE_CODE

5 - Se realiza web scraping de la web: https://cnnespanol.cnn.com/2019/06/18/los-13-tsunamis-mas-mortales-de-la-historia/. En ella sacamos una     tabla con los 13 Tsunamis mas catastroficos de la historia

6 - Al ejecutar el Main.py sacamos por consola el dataframe que hemos creado haciendo web scraping de la web de la CNN