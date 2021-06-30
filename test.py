import unittest
import math
from main import AddTwoLinkedLists

class AppTestCase(unittest.TestCase):

    def test_output_1(self):
        value1 = [2,4,3]
        value2 = [5,6,4]

        p = AddTwoLinkedLists(value1, value2)

        output = p.calculate()

        self.assertEqual(output, [7,0,8])

    def test_output_2(self):
        value1 = [0]
        value2 = [0]

        p = AddTwoLinkedLists(value1, value2)

        output = p.calculate()

        self.assertEqual(output, [0])

    def test_output_3(self):
        value1 = [9,9,9,9,9,9,9]
        value2 = [9,9,9,9]

        p = AddTwoLinkedLists(value1, value2)

        output = p.calculate()

        self.assertEqual(output, [8,9,9,9,0,0,0,1])

def suite():
    suite = unittest.TestSuite()

    suite.addTest(AppTestCase('test_output_1'))
    suite.addTest(AppTestCase('test_output_2'))
    suite.addTest(AppTestCase('test_output_3'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())