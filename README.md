# PIPELINES PROJECT

In this project we create a program that  returns information about a song based on two variables: artist and song.
For that, we obtained the information from two sources that we detail below:
## 1. CSV file:
Firstable we selected a dataset from (www.kaggle.com) and we analyze it. It was necessary to do some cleanings tasks and then we created our clean csv. From that document we can extract the lyrics of a song and we complete the information with other source.
## 2. iTunes API:
To search for content, we must create a search field that passes a fully-qualified URL content request to the iTunes Store, parse the JavaScript Object Notation (JSON) format returned from the search, and display the results. We can define the parameter keys and values to search for more specific content within the iTunes Store.

#
With this information, and given an artist and a song, the program returns the lyrics of the song, the price of the song in iTunes, the album it belongs to and the price of the album. Then the programa generate a PDF file with that information.

This program was made using Python3 and some of its libraries such as:
- Argparse
- Pandas
- Json
- Requests
- FPDF
- Web browser

