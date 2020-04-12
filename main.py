import pandas as pd
from argparse import ArgumentParser
import sys
from iTunes import getFromiTunes

parser = ArgumentParser(description="This program give you the lyrics of a song and aditional information as price, album's name, album's price")

parser.add_argument("--artist",help="The artist, each word must be written with the first letter in capital letters")
parser.add_argument("--song",help="The song, each word must be written with the first letter in capital letters")

df = pd.read_csv("../data/songdata_clean.csv", encoding="latin-1")

def lyrics (artist, song):
    if (artist in list(df["artist"]))==False:
        print ("Sorry, your search did not match any result")    
    else:
        if (song in list(df["song"]))==True:
            text = list(df["text"][df["artist"]==artist][df["song"]==song].items())
            queryParams = {
                "term":f"{artist} {song}",
                "media":"music",
                "entity":"song",
                "limit": 100
            }
            iTunes = getFromiTunes("/search",queryParams)["results"][0]
            print (f"Lyrics: {text[0][1]} \nPrice: {iTunes['trackPrice']}$ \nAlbum: {iTunes['collectionName']} \nAlbum price: {iTunes['collectionPrice']}$ ")
        else:
            songs = list(df["song"][df["artist"]==artist].items())
            list_songs = sorted([e[1] for e in songs])
            print (f"We don`t find that song, please find in the list below the songs of the desired artist: \n{list_songs}")
artist = sys.argv[2]
song = sys.argv[4]

lyrics(artist, song)







