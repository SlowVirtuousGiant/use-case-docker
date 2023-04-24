import requests
import time
import psycopg2
import numpy as np
import pandas as pd

from datetime import datetime
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

print ("App starts")
def get_dataweather():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=48.85&longitude=2.35&start_date=2023-01-01&end_date=2023-01-31&hourly=temperature_2m,apparent_temperature,precipitation"
    res = requests.get(url)
    json = res.json()["hourly"]
    df = pd.DataFrame(json)
    #df['time'] = pd.to_datetime(df['time']).apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    #df['temperature_2m'] = df['temperature_2m'].astype(float)
    #df['apparent_temperature'] = df['apparent_temperature'].astype(float)
    #df['precipitation'] = df['precipitation'].astype(float)
    return df


connection = psycopg2.connect(user = "admin",password = "admin",host = "db",port = "5432",database = "weatherDB")
connection.autocommit = True
cursor = connection.cursor()
#SQL Code Block
sql = '''INSERT INTO weather (time,temperature_2m,apparent_temperature,precipitation)
               VALUES (%s, %s, %s, %s)'''

cursor.executemany(sql, get_dataweather().to_records(index = False))
connection.close()

print ("App end")