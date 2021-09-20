'''
for item in response.json()['albums']['items']:
    album_type, album_id (id), album_name(name), album_release_date(release_date), total_tracks(total_tracks)
    artist - artist_name(name), artist_type(type), artist_uid(id)
'''

{
    'albums': 
    {
        'href': 'https://api.spotify.com/v1/browse/new-releases?offset=0&limit=1',
        'items': [
            {
                'album_type': 'album',
                'artists': [
                    {
                        'external_urls': {'spotify': 'https://open.spotify.com/artist/7jVv8c5Fj3E9VhNjxT4snq'},
                        'href': 'https://api.spotify.com/v1/artists/7jVv8c5Fj3E9VhNjxT4snq',
                        'id': '7jVv8c5Fj3E9VhNjxT4snq',
                        'name': 'Lil Nas X',
                        'type': 'artist',
                        'uri': 'spotify:artist:7jVv8c5Fj3E9VhNjxT4snq'
                    }
                ],
                
                'available_markets': ['AD','ZW'],
                'external_urls': {'spotify': 'https://open.spotify.com/album/6pOiDiuDQqrmo5DbG0ZubR'},
                'href': 'https://api.spotify.com/v1/albums/6pOiDiuDQqrmo5DbG0ZubR',
                'id': '6pOiDiuDQqrmo5DbG0ZubR',
                'images': [
                    {
                        'height': 640,
                        'url': 'https://i.scdn.co/image/ab67616d0000b273be82673b5f79d9658ec0a9fd',
                        'width': 640
                    },
                    {
                        'height': 300,
                        'url': 'https://i.scdn.co/image/ab67616d00001e02be82673b5f79d9658ec0a9fd',
                        'width': 300
                    },
                    {
                        'height': 64,
                        'url': 'https://i.scdn.co/image/ab67616d00004851be82673b5f79d9658ec0a9fd',
                        'width': 64
                    }
                ],
                
                'name': 'MONTERO',
                'release_date': '2021-09-17',
                'release_date_precision': 'day',
                'total_tracks': 15,
                'type': 'album',
                'uri': 'spotify:album:6pOiDiuDQqrmo5DbG0ZubR'
            }
        ],
        'limit': 1,
        'next': 'https://api.spotify.com/v1/browse/new-releases?offset=1&limit=1',
        'offset': 0,
        'previous': None,
        'total': 100
    }
}