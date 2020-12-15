import unittest
from typing import Any, List

from hstest.check_result import CheckResult
from hstest.common.reflection_utils import get_main
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestNbspInOutput(StageTest):

    def generate(self) -> List[TestCase]:
        return [
            TestCase()
        ]

    def check(self, reply: str, attach: Any) -> CheckResult:
        return CheckResult(reply == "1\u00202\u00203", '')


class Test(unittest.TestCase):
    def test(self):
        status, feedback = TestNbspInOutput(get_main()).run_tests()
        self.assertEqual("test OK", feedback)
        self.assertEqual(status, 0)
