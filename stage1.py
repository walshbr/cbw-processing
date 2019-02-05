# given a text file, print the first 100 characters

text_path = 'repos/books/a001/a001.tei.xml'


def read_file(path_to_text):
    with open(path_to_text, 'r') as fin:
        tei = fin.read()
    return tei


text = read_file(text_path)

print(text[0:100])