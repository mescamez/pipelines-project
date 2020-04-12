import pandas as pd

df = pd.read_csv("../data/songdata_clean.csv", encoding="latin-1")

def lyrics (artist, song):
    if (song in list(df["song"]))==True:
        text = list(df["text"][df["artist"]==artist][df["song"]==song].items())
        queryParams = {
            "term":f"{artist} {song}",
            "media":"music",
            "entity":"song",
            "limit": 100
        }
        iTunes = getFromiTunes("/search",queryParams)["results"][0]
        print (f"Lyrics: {text[0][1]} \nPrice: {iTunes['trackPrice']}$ \nAlbum: {iTunes['collectionName']} \nAlbum price: {iTunes['collectionPrice']}$")
    else:
        if (artist in list (df["artist"]))==False:
            print("Sorry, that artist isn`t in our data base")
        else:
            songs = list(df["song"][df["artist"]==artist].items())
            list_songs = sorted([e[1] for e in songs])
            print (f"We don`t find any song with that song, please find in the list below the songs of the desired artist: \n{list_songs}")