import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('Null'), 'Null')

class TestFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Null'), 'Null')

unittest.main()