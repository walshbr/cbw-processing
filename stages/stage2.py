# given a text file, print the first 100 text characters of it

def read_file(path_to_text):
    # take a file path and return the raw tei from it
    with open(path_to_text, 'rb') as fin:
        raw_tei = fin.read()
    return raw_tei


text_path = 'repos/books/a001/a001.tei.xml'

raw_tei = read_file(text_path)
print(raw_tei)
