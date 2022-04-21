import os
import unittest

from hstest import TestedProgram, correct, wrong
from hstest.dynamic.dynamic_test import dynamic_test
from hstest.stage import PlottingTest
from tests.outcomes.plot.universal_test import universal_test


class TestHist(PlottingTest):
    @dynamic_test
    def test(self):
        files = [i for i in os.listdir() if i != 'test.py' and i.endswith('.py')]

        for file in files:
            program = TestedProgram(file)
            program.start()

            if str(program) != file:
                return wrong("hs-test-python didn't run requested file")

            universal_test(
                file,
                'hist',
                [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]],
                [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
                self.new_figures()
            )

        return correct()


class Test(unittest.TestCase):
    def test(self):
        status, feedback = TestHist().run_tests()
        self.assertEqual(status, 0)


if __name__ == '__main__':
    Test().test()
