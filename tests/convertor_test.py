import unittest
from unittest.mock import patch, call, mock_open
from convertors.html_convertor import HtmlConvertor

PATH_TO_MARKDOWN_FILES = (
    "markdown_files/")

HTML_OUTPUT_PATH = "something.html"

MARKDOWN_COMBINATIONS = (
    "<b>test</b> <b>some</b>",
    "<p>Paragraph1. Lorem Ipsum Dolor Sit Amet. \nThis is still paragraph 1.</p>",
    "<p>And after a blank line this is paragraph 2.</p>",
    "<b>Additional text</b> \n<tt>monospace</tt> \n<i>також працює</i>",
    "<b>test</b> \n<b>correct</b> \n<tt>правильно</tt> \n<i>italic</i> <tt>monospaced</tt> <pre>Привіт</pre>",
    "<pre>This is a pre tag</pre>",
)


class TestHtmlConvertor(unittest.TestCase):

    def setUp(self):
        self.html_convertor = HtmlConvertor

    @patch("builtins.print")
    def test_bold_tags_are_printed(self, mock_print):
        self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}bold.md')
        mock_print.assert_called_with(MARKDOWN_COMBINATIONS[0])

    @patch("builtins.print")
    def test_paragraphs_are_printed(self, mock_print):
        self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}paragraphs.md')
        calls = [
            call(MARKDOWN_COMBINATIONS[1]),
            call(MARKDOWN_COMBINATIONS[2])
        ]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_paragraphs_with_additional_tags_are_printed(self, mock_print):
        self.html_convertor(
            f'{PATH_TO_MARKDOWN_FILES}paragraphs_with_additional_text.md')
        calls = [
            call(MARKDOWN_COMBINATIONS[1]),
            call(MARKDOWN_COMBINATIONS[2]),
            call(MARKDOWN_COMBINATIONS[3])]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_common_tags_are_printed(self, mock_print):
        self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}common_tags.md')
        calls = [
            call(
                MARKDOWN_COMBINATIONS[4])

        ]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_pre_tags_are_printed(self, mock_print):
        self.html_convertor(f'{PATH_TO_MARKDOWN_FILES}pre_tag.md')
        mock_print.assert_called_with(MARKDOWN_COMBINATIONS[5])




    @patch("builtins.open", new_callable=mock_open)
    def test_can_write_to_file(self, mock_file):
        file_content = "**test** **some**"
        expected_html_content = MARKDOWN_COMBINATIONS[0]
        with patch.object(HtmlConvertor, 'read_md_file', return_value=[file_content]):
            HtmlConvertor(f'{PATH_TO_MARKDOWN_FILES}bold.md', HTML_OUTPUT_PATH)
        mock_file.assert_called_with(HTML_OUTPUT_PATH, 'a', encoding='utf-8')
        mock_file().write.assert_called_with(expected_html_content + '\n')

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


unittest.main()
