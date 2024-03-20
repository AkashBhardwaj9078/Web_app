import pickle 
import streamlit as st 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id="63a685626f464f0da59a62d8c3cd842f"
client_secret="ee1a8c6324b846538f3ade30ce2b86d4"

client_cred_mng=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
# sp=spotipy.Spotify(client_credential_manager=client_cred_mng)
sp=spotipy.Spotify(client_credentials_manager=client_cred_mng)


 
df=pickle.load(open("df","rb"))
similiar=pickle.load(open("similiar","rb"))   

def get_song_album(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(search_query, type="track")
    
    if results and results["tracks"]["items"]:
        album_cover_url = results["tracks"]["items"][0]["album"]["images"][0]["url"]
        return album_cover_url
    else:
        # Return a placeholder image URL if no results are found
        return "https://www.google.com/placeholder.jpg"
def  recommend(song_name):
    idx=df[df.song==song_name].index[0]
    distance=sorted(list(enumerate(similiar[idx])),reverse=True,key=lambda x:x[1])
    song_cover=[]
    song=[]
    for id in distance[1:6]:
        song.append(df.iloc[id[0]].song)
        artist=df.iloc[id[0]].artist
        print(artist)
        print(df.iloc[id[0]].song)
        
        song_cover.append(get_song_album(df.iloc[id[0]].song,df.iloc[id[0]].artist))
    return song,song_cover

    
        
st.header("Music Recommender System")


song_list=df.song
typed=st.selectbox("type or select a song from drop down",song_list)

if st.button("Show Recommnedation"):
    songs,song_cover=recommend(typed)
    col0,col1,col2,col3,col4=st.columns(5)
    with col0:
        st.text(songs[0])
        st.image(song_cover[0])
    with col1:
        st.text(songs[1])
        st.image(song_cover[1])
    with col2:
        st.text(songs[2])
        st.image(song_cover[2])
        
    with col3:
        st.text(songs[3])
        st.image(song_cover[3])
        
    with col4:
        st.text(songs[4])
        st.image(song_cover[4])
        

