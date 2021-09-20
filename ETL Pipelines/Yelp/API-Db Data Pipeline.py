'''
Steps
0. Database Design
1. Extract
    1.1 Modify header
    1.2 GET list of restaurants in 'Paris'
    1.3 List 'id' of all restaurants
    1.4 GET metadata of selected restaurants using 'id' in list
2. Transform - Datatypes conversion
3. Load
    3.1 Establish connection with Db
    3.2 Load data using connection object
    3.3 Commit and close connection
'''

import pyodbc
import requests as req

print("Executing...")

api_key = "YOUR-API-KEY"
headers = {'Authorization': 'BEARER {key}'.format(key=api_key)}
bizlist = []

city = 'Paris'
bizlist_url = 'https://api.yelp.com/v3/businesses/search?location='
get_bizlist = req.get(bizlist_url + city, headers=headers)

json_bizlist = get_bizlist.json()

print("Extracting restaurant list...")
for biz in json_bizlist['businesses']:
    bizlist.append(biz['id'])
    

print("Establishing Db connection...")
# Database Configurations
driver = "{SQL-ENGINE}"
server = ".\SQL-SERVER-NAME"
database = "SQL-DATABASE"
load_query = 'INSERT INTO Restaurant (id, rname, is_closed, phone, reviews, rating, zipcode, city, country, latitude, longitude, currency) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

# Establish a Connection with Database
cnxn_string = 'DRIVER={0};SERVER={1};DATABASE={2}'.format(driver, server, database)

biz_url = 'https://api.yelp.com/v3/businesses/{id}'

cnxn = pyodbc.connect(cnxn_string)
print("Database connection established successfully!\nTransforming and loading metadata...")

cursor = cnxn.cursor()

# Data Transformation
for biz in bizlist:
    json_bizmeta = req.get(biz_url.format(id=biz), headers=headers).json()
    
    biz_id = str(json_bizmeta['id'])
    biz_name = str(json_bizmeta['name'])
    biz_is_closed = bool(json_bizmeta['is_closed'])
    biz_phone = int(json_bizmeta['phone'])
    biz_reviews = int(json_bizmeta['review_count'])
    biz_rating = float(json_bizmeta['rating'])
    
    location = json_bizmeta['location']
    biz_zip = int(location['zip_code'])
    biz_city = str(location['city'])
    biz_country = str(location['country'])
    
    coordinates = json_bizmeta['coordinates']
    co_lat = float(coordinates['latitude'])
    co_lon = float(coordinates['longitude'])
    
    try:
        biz_price = str(json_bizmeta['price'])
    except:
        biz_price = ' '

    cursor.execute(load_query, biz_id, biz_name, biz_is_closed, biz_phone, biz_reviews, biz_rating, biz_zip, biz_city, biz_country, co_lat, co_lon, biz_price)

print("Loading completed successfully! Disconnecting link with Db..")

cnxn.commit()
cnxn.close()
print("Data pipeline is paused. Execution completed.")

    
    