import re
import argparse
from validators.validator import Validator

REPLACEMENT_ARRAY = [
    ('\\*\\*(.*?)\\*\\*', '<b>\\1</b>'),
    ('```(.*?)```', '<pre>\\1</pre>'),
    ('`(.*?)`', '<tt>\\1</tt>'),
    ('_(.*?)_', '<i>\\1</i>')
]


class HtmlConvertor:

    def __init__(self, md_file, html_file=None):
        self.md_file = md_file
        self.html_file = html_file
        self.validator = Validator(self.md_file)
        self.run_converter(self.md_file)

    def read_md_file(self, md_file):
        with open(md_file, 'r', encoding='utf-8') as file:
            for line in file:
                yield line

    def write_to_html_file(self, html_file, html_line):
        with open(html_file, 'a', encoding='utf-8') as file:
            file.write(html_line + '\n')

    def convert_to_html(self, md_string):
        for regex, replacement in REPLACEMENT_ARRAY:
            md_string = re.sub(regex, replacement, md_string)

        return md_string

    def convert_paragraphs(self, lines):
        paragraph = ""
        for line in lines:

            if line.strip():
                paragraph += line.strip() + " " + '\n'
            else:
                if paragraph:
                    yield f"<p>{paragraph.strip()}</p>"
                    paragraph = ""
        if paragraph:
            yield f"{paragraph.strip()}"

    @staticmethod
    def parse_command_line_args():
        parser = argparse.ArgumentParser(description='Parse command line')
        parser.add_argument('input_filepath', default=None)
        parser.add_argument('--out', default=None)
        args = parser.parse_args()
        return args

    def run_converter(self, md_file):
        processed_lines = [self.convert_to_html(
            line) for line in self.read_md_file(md_file)]
        for html in self.convert_paragraphs(processed_lines):
            if self.html_file:
                self.write_to_html_file(self.html_file, html)
            print(html)


HtmlConvertor(
    HtmlConvertor.parse_command_line_args().input_filepath,
    HtmlConvertor.parse_command_line_args().out)
