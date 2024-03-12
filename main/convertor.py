import re
from validators.validator import Validator


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
            file.write(html_line)

    def convert_to_html(self, md_string):
        md_string = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md_string)
        md_string = re.sub(r'```(.*?)```', r'<pre>\1</pre>', md_string)
        md_string = re.sub(r'`(.*?)`', r'<tt>\1</tt>', md_string)
        md_string = re.sub(r'_(.*?)_', r'<i>\1</i>', md_string)
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

    def run_converter(self, md_file):
        processed_lines = [self.convert_to_html(
            line) for line in self.read_md_file(md_file)]
        for html in self.convert_paragraphs(processed_lines):
            self.write_to_html_file(self.html_file, html)


if __name__ == '__main__':
    converter = HtmlConvertor("test.md", "some.html")
