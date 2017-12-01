#!/usr/bin/env python
import os
import errno
import re
import shutil
from classifier import ClassifierNaive

categories =  [('Optics',
                   {'optics', 'light matter', 'matter interactions', 'photonics', 'metamaterials', 'waves', 'fiber',
                    'electromagnetic', 'classical electrodynamics'}),
               ('Classical_mechanics',
                   {'classical mechanics', 'hamiltonian mechanics', 'lagrangian mechanics'}),
               ('QFT',
                   {'quantum field', 'quantum electrodynamics'}),
               ('Quantum_mechanics',
                   {'quantum mechanics', 'quantum', 'path integration', 'path integral', 'path integrals'}),
               ('Semiconductors',
                   {'semiconductor', 'semiconductor optics', 'nanostructures'}),
               ('Solid-state',
                   {'solid state', 'surfaces', 'crystal', 'eletronic structure', 'nanoplasmonics', 'plasmonics'}),
               ('Transport',
                   {'transport', 'electronic transport', 'carrier transport'}),
               ('Magnetism',
                   {'magnetic', 'magnetism'}),
               ('Python',
                   {'python'}),
               ('C++',
                   {'c++'}),
               ('Algorithm',
                   {'algorithm', 'data structures', 'algorithms'}),
               ('Mathematical physics',
                {'mathematical physics'}),
               ('Topology',
                {'topology'}),
               ('Algebra',
                   {'algebra', 'group', 'rings'})]

extensions = (".pdf", ".djvu", ".epub")


def make_dir(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

class Library(object):

    def __init__(self, path_to_lib=None):

        make_dir(path_to_lib)

        self.path_to_lib = path_to_lib
        self.classifier = ClassifierNaive()
        self.classifier.fit(categories)
        self.shelves = dict()
        self.make_shelves_from_categories(categories)

    def process_dir(self, path):

        for filename in os.listdir(path):
            if filename.endswith(extensions):
                shelf = self.classify(os.path.basename(filename))
                self.put_on_shelf(os.path.join(path, filename), shelf)

    def classify(self, title):
        return self.classifier.predict(title)

    def put_on_shelf(self, path, shelf):
        if shelf is not None:
            path_to_move_to = os.path.join(self.path_to_lib, shelf, os.path.basename(path))
            shutil.move(path, path_to_move_to)

    def make_shelf(self, name, keywords=None):

        make_dir(os.path.join(self.path_to_lib, name))

        if name in self.shelves:
            print("The shelf $s is already created" % name)
        else:
            if keywords is not None:
                self.shelves[name] = keywords
            else:
                self.shelves[name] = {re.sub('_|-', ' ', name)}

    def make_shelves_from_categories(self, categories):

        for item in categories:
            if item[0] in self.shelves:
                print("The shelf $s is already created" % item[0])
            else:
                self.make_shelf(item[0], item[1])

    def combine_shelves(self, path):
        pass


    def del_shelf(self, path):
        pass


if __name__ == '__main__':

     lib = Library(path_to_lib='/Users/freude/Downloads/Bibliotek')
     lib.process_dir('/Users/freude/Downloads/')
