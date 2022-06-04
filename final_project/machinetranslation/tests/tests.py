import unittest

from translator import french_to_english, english_to_french

class TestMyModule(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual(None, "something")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertNotEqual(None, "something")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()

