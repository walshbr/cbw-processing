import os
import shutil
import csv
from bs4 import BeautifulSoup
# notes - lots of inconsistent filenaming - xml.xml; new.xml


class TeiText(object):
    def __init__(self, fn):
        # TODO: differentiate bess from regular TEI. IE - does bess even have paragraph tags? it does not. so you'll have to get something else meaningful there.
        # TODO: dump the text of each doc into a file format that the topic modeling tool can use - entails pulling out relevant metadata
        self.fn = fn
        print(fn)
        self.raw_text = self.read_text()
        self.raw_tei = BeautifulSoup(self.raw_text, 'lxml')
        self.paragraphs = self.raw_tei.find_all('p')
        self.author = self.raw_tei.author.text
        self.paragraph_text = [paragraph.text for paragraph in self.paragraphs]
        self.combined_paragraph_text = ' '.join(self.paragraph_text)
        
    def read_text(self):
        with open(self.fn, 'rb') as fin:
            return fin.read()

class BessText(object):
    def __init__(self, fn):
        # TODO: differentiate bess from regular TEI. IE - does bess even have paragraph tags? it does not. so you'll have to get something else meaningful there.
        # TODO: dump the text of each doc into a file format that the topic modeling tool can use - entails pulling out relevant metadata
        self.fn = fn
        print(fn)
        self.raw_text = self.read_text()
        self.raw_tei = BeautifulSoup(self.raw_text, 'lxml')
        # self.paragraphs = self.raw_tei.find_all('p')
        # self.author = self.raw_tei.author.text
        # self.paragraph_text = [paragraph.text for paragraph in self.paragraphs]
        # self.combined_paragraph_text = ' '.join(self.paragraph_text)
        # 
    def read_text(self):
        with open(self.fn, 'rb') as fin:
            return fin.read()

class Corpus(object):
    def __init__(self, corpus_dir):
        self.corpus_dir = corpus_dir
        self.topic_modeling_output_dir = 'topic_modeling_input'
        self.full_tei_fns, self.bess_fns = self.all_files()
        self.bess_files = [BessText(fn) for fn in self.bess_fns]
        self.full_tei_files = [TeiText(fn) for fn in self.full_tei_fns]
        self.topic_model_dump()
        
    def all_files(self):
        """given a directory, return the filenames in it"""
        full_tei_fns = []
        bess_fns = []
        for (root, _, files) in os.walk(self.corpus_dir):
            for fn in files:
                if fn[-8:] == 'bess.xml':
                    path = os.path.join(root, fn)
                    bess_fns.append(path)
                elif fn[-4:] == '.xml':
                    path = os.path.join(root, fn)
                    full_tei_fns.append(path)
                else:
                    pass

        return full_tei_fns, bess_fns

    def clean_topic_modeling_clean(self):
        if os.path.isdir(self.topic_modeling_output_dir):
            shutil.rmtree(self.topic_modeling_output_dir)
            os.mkdir(self.topic_modeling_output_dir)
            os.mkdir(self.topic_modeling_output_dir + '/input_tei')
            os.mkdir(self.topic_modeling_output_dir + '/input_bess')
            with open(self.topic_modeling_output_dir + '/metadata.csv', 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['filenames', 'author'])
        else:
            os.mkdir(self.topic_modeling_output_dir)
            os.mkdir(self.topic_modeling_output_dir + '/output')
            os.mkdir(self.topic_modeling_output_dir + '/input_tei')
            os.mkdir(self.topic_modeling_output_dir + '/input_bess')
            with open(self.topic_modeling_output_dir + '/metadata.csv', 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['filenames', 'author'])

    def topic_model_dump(self):
        self.clean_topic_modeling_clean()
        for file in self.full_tei_files:
            with open(self.topic_modeling_output_dir + '/input_tei/' + os.path.basename(file.fn) + '.txt', 'w') as fin:
                fin.write(file.combined_paragraph_text)
            with open(self.topic_modeling_output_dir + '/metadata.csv', 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([os.path.basename(file.fn) + '.txt', file.author])
                # TODO - figure out what to write?
                # dates at least, but is that in the tei somewhere
        for file in self.bess_files:
            # TODO: find something meaningful for this
            with open(self.topic_modeling_output_dir + '/input_bess/' + os.path.basename(file.fn) + '.txt', 'w') as fin:
                fin.write('nothing for now')


def main():
    corpus_dir = 'repos/books/'
    corpus = Corpus(corpus_dir)
    
if __name__ == '__main__':
    main()