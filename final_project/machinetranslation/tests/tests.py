import unittest
from machinetranslation.translator import french_to_english, english_to_french


class TranslationTests(unittest.TestCase):
    def test_frenchToEnglish(self):
        french_text = "Bonjour"
        expected_translation = "Hello"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_translation)

        # Testing with a different French text
        french_text_2 = "Au revoir"
        expected_translation_2 = "Goodbye"
        translated_text_2 = french_to_english(french_text_2)
        self.assertNotEqual(translated_text_2, expected_translation_2)

    def test_englishToFrench(self):
        english_text = "Hello"
        expected_translation = "Bonjour"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_translation)

        # Testing with a different English text
        english_text_2 = "Goodbye"
        expected_translation_2 = "Au revoir"
        translated_text_2 = english_to_french(english_text_2)
        self.assertNotEqual(translated_text_2, expected_translation_2)

if __name__ == '__main__':
    unittest.main()
