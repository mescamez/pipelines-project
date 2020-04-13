# PIPELINES PROJECT

In this project a program that returns information about a song based on two variables
(artist and song) was created.
To this purpose the information is obtained trough two different sources, detailed below:
CSV file and iTunes API.

## 1. CSV file:

First of all a dataset from (www.kaggle.com) was selected and analyzed. Some cleaning
tasks were needed in order to obtain a clean csv.
From the clean csv the lyric of the desired song is extracted. Extra information about the
song is obtained from another source, in this case iTunes API.

## 2. iTunes API:

In order to look for content a search field must be created. This searh field passes a fully-
qualified URL content request to the iTunes Store, parse the JavaScript Object Notation
(JSON) format returned from the search, and display the results.
The parameter keys and values to search could be defined to obtain more specific content
within the iTunes Store.

#
With this information, and given an artist and a song, the program returns the lyrics of the
song, its price in iTunes, the album it belongs to and its price. Finally the programa generates a PDF file with the complet information.
This program was made using Python3 and some of its libraries, such as:
- Argparse
- Pandas
- Json
- Requests
- FPDF
- Web browser

