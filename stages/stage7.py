# Now we'll turn out text into tokens.

# load Beautiful Soup - the way we'll process the TEI
from bs4 import BeautifulSoup
import nltk
# store some basic functions we'll be using.


def read_file_and_get_text(path_to_text):
    # Note that here we have reorganized (programers would call it refactored)
    # Several related functions into a single one!
    # take a file path and return the raw text from it
    with open(path_to_text, 'r') as fin:
        raw_tei = fin.read()
    usable_tei = BeautifulSoup(raw_tei, 'lxml')
    return usable_tei.text

def turn_the_text_into_tokens(the_raw_text):
    return nltk.word_tokenize(the_raw_text)

# at the end of the day, the first step is to get a filename
# you'll be working with.
text_path = 'repos/books/a001/a001.tei.xml'
# get the text from that file
raw_text = read_file_and_get_text(text_path)
tokens = turn_the_text_into_tokens(raw_text)
processed_text = nltk.Text(tokens)
print('collocations: \n')
processed_text.collocations()
print('============')
print('Words similar to "she": \n')
processed_text.similar('she')
print('============')
processed_text.dispersion_plot(['man', 'woman', 'daughter', 'he', 'she', 'life', 'death'])
