import unittest
from validators.validator import Validator

PATH_TO_MARKDOWN_FILES = "/home/andrew/PycharmProjects/software_architecture/implementation/Methodologies_2/markdown_files/"


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator

    def test_validate_not_closed_tag(self):
        not_closed_tag_file = "not_closed_tags.md"
        with self.assertRaises(ValueError) as e:
            self.validator(f'{PATH_TO_MARKDOWN_FILES}{not_closed_tag_file}')
        self.assertEqual("You forgot to close the tag", e.exception.args[0])

    def test_validate_tag_combination(self):
        invalid_tag_combination_file = "invalid_tag_combination.md"
        with self.assertRaises(ValueError) as e:
            self.validator(
                f'{PATH_TO_MARKDOWN_FILES}{invalid_tag_combination_file}')
        self.assertEqual(
            "The sequence of special characters is incorrect",
            e.exception.args[0])

    def test_detect_errors_inside_tags(self):
        error_inside_common_tag = "errors_inside_common.md"
        with self.assertRaises(ValueError) as e:
            self.validator(
                f'{PATH_TO_MARKDOWN_FILES}{error_inside_common_tag}')
        self.assertEqual("You forgot to close the tag", e.exception.args[0])

    def tearDown(self):
        del self.validator


unittest.main()
