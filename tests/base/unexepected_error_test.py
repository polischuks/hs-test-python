from tests.base.expected_fail_test import ExpectedFailTest


class UnexpectedErrorTest(ExpectedFailTest):
    _base_contain = 'Unexpected error'
