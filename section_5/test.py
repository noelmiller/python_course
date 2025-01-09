import unittest

from letters_only import is_letters_only


class TestLettersOnly(unittest.TestCase):
    def test_is_letters_only(self):
        self.assertIsNone(is_letters_only("Hello World"))
        self.assertIsNone(is_letters_only("HelloWorld"))
        self.assertRaises(ValueError, is_letters_only, "Hello World1")
        self.assertRaises(ValueError, is_letters_only, "HelloWorld1")
        self.assertRaises(ValueError, is_letters_only, "Hello World1!")
        self.assertRaises(ValueError, is_letters_only, "HelloWorld1!")
        self.assertRaises(ValueError, is_letters_only, "Hello World1!@#$%^&*()")
        self.assertRaises(ValueError, is_letters_only, "HelloWorld1!@#$%^&*()")
        self.assertRaises(ValueError, is_letters_only, "Hello World1!@#$%^&*()1234567890")
        self.assertRaises(ValueError, is_letters_only, "HelloWorld1!@#$%^&*()1234567890")
        self.assertRaises(ValueError, is_letters_only, "Hello World1!@#$%^&*()1234567890\n")
        self.assertRaises(ValueError, is_letters_only, "HelloWorld1!@#$%^&*()1234567890\n")
        self.assertRaises(ValueError, is_letters_only, "Hello World1!@#$%^&*()1234567890\n\t")
        self.assertRaises(ValueError, is_letters_only, "HelloWorld1!@#$%^&*()1234567890\n\t")

if __name__ == "__main__":
    unittest.main()
