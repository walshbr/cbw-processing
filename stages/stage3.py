# given a text file, print the TEI from it as TEI
# Note that you'll have to have installed beautiful soup and an
# xml parser before you can use them -
# $ pip3 install bs4
# $ pip3 install lxml

# load Beautiful Soup - the way we'll process the TEI
from bs4 import BeautifulSoup

# store some basic functions we'll be using.


def read_file(path_to_text):
    # take a file path and return the raw tei from it
    with open(path_to_text, 'rb') as fin:
        raw_tei = fin.read()
    return raw_tei


def turn_raw_tei_into_usable_tei(the_raw_tei):
    # given a raw_chunk_of_text read from a TEI file, turn it into usable TEI
    tei = BeautifulSoup(the_raw_tei, 'lxml')
    return tei

# at the end of the day, the first step is to get a filename
# you'll be working with.

text_path = 'repos/books/a001/a001.tei.xml'
raw_tei = read_file(text_path)
tei = turn_raw_tei_into_usable_tei(raw_tei)
print(tei)
