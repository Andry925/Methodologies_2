import unittest
from unittest.mock import patch, call, mock_open
from convertors.ansi_convertor import AnsiConvertor

PATH_TO_MARKDOWN_FILES = 'markdown_files/'
OUTPUT_FILE = "something.html"


class TestAnsiConvertor(unittest.TestCase):
    def setUp(self):
        self.converter = AnsiConvertor

    @patch("builtins.print")
    def test_bold_tags_are_printed(self, mock_print):
        self.converter(f'{PATH_TO_MARKDOWN_FILES}bold.md')
        mock_print.assert_called_with(
            "\x1b[1mtest\x1b[22m \x1b[1msome\x1b[22m")

    @patch("builtins.print")
    def test_paragraphs_are_printed(self, mock_print):
        self.converter(f'{PATH_TO_MARKDOWN_FILES}paragraphs.md')
        calls = [
            call('Paragraph1. Lorem Ipsum Dolor Sit Amet.'),
            call('This is still paragraph 1.'),
            call(''),
            call('And after a blank line this is paragraph 2.'),
            call('')
        ]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_paragraphs_with_additional_tags_are_printed(self, mock_print):
        self.converter(
            f'{PATH_TO_MARKDOWN_FILES}paragraphs_with_additional_text.md')

        calls = [
            call("Paragraph1. Lorem Ipsum Dolor Sit Amet."),
            call("This is still paragraph 1."),
            call(""),
            call("And after a blank line this is paragraph 2."),
            call(""),
            call("\x1b[1mAdditional text\x1b[22m"),
            call("\x1b[7mmonospace\x1b[27m"),
            call("\x1b[3mтакож працює\x1b[23m")
        ]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_common_tags_are_printed(self, mock_print):
        self.converter(f'{PATH_TO_MARKDOWN_FILES}common_tags.md')
        calls = [
            call("\x1b[1mtest\x1b[22m"),
            call("\x1b[1mcorrect\x1b[22m"),
            call("\x1b[7mправильно\x1b[27m"),
            call("\x1b[3mitalic\x1b[23m \x1b[7mmonospaced\x1b[27m \x1b[7mПривіт\x1b[27m")]
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_pre_tags_are_printed(self, mock_print):
        self.converter(f'{PATH_TO_MARKDOWN_FILES}pre_tag.md')
        mock_print.assert_called_with("\x1b[7mThis is a pre tag\x1b[27m'")

    @patch("builtins.open", new_callable=mock_open)
    def test_can_write_to_file(self, mock_file):
        file_content = "**test** **some**"
        expected_html_content = "\x1b[1mtest\x1b[22m \x1b[1msome\x1b[22m"
        with patch.object(AnsiConvertor, 'read_md_file', return_value=[file_content]):
            AnsiConvertor(f'{PATH_TO_MARKDOWN_FILES}bold.md', OUTPUT_FILE)
        mock_file.assert_called_with(OUTPUT_FILE, 'a', encoding='utf-8')
        mock_file().write.assert_called_with(expected_html_content)

    def test_not_closed_tags(self):
        with self.assertRaises(ValueError) as e:
            self.converter(f'{PATH_TO_MARKDOWN_FILES}not_closed_tags.md')

        self.assertEqual("You forgot to close the tag", e.exception.args[0])

    def test_invalid_combination(self):
        with self.assertRaises(ValueError) as e:
            self.converter(
                f'{PATH_TO_MARKDOWN_FILES}invalid_tag_combination.md')

        self.assertEqual(
            "The sequence of special characters is incorrect",
            e.exception.args[0])

    def tearDown(self):
        del self.converter


if __name__ == '__main__':
    unittest.main()
