# Exchange Rate Data Retrieval and Storage Documentation
## Introduction
This code is a Python script for retrieving exchange rate data from a specified URL and storing it in a SQL database using the petl library. The data is requested using the requests library, and parsed using the json and decimal libraries. The resulting data is stored in a petl table, which is then inserted into a SQL database using the pymssql library.

## Installation
Before running the code, make sure the required Python libraries are installed. You can install them using pip. Open your terminal and enter the following commands:


```
pip install petl
pip install pymssql
pip install requests
```
## Configuration
The configuration file config.ini is used to specify various settings for the script.

The following settings are required:

startDate: A string representing the start date for the exchange rate data in YYYY-MM-DD format.
url: The URL to retrieve the exchange rate data from.
server: The name of the SQL Server to store the data in.
database: The name of the database to store the data in.
Note: make sure to replace the default settings with your own.

## Usage
To run the code, simply execute the script. The data will be retrieved from the specified URL, processed, and stored in the specified SQL database.

## Output
The resulting data is stored in a SQL database table called ExchangeRate, with the following columns:

date: The date of the exchange rate in YYYY-MM-DD format.
rate: The exchange rate for the specified date.

## Conclusion
This code retrieves exchange rate data from a specified URL and stores it in a SQL database. By modifying the configuration file, you can customize the script to retrieve data from different URLs and store it in different SQL databases.
