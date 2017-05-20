import unittest
import slackmojify

class Tests(unittest.TestCase):

    def test_determine_dimensions(self):

        actual = determine_dimensions((64, 64), (64, 64))
        expected = (64, 64)
        self.assertEqual(actual, expected)

        actual = determine_dimensions((64, 64), (128, 128))
        expected = (64, 64)
        self.assertEqual(actual, expected)

        actual = determine_dimensions((64, 64), (128, 64))
        expected = (64, 32)
        self.assertEqual(actual, expected)

        actual = determine_dimensions((64, 32), (128, 64))
        expected = (64, 32)
        self.assertEqual(actual, expected)
