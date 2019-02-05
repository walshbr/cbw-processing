# This stage merely reorganizes things!

# load Beautiful Soup - the way we'll process the TEI
from bs4 import BeautifulSoup

# store some basic functions we'll be using.


def read_file_and_get_text(path_to_text):
    # Note that here we have reorganized (programers would call it refactored)
    # Several related functions into a single one!
    # take a file path and return the raw text from it
    with open(path_to_text, 'rb') as fin:
        raw_tei = fin.read()
    usable_tei = BeautifulSoup(raw_tei, 'lxml')
    return usable_tei.find('text').text


# at the end of the day, the first step is to get a filename
# you'll be working with.
text_path = 'repos/books/a001/a001.tei.xml'
# get the text from that file
raw_text = read_file_and_get_text(text_path)
print(raw_text)