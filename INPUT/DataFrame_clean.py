import numpy as np
import pandas as pd
import re
import requests


#Importamos csv sources con data de tsunamis

tsunami_Sources = pd.read_csv('../input/sources.csv', sep=",", header=0, index_col=0)

#Eliminamos las columnas que nos aportan datos 

tsunami_Sources = tsunami_Sources.drop(['HOUR','MINUTE','CAUSE','FOCAL_DEPTH','STATE/PROVINCE','MAGNITUDE_ABE',
                                        'MAGNITUDE_IIDA','WARNING_STATUS','MISSING','MISSING_ESTIMATE','INJURIES',
                                        'INJURY_ESTIMATE','DAMAGE_MILLIONS_DOLLARS','HOUSES_DAMAGED','HOUSE_DAMAGE_ESTIMATE',
                                        'HOUSES_DESTROYED','HOUSE_DAMAGE_ESTIMATE','ALL_MISSING','MISSING_TOTAL','ALL_INJURIES',
                                        'INJURY_TOTAL','ALL_HOUSES_DAMAGED','HOUSE_DAMAGE_TOTAL','ALL_HOUSES_DESTROYED',
                                        'HOUSE_DESTRUCTION_TOTAL'], 1)

#Se crea groupby con COUNTRY_FRECUENCY y COUNTRY para ver la frecuencia de Tsunamis por pais

tsunami_Sources['COUNTRY_FRECUENCY'] = tsunami_Sources.groupby(tsunami_Sources.COUNTRY)['COUNTRY'].transform('count')
tsunami_Sources.COUNTRY[tsunami_Sources.COUNTRY_FRECUENCY > 50].value_counts().plot(kind='bar', legend=False, figsize=(12,5), 
                                            title="Frecuencia de tsunamis por paises > 50", fontsize=12, alpha=0.5); 



#Se crea nuevo groupby 

#tsunami_Sources.COUNTRY[(tsunami_Sources.YEAR >= 1950) & (tsunami_Sources.COUNTRY_FRECUENCY > 50)].value_counts().plot(kind='bar',
#               legend=False, figsize=(12,5), title="Tsunamis frecuency by countries (Year >= 2000)", fontsize=12, alpha=0.5); 

#Se crea un diccionario para acotar las zonas y asi crear un grafico con las regiones costeras mas azotadas por los Tsunamis

regions = {77:'Costa Oeste de Africa', 78:'Central Africa', 73:'Northeast Atlantic Ocean', 72:'Northwest Atlantic Ocean',
           70:'Southeast Atlantic Ocean', 71:'Southwest Atlantic Ocean', 75:'E. Coast USA and Canada, St Pierre and Miquelon',
           76:'Gulf of Mexico', 74:'Caribbean Sea', 40:'Black Sea and Caspian Sea', 50:'Mediterranean Sea', 30:'Red Sea and Persian Gulf',
           60:'Indian Ocean (including west coast of Australia)', 87:'Alaska (including Aleutian Islands)',
           84:'China, North and South Korea, Philippines, Taiwan', 81:'E. Coast Australia, New Zealand, South Pacific Is.', 
           80:'Hawaii, Johnston Atoll, Midway I', 83:'E. Indonesia (Pacific Ocean) and Malaysia', 
           82:'New Caledonia, New Guinea, Solomon Is., Vanuatu', 86:'Kamchatka and Kuril Islands', 85:'Japan',
           88:'West Coast of North and Central America', 89:'West Coast of South America'}

tsunami_Sources['REGIONS'] = tsunami_Sources['REGION_CODE'].map(regions)

#Group by Regions
tsunami_Sources['REGIONS_FRECUENCY'] = tsunami_Sources.groupby(tsunami_Sources.REGIONS)['REGIONS'].transform('count')
#Frecuency by Regions
tsunami_Sources.REGIONS[tsunami_Sources.REGIONS_FRECUENCY > 100].value_counts().plot(kind='pie', legend=False, figsize=(8,7),
                                                            title="Tsunamis por Regiones", autopct='%.1f%%') 


#Se crea otro diccionario con los codigos de las causas de los Tsunamis, 
# con el que se crea otro groupby con CAUSES FRECUENCY y CAUSES para sacar nuevo grafico con las causas de los Tsunamis

causes = {0:'Unknown', 1:'Earthquake', 2:'Questionable Earthquake', 3:'Earthquake and Landslide', 4:'Volcano and Earthquake',
          5:'Volcano, Earthquake, and Landslide', 6:'Volcano', 7:'Volcano and Landslide', 8:'Landslide', 9:'Meteorological',
          10:'Explosion', 11:'Astronomical Tide'}


tsunami_Sources['CAUSES_FRECUENCY'] = tsunami_Sources.groupby(tsunami_Sources.CAUSES)['CAUSES'].transform('count')#grupo por causas
tsunami_Sources.CAUSES[tsunami_Sources.CAUSES_FRECUENCY >= 50].value_counts().plot(kind='pie', legend=False, figsize=(8,7),
                                                            title="Causas de los Tsunamis", autopct='%.1f%%'); # causa del tsunami
                                            
#importamos el segundo daframe

tsunami = pd.read_csv('../input/waves.csv', sep=",", header=0, index_col=0)

#Eliminamos las columnas que nos aportan datos

tsunami = tsunami.drop(['TRAVEL_TIME_HOURS','TRAVEL_TIME_MINUTES','VALIDITY','FIRST_MOTION','INJURIES',
                       'INJURY_ESTIMATE','FATALITIES','FATALITY_ESTIMATE','DAMAGE_MILLIONS_DOLLARS',
                       'DAMAGE_ESTIMATE','HOUSES_DAMAGED','HOUSE_DAMAGE_ESTIMATE','HOUSES_DESTROYED',
                       'HOUSE_DAMAGE_ESTIMATE'], 1)

#hacemos un merge de las columnas comunes con la tabla sources

tsunami_stat = pd.merge(tsunami_Sources, tsunami, on=['YEAR','MONTH','DAY','REGION_CODE','COUNTRY','LOCATION','LATITUDE',
                                                      'LONGITUDE','MAXIMUM_HEIGHT','HOUSE_DESTRUCTION_ESTIMATE'])

                                                      







    