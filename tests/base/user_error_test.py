from tests.base.expected_fail_test import ExpectedFailTest


class UserErrorTest(ExpectedFailTest):
    _base_not_contain = 'Unexpected error'
