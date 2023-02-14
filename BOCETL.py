import os
import sys
import petl
import pymssql
import configparser
import requests
import datetime
import json
import decimal

# Get data from config file
config = configparser.ConfigParser()
config.read('config.ini')

# Read Settings from configuration file
startDate=config['CONFIG']['startDate']
url=config['CONFIG']['url']
testServer=config['CONFIG']['server']
testDatabase=config['CONFIG']['database']

# Request data from URL
BOCResponse= requests.get(url+startDate)

# Initialize list of lists for data storage
BOCDates=[]
BOCRates=[]

# Check respose status and process the JSON object
if (BOCResponse.status_code==200):
    BOCRaw=json.loads(BOCResponse.text)

    # Extract observation data into column arrays
    for row in BOCRaw['observations']:
        BOCDates.append(datetime.datetime.strptime(row['d'],'%Y-%m-%d'))
        BOCRates.append(decimal.Decimal(row['FXUSDCAD']['v']))
    
    # Create petl table from colums arrays and rename the columns
    exchangRate = petl.fromcolumns([BOCDates,BOCRates],header=['date','rate'])

    # Initialize Database Connection
    dbConnection = pymssql.connect(server=testServer,database=testDatabase)

    # Populating database table
    petl.io.todb(exchangRate,dbConnection,'ExchangeRate')