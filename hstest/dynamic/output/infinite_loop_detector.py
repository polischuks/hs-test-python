from typing import List

from hstest.dynamic.security.exit_exception import ExitException
from hstest.exception.testing import InfiniteLoopException


class InfiniteLoopDetector:

    def __init__(self):
        self.working: bool = True

        self.check_same_input_between_requests = True
        self.check_no_input_requests_for_long = True
        self.check_repeatable_output = True

        self._curr_line: List[str] = []
        self._since_last_input: List[str] = []

        self._between_input_requests = []
        self._BETWEEN_INPUT_SAVED_SIZE = 20

        self._every_line = []
        self._EVERY_LINE_SAVED_SIZE = 100

        self._chars_since_last_input = 0
        self._lines_since_last_input = 0

        self._CHARS_SINCE_LAST_INPUT_MAX = 5000
        self._LINES_SINCE_LAST_INPUT_MAX = 500

        self._chars_since_last_check = 0
        self._CHARS_SINCE_LAST_CHECK_MAX = 100

    def write(self, output: str):
        if not self.working:
            return

        if len(output) > 1:
            for c in output:
                self.write(c)
            return

        self._curr_line += [output]
        self._since_last_input += [output]

        self._chars_since_last_input += len(output)
        self._chars_since_last_check += len(output)

        new_lines = output.count('\n')

        if new_lines:
            self._lines_since_last_input += new_lines
            self._every_line += [''.join(self._curr_line)]
            self._curr_line = []
            if len(self._every_line) > self._EVERY_LINE_SAVED_SIZE:
                self._every_line.pop(0)

            self._check_inf_loop_lines()

        if self._chars_since_last_check >= self._CHARS_SINCE_LAST_CHECK_MAX:
            self._check_inf_loop_chars()
            self._chars_since_last_check = 0

    def reset(self):
        self._curr_line = []
        self._chars_since_last_input = 0
        self._lines_since_last_input = 0
        self._chars_since_last_check = 0
        self._since_last_input = []
        self._between_input_requests = []
        self._every_line = []

    def input_requested(self):
        if not self.working:
            return

        self._between_input_requests += [''.join(self._since_last_input)]
        if len(self._between_input_requests) > self._BETWEEN_INPUT_SAVED_SIZE:
            self._between_input_requests.pop(0)
            self._check_inf_loop_input_requests()

        self._since_last_input = []
        self._every_line = []
        self._chars_since_last_input = 0
        self._lines_since_last_input = 0

    def _check_inf_loop_chars(self):
        if self.check_no_input_requests_for_long and \
           self._chars_since_last_input >= self._CHARS_SINCE_LAST_INPUT_MAX:
            self._fail("No input request for the last " +
                       str(self._chars_since_last_input) + " characters being printed.")

    def _check_inf_loop_lines(self):
        if self.check_no_input_requests_for_long and \
           self._lines_since_last_input >= self._LINES_SINCE_LAST_INPUT_MAX:
            self._fail("No input request for the last " +
                       str(self._lines_since_last_input) + " lines being printed.")

        if not self.check_repeatable_output:
            return

        if len(self._every_line) != self._EVERY_LINE_SAVED_SIZE:
            return

        for lines_repeated in range(1, 11):
            self._check_repetition_size(lines_repeated)

    def _check_repetition_size(self, lines_repeated: int):
        how_many_repetitions: int = len(self._every_line) // lines_repeated
        lines_to_check: int = lines_repeated * how_many_repetitions
        starting_from_index: int = len(self._every_line) - lines_to_check

        for shift in range(lines_repeated):
            initial_index: int = starting_from_index + shift
            to_compare: str = self._every_line[initial_index]

            for rep in range(1, how_many_repetitions):
                curr_index: int = initial_index + rep * lines_repeated
                curr: str = self._every_line[curr_index]
                if to_compare != curr:
                    return

        if lines_repeated == 1:
            self._fail("Last " + str(lines_to_check) +
                       " lines your program printed are the same.")
        else:
            self._fail("Last " + str(lines_to_check) + " lines your program printed have "
                       + str(how_many_repetitions) + " blocks of "
                       + str(lines_repeated) + " lines of the same text.")

    def _check_inf_loop_input_requests(self):
        if not self.check_no_input_requests_for_long:
            return

        first_elem = self._between_input_requests[0]
        for curr in self._between_input_requests:
            if curr != first_elem:
                return

        self._fail("Between the last " + str(self._BETWEEN_INPUT_SAVED_SIZE)
                   + " input requests the texts being printed are identical.")

    def _fail(self, reason: str):
        from hstest.stage_test import StageTest
        StageTest.curr_test_run.set_error_in_test(
            InfiniteLoopException(reason))
        raise ExitException()


loop_detector = InfiniteLoopDetector()
