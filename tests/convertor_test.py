import unittest
from unittest.mock import patch, call
from main.convertor import HtmlConvertor

PATH_TO_MARKDOWN_FILES = (
    "/home/andrew/PycharmProjects/software_architecture/implementation/Methodologies_2"
    "/markdown_files/")


class TestHtmlConvertor(unittest.TestCase):

    def setUp(self):
        self.html_convertor = HtmlConvertor

    @patch("builtins.print")
    def test_common_tags_is_printed(self, mock_print):
        self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}bold.md')
        mock_print.assert_called_with("<b>test</b> <b>some</b>")

    @patch("builtins.print")
    def test_paragraphs_are_printed(self, mock_print):
        self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}paragraphs.md')
        calls = [
            call("<p>Paragraph1. Lorem Ipsum Dolor Sit Amet. \nThis is still paragraph 1.</p>"),
            call("<p>And after a blank line this is paragraph 2.</p>")]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_paragraphs_with_additional_tags(self, mock_print):
        self.html_convertor(
            f'{PATH_TO_MARKDOWN_FILES}paragraphs_with_additional_text.md')
        calls = [
            call('<p>Paragraph1. Lorem Ipsum Dolor Sit Amet. \nThis is still paragraph 1.</p>'),
            call('<p>And after a blank line this is paragraph 2.</p>'),
            call('<b>Additional text</b> \n<tt>monospace</tt> \n<i>також працює</i>')]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_common_tags(self, mock_print):
        self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}common_tags.md')
        calls = [
            call(
                '<b>test</b> \n<b>correct</b> \n<tt>правильно</tt> \n<i>italic</i> <tt>monospaced</tt> <pre>Привіт</pre>')

        ]
        mock_print.assert_has_calls(calls)

    def test_not_closed_tags(self):
        with self.assertRaises(ValueError) as e:
            self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}not_closed_tags.md')

        self.assertEqual("You forgot to close the tag", e.exception.args[0])

    def test_invalid_combination(self):
        with self.assertRaises(ValueError) as e:
            self.html_convertor(
                f'{PATH_TO_MARKDOWN_FILES}invalid_tag_combination.md')

        self.assertEqual(
            "The sequence of special characters is incorrect",
            e.exception.args[0])

    def tearDown(self):
        del self.html_convertor


if __name__ == "__main__":
    unittest.main()
