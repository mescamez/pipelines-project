from argparse import ArgumentParser
from songdata import lyrics
from PDF import createPDF


def parse():
    parser = ArgumentParser(description="This program give you the lyrics of a song and aditional information as price, album's name, album's price")
    parser.add_argument("--artist",help="The artist, each word must be written with the first letter in capital letters")
    parser.add_argument("--song",help="The song, each word must be written with the first letter in capital letters")
    return parser.parse_args()

def main():
    args = parse()
    artist = args.artist
    song = args.song
    infoSong = (lyrics(artist, song))
    createPDF(infoSong)


if __name__ == '__main__':
    main()
"""

import sys
artist = sys.argv[2]
song = sys.argv[4]

lyrics(artist, song)

"""