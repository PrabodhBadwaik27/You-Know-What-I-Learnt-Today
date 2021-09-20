import requests as req
import datetime
import pyodbc

# Authorization using OAuth or 'Client Credentials Flow'
client_id = "YOUR-CLIENT-ID"
client_secret = "CLIENT-SECRET-KEY"

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret    
}

token = req.post('https://accounts.spotify.com/api/token', data=data)
access_token = token.json()['access_token']

header = { 'Authorization': 'Bearer {0}'.format(access_token) }

response = req.get('https://api.spotify.com/v1/browse/new-releases?limit=50', headers=header)
json_response = response.json()
new_release = json_response['albums']['items']

# Establish Db Connection
driver = "{SQL-ENGINE}"
server = ".\SQL-SERVER-NAME"
database = "SQL-DATABASE"

cnxn = pyodbc.connect('DRIVER={0};SERVER={1};DATABASE={2}'.format(driver, server, database))

album_cursor = cnxn.cursor()
artist_cursor = cnxn.cursor()

released_artists = []

for item in new_release:
    album_id = str(item['id'])
    album_name = str(item['name'])
    album_type = str(item['album_type'])
    album_release_date = datetime.datetime.strptime(item['release_date'], '%Y-%m-%d')
    album_total_tracks = item['total_tracks']
    album_total_artists = len(item['artists'])
    
    album_cursor.execute('INSERT INTO RecentlyReleasedAlbums (id, album, album_type, release_date, total_tracks, total_artists) VALUES (?, ?, ?, ?, ?, ?)', album_id, album_name, album_type, album_release_date, album_total_tracks, album_total_artists)
    

    for artist in item['artists']:
        if artist['id'] not in released_artists:
            released_artists.append(artist['id'])
            
            artist_id = str(artist['id'])
            artist_name = str(artist['name']) 
            artist_type = str(artist['type']) 
            
            artist_cursor.execute('INSERT INTO RecentlyReleasedArtists (id, artist, artist_type) VALUES (?, ?, ?)', artist_id, artist_name, artist_type)

cnxn.commit()
cnxn.close()