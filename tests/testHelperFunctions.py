import unittest
import numpy as np
import turbo_seti.findoppler.helper_functions as hlp


class HelperTests(unittest.TestCase):
    """
    These aren't real tests, I just used them to understand some of the undocumented functions in helper_functions.py
    """
    def testFlipX1(self):
        alpha = np.zeros(10)
        for i in range(1, 11):
            alpha[i- 1] = i
        hlp.FlipX(alpha, 5, 2)
        print("1")

    def testFlipBand1(self):
        bravo = np.zeros(19)
        for i in range(1, 20):
            bravo[i- 1] = i
        hlp.FlipBand(bravo, 6, 3)
        print("1")

    def testAxisSwap1(self):
        charlie = np.zeros(15)
        delta = np.zeros(15)
        for i in range(0, 15):
            charlie[i] = i
        hlp.AxisSwap(charlie, delta, 3, 5)
        x = 1

if __name__ == '__main__':
    unittest.main()
