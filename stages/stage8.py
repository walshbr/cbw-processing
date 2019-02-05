# This is meant to be imported from the interpreter like so, from the
# same folder you're in
# >>> from stages import stage8
# >>> text_path = 'repos/books/a001/a001.tei.xml'
# >>> our_text = stage8.read_and_process_text(text_path)
# now our_text is a variable containing a processed version of the text
# that we can do things to.
# >>> our_text.collocations()
# to see other options you can do with a text, type our_text. (end with a period), and hit tab twice rather than hitting return.
# to see what an individual method can do, try the format
# help(our_text.collocations)

# load Beautiful Soup - the way we'll process the TEI
from bs4 import BeautifulSoup
import nltk
# store some basic functions we'll be using.


def read_and_process_text(path_to_text):
    # Note that here we have reorganized (programers would call it refactored)
    # Several related functions into a single one!
    # take a file path and return the raw text from it
    with open(path_to_text, 'r') as fin:
        raw_tei = fin.read()
    usable_tei = BeautifulSoup(raw_tei, 'lxml')
    tokens = nltk.word_tokenize(usable_tei.text)
    return nltk.Text(tokens)


def main():
    # at the end of the day, the first step is to get a filename
    # you'll be working with.
    text_path = 'repos/books/a001/a001.tei.xml'
    processed_text = read_and_process_text(text_path)
    processed_text.collocations()

if __name__ == '__main__':
    main()
