import unittest
import turbo_seti.findoppler.findopp as findopp


class bitrevTests(unittest.TestCase):
    def testn1(self):
        """
        input of
            inval       int 1 = binary 0001
            nbits       1
        Should yield '1' because the number is considered to have a length of 1 bit, so only the rightmost bit
        is flipped, yielding no change.
        """
        alpha = findopp.bitrev(1, 1)
        self.assertEqual(alpha, 1)

    def testn2(self):
        """
        input of
            inval       int 1 = binary 0001
            nbits       2
        Should yield int 2 = binary 0010 because the rightmost 2 bits swap places
        """
        bravo = findopp.bitrev(1, 2)
        self.assertEqual(bravo, 2)

    def testVaried(self):
        """
        input of
            inval       int 37 = binary 0010 0101
            nbits       1
        Should yield int 1 = binary 0001 because the number is considered to have a length of 1 bit, meaning that the
        rightmost bit is flipped and the rest of the bits are truncated
        """
        charlie = findopp.bitrev(37, 1)
        self.assertEqual(charlie, 1)

        """
        input of
            inval       int 37 = binary 0010 0101
            nbits       5
        Should yield int 20 = binary 0001 0100 because the number is considered to have a length of 5 bits, meaning 
        that the rightmost 5 bits are flipped to make 20, and the rest of the bits are truncated
        """
        delta = findopp.bitrev(37, 5)
        self.assertEqual(delta, 20)


class bitrev2Tests(unittest.TestCase):
    def testn1(self):
        """
        input of
            inval       int 1 = binary 0001
            nbits       1
        Should yield '1' because the number is considered to have a length of 1 bit, so only the rightmost bit
        is flipped, yielding no change.
        """
        alpha = findopp.bitrev2(1, 1)
        self.assertEqual(alpha, 1)

    def testn2(self):
        """
        input of
            inval       int 1 = binary 0001
            nbits       2
        Should yield int 2 = binary 0010 because the rightmost 2 bits swap places
        """
        bravo = findopp.bitrev2(1, 2)
        self.assertEqual(bravo, 2)

    def testVaried(self):
        """
        input of
            inval       int 37 = binary 0010 0101
            nbits       1
        Should yield int 1 = binary 0001 because the number is considered to have a length of 1 bit, meaning that the
        rightmost bit is flipped and the rest of the bits are truncated
        """
        charlie = findopp.bitrev2(37, 1)
        self.assertEqual(charlie, 1)

        """
        input of
            inval       int 37 = binary 0010 0101
            nbits       5
        Should yield int 20 = binary 0001 0100 because the number is considered to have a length of 5 bits, meaning 
        that the rightmost 5 bits are flipped to make 20, and the rest of the bits are truncated
        """
        delta = findopp.bitrev2(37, 5)
        self.assertEqual(delta, 20)


class bitrev3Tests(unittest.TestCase):
    """
    While bitrev and bitrev2 aim to have the same behavior with different implementations, bitrev3 is meant to have
    different behavior. It does away with the nbits field and instead assumes all inputs 'x' are 32 bit numbers.
    """
    def testn1(self):
        """
        input of
            x       int 1 = binary 0000 0000 0000 0000 0000 0000 0000 0001
        int result depends on whether the returned value is interpreted as unsigned or signed. binary result should be
        1000 0000 0000 0000 0000 0000 0000 0000 = unsigned 2147483648 = signed -2147483648
        """
        alpha = findopp.bitrev3(1)
        self.assertEqual(alpha, 2147483648)

    """
    testn2 is pointless with bitrev3 because due to the assumption of 32-bit integers, it would behave the same as
    testn1
    """

    def testVaried(self):
        """
        input of
            x       int 37 = binary 0000 0000 0000 0000 0000 0000 0010 0101
        int result depends on whether the returned value is interpreted as unsigned or signed. binary result should be
        1010 0100 0000 0000 0000 0000 0000 0000 = unsigned 2751463424 = signed -1543503872
        """
        charlie = findopp.bitrev3(37)
        self.assertEqual(charlie, 2751463424)




if __name__ == '__main__':
    unittest.main()
