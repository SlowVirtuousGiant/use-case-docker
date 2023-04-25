import requests
import time
import psycopg2
import numpy as np
import pandas as pd
import os
import hashlib

from dotenv import load_dotenv
from datetime import datetime
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

access = os.getenv("URL")

print ("App starts")
def get_dataweather():
    url = access
    res = requests.get(url)
    json = res.json()["hourly"]
    df = pd.DataFrame(json)
    return df

usr = os.getenv("USER")
pwd = os.getenv("PASSWORD")

connection = psycopg2.connect(user = usr ,password = pwd ,host = "db",port = "5432",database = "weatherDB")
connection.autocommit = True
cursor = connection.cursor()
#SQL Code Block
sql = '''INSERT INTO weather (time,temperature_2m,apparent_temperature,precipitation)
               VALUES (%s, %s, %s, %s)'''

cursor.executemany(sql, get_dataweather().to_records(index = False))
connection.close()

print ("App end")