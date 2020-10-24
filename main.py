import requests

if __name__ == '__main__':
    client_id = 'c46f250061634356854fa16bc47802df'
    client_secret = 'd48fde2af9724b748de5d36589b67e47'
    urlToken = 'https://accounts.spotify.com/api/token'
    body = {'grant_type': 'client_credentials', 'client_id':'c46f250061634356854fa16bc47802df', 'client_secret': 'd48fde2af9724b748de5d36589b67e47'}
    BASE_URL = 'https://api.spotify.com/v1/'
    headers = { 'Authorization':'Bearer BQBCp0wqeo9uTIiG9nWEv9KZ97J2Pbw-UtQGWeV-5lgMjYrN4RvFTuhhQi8e3vXLE8mr6y218iI5igxp6zRh47Oe1o2rhy7B2k_oMpRXCI2EpWZsweTBI5beL9JJzPMlnz9oonpHpoe-QgQBqmSpl_V7s3zzyk'}
    response = requests.post(urlToken, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
                                   })

    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json['access_token']
        headers = {
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        id_ledZeppelin = '36QJpDe2go2KgaRleHCDTp'
        id_BlackSabbath = '5M52tdBnJaKSvOpJGz8mfZ'
        id_Metallica = '2ye2Wgw4gimLv2eAKyk1NB'
        id_GrupoNiche = '1zng9JZpblpk48IPceRWs8'
        id_BodDylan = '74ASZWbe4lXaubB36ztrGX'
        id_MichaelJackson = '3fMbdgg4jU18AjLCKBhRSm'
        tabla={}

        artistas_id = ['36QJpDe2go2KgaRleHCDTp', '5M52tdBnJaKSvOpJGz8mfZ', '2ye2Wgw4gimLv2eAKyk1NB', '1zng9JZpblpk48IPceRWs8', '74ASZWbe4lXaubB36ztrGX','3fMbdgg4jU18AjLCKBhRSm' ]
        for artista_id in artistas_id:
            r = requests.get(BASE_URL + 'artists/' + artista_id + '/top-tracks?market=ES' ,
                             headers=headers,
                             params={'include_groups': 'album', 'limit': 50})
            data = requests.get(BASE_URL + 'artists/' + artista_id ,
                             headers=headers,
                             )

            artista_data=data.json()
            tracks_data=r.json()["tracks"]

            artista={}
            artista["Artist"]= {'nombre del artista': artista_data['name'],
                                'Tipo': artista_data['type'],
                                'Uri': artista_data['uri'],
                                'Popularidad': artista_data['popularity'],
                                'Cantidad de seguidores': artista_data['followers']['total']

                                }
            tracks=[]
            for track in tracks_data:
                trackAux={'Nombre del track': track['name'],
                          'Tipo de track':track['type'],
                          'artista': track["artists"][0]["name"],
                          'Album': track["album"]["name"],
                          'Popularidad': track["popularity"],
                          'Fecha de lanzamiento': track["album"]["release_date"],
                          'Id': track["id"],
                          'Uri': track["uri"],
                          'Generos': artista_data["genres"]


                          }
                tracks.append(trackAux)
            artista["tracks"] = tracks



            tabla[artista_data['name']]=artista
    print(tabla["Led Zeppelin"])












