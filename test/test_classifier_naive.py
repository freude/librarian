import unittest
from core.classifier import ClassifierNaive


class TestClassifierNaive(unittest.TestCase):

    def setUp(self):

        categories = [('C++', {'c++'}),
                      ('Algorithm', {'algorithm', 'data structures', 'algorithms'}),
                      ('Algebra', {'algebra', 'group', 'rings'})]

        self.cl = ClassifierNaive()
        self.cl.fit(categories)
        self.test_string = "(Core Series) J Chun-Core Python C++ Programming-Prentice Hall (2012)"
        self.test_result = {'core', 'series', 'j', 'chun', 'core', 'python', 'c++', 'programming', 'prentice',
                            'hall', '2012',  'core series', 'series j', 'j chun', 'chun core', 'core python',
                            'python c++', 'c++ programming', 'programming prentice', 'prentice hall', 'hall 2012'}
        self.test_string1 = "(Core Series) J Chun-Core C++ Programming-Prentice Hall (2012)"
        self.test_result1 = 'C++'

    def test_get_words_set(self):
        self.assertSetEqual(self.cl._get_words_set(self.test_string), self.test_result)

    def test_predict(self):
        self.assertEqual(self.cl.predict(self.test_string1), self.test_result1)

if __name__ == '__main__':

    unittest.main()