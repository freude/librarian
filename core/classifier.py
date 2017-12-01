from abc import ABCMeta, abstractmethod
import re
import numpy as np


class ClassifierInterface(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def predict(self, string):
        raise NotImplementedError("Should have implemented this")

    @abstractmethod
    def fit(self, data):
        raise NotImplementedError("Should have implemented this")

    @abstractmethod
    def restore(self, path):
        raise NotImplementedError("Should have implemented this")


class ClassifierNaive(ClassifierInterface):

    def __init__(self):
        self.map = None

    def predict(self, title):
        score = np.zeros(len(self.map))
        words = self._get_words_set(title)
        for j, item in enumerate(self.map):
            score[j] = len(item[1] & words)
        if np.max(score) == 0:
            return None
        else:
            return self.map[np.argmax(score)][0]

    def fit(self, sets_and_labels):
        self.map = sets_and_labels

    def restore(self, path):
        pass

    def _get_words_set(self, title):

        words = re.sub(r'[^\w|+]', ' ', title.lower())
        words = re.split(' |_|-', words)
        words = filter(None, words)
        return set(words) | set([words[j] + " " + words[j+1] for j in xrange(len(words)-1)])