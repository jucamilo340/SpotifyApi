import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from datetime import timezone
from datetime import datetime
import socket


if __name__ == '__main__':
    client_id = 'c46f250061634356854fa16bc47802df'
    client_secret = 'd48fde2af9724b748de5d36589b67e47'
    urlToken = 'https://accounts.spotify.com/api/token'
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
        print(headers)
        id_ledZeppelin = '36QJpDe2go2KgaRleHCDTp'
        id_BlackSabbath = '5M52tdBnJaKSvOpJGz8mfZ'
        id_Metallica = '2ye2Wgw4gimLv2eAKyk1NB'
        id_GrupoNiche = '1zng9JZpblpk48IPceRWs8'
        id_BodDylan = '74ASZWbe4lXaubB36ztrGX'
        id_MichaelJackson = '3fMbdgg4jU18AjLCKBhRSm'

        #DATOS DE LOS ARTISTAS
        nombres = []
        Tipo = []
        Uri=[]
        Popularidad = []
        seguidores = []
        carga=[]
        Origen=[]

        #DATOS DE LOS TRACKS
        nombresTracks=[]
        TipoTrack=[]
        PopularidadTracks=[]
        Artistas=[]
        Fecha=[]
        id=[]
        urlTracks=[]
        Album=[]
        Generos = []
        cargaTrack=[]
        OrigenTracks=[]




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

            nombres.append(artista_data["name"])
            Tipo.append(artista_data['type'])
            Uri.append(artista_data['uri'])
            Popularidad.append(artista_data['popularity'])
            seguidores.append(artista_data['followers']['total'])
            now = datetime.now()
            carga.append(now.replace(tzinfo=timezone.utc).timestamp())
            Origen.append(artista_data['href'])


            tracks=[]
            for track in tracks_data:

                OrigenTracks.append(track['href'])
                nombresTracks.append(track['name'])
                TipoTrack.append(track['type'])
                Artistas.append(track["artists"][0]["name"])
                Album.append(track["album"]["name"])
                PopularidadTracks.append(track["popularity"])
                Fecha.append(track["album"]["release_date"])
                id.append(track["id"])
                Generos.append(artista_data["genres"])
                urlTracks.append(track["uri"])
                now = datetime.now()
                cargaTrack.append(now.replace(tzinfo=timezone.utc).timestamp())
                OrigenTracks.append(track['href'])



    d = {'nombre': nombres,'Tipo':Tipo,'Uri':Uri,'popularidad':Popularidad,'seguidores':seguidores,'FechaCarga':carga,'Origen':Origen}
    b = {'ID':id,'nombre': nombresTracks, 'Tipo': TipoTrack, 'Uri': urlTracks, 'popularidad': PopularidadTracks,'artista':Artistas,'FechaDeLanzamiento':Fecha,'Generos':Generos
        ,'FechaCarga':cargaTrack}
    artistas = pd.DataFrame(data=d)
    Tracks = pd.DataFrame(data=b)
    engine = create_engine('postgresql://postgres:root@127.0.0.1:5432/spotifybase')
    artistas.to_sql('Artist', con=engine, index=False)
    Tracks.to_sql('Tracks', con=engine, index=False)
    print(artistas)
    print(Tracks)



















