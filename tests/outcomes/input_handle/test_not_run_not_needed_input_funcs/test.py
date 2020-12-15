import unittest
from typing import Any, List

from hstest.check_result import CheckResult
from hstest.common.reflection_utils import get_main
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestNotRunNotNeededInputFuncs(StageTest):

    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin=[lambda x: '3\n4', lambda x: 0/0])
        ]

    def check(self, reply: str, attach: Any) -> CheckResult:
        return CheckResult.correct()


class Test(unittest.TestCase):
    def test(self):
        status, feedback = TestNotRunNotNeededInputFuncs(get_main()).run_tests()

        self.assertEqual('test OK', feedback)
        self.assertEqual(status, 0)
