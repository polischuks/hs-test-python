import os
from inspect import cleandoc
import unittest
from typing import Any, List

from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase, SimpleTestCase


class TestEmptyEval(StageTest):

    def generate(self) -> List[TestCase]:
        return [
            TestCase()
        ]


class Test(unittest.TestCase):
    def test(self):
        file = __file__.replace(os.sep, '.')[:-3]
        file = file[file.find('.tests.') + 1: file.rfind('.') + 1] + 'main'
        status, feedback = TestEmptyEval(file).run_tests()

        self.assertEqual('Exception in test #1\n'
                         '\n'
                         'Traceback (most recent call last):\n'
                         '  File "main.py", line 2, in <module>\n'
                         '    print(eval(")"))\n'
                         '  File "<string>", line 1\n'
                         '    )\n'
                         '    ^\n'
                         'SyntaxError: unmatched \')\'\n'
                         '\n'
                         'Please find below the output of your program during this failed test.\n'
                         '\n'
                         '---\n'
                         '\n'
                         '123', feedback)
        self.assertNotEqual(status, 0)


if __name__ == '__main__':
    Test().test()