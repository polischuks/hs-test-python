import unittest
from typing import Any, List

from hstest.check_result import CheckResult
from hstest.common.reflection_utils import get_main
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class UnexpectedErrorUserMainFileNotExists(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply: str, attach: Any) -> CheckResult:
        return CheckResult(True, '')


class Test(unittest.TestCase):
    def test(self):
        status, feedback = UnexpectedErrorUserMainFileNotExists(get_main('bad_file')).run_tests()

        self.assertIn(
            'Error in test #1\n\n'
                        
            'Cannot find a file to import and run your code.\n'
            'Are your project files located at "',

            feedback
        )


if __name__ == '__main__':
    Test().test()
