import unittest
from typing import Any, List

from hstest.check_result import CheckResult
from hstest.common.reflection_utils import get_main
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestImportPackage7(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply: str, attach: Any) -> CheckResult:
        return CheckResult(reply == '3067\n', '')


@unittest.skip('Relative imports doesn\'t work')
class Test(unittest.TestCase):
    def test(self):
        status, feedback = TestImportPackage7(get_main('random_module.main')).run_tests()
        self.assertEqual("test OK", feedback)


if __name__ == '__main__':
    Test().test()
