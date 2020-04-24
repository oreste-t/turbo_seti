import unittest
from turbo_seti.findoppler import file_writers


class GeneralWriterTest(unittest.TestCase):
    def testOpenClose(self):
        """
        Test to confirm my suspicion that GeneralWriter's open function actually closed the file immediately after
        opening it. This was due to the use of the 'with' keyword.
        Whether intentional or not, open did not leave the GeneralWriter with an opened file object. It simply changed
        the file mode, then closed the file.
        """
        alpha = file_writers.GeneralWriter("test.txt", "a")
        alpha.open()
        self.assertEqual(True, alpha.is_open())

        self.assertEqual("a", alpha.filehandle.mode)
        alpha.open("r")
        self.assertEqual("r", alpha.filehandle.mode)
        alpha.close()
        self.assertEqual(False, alpha.is_open())

    def testWriteable(self):
        """
        Due to how open was written, writeable would always be false, since it also checked whether a file is open.
        It has since been fixed.
        """
        bravo = file_writers.GeneralWriter("test.txt", "a")
        self.assertEqual(False, bravo.writable())  # False because file has not yet been opened.
        bravo.open("w")
        self.assertEqual(True, bravo.writable())
        bravo.close()

    def testClose(self):
        charlie = file_writers.GeneralWriter("test.txt", "r")
        charlie.close()
        self.assertEqual(False, charlie.writable())
        self.assertEqual(False, charlie.is_open())
        charlie.close()

    def testWrite(self):
        delta = file_writers.GeneralWriter("test.txt", "w")
        origStr = "This is some text."
        delta.write(origStr)
        delta.open("r")
        str = delta.filehandle.read()
        self.assertEqual(str, origStr)
        delta.write(" This should get appended even if I didn't change mode.")
        delta.open("r")
        finalStr = delta.filehandle.read()
        correctStr = "This is some text. This should get appended even if I didn't change mode."
        self.assertEqual(correctStr, finalStr)
        delta.close()

    def testStartOver(self):
        echo = file_writers.GeneralWriter("test.txt", "w")
        origStr = "I will be wiped."
        echo.write(origStr)
        echo.open("r")
        str = echo.filehandle.read()
        self.assertEqual(origStr, str)
        echo.start_over()
        echo.open("r")
        wipedStr = echo.filehandle.read()
        self.assertEqual("", wipedStr)


if __name__ == '__main__':
    unittest.main()
