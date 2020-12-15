import unittest
from typing import Any, List

from hstest.check_result import CheckResult
from hstest.common.reflection_utils import get_main
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestDynamicOutput(StageTest):

    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin=[self.in1, self.in2])
        ]

    def in1(self, out):
        if out != '1\n2\n':
            0/0
        return '3\n4'

    def in2(self, out):
        if out != '5\n6\n':
            0/0
        return '7\n8\n'

    def check(self, reply: str, attach: Any) -> CheckResult:
        return CheckResult.correct()


class Test(unittest.TestCase):
    def test(self):
        status, feedback = TestDynamicOutput(get_main()).run_tests()
        self.assertEqual('test OK', feedback)
        self.assertEqual(status, 0)
