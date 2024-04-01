import re
from validators.validator import Validator

REPLACEMENT_ARRAY = [
    ('\\*\\*(.*?)\\*\\*', '\x1b[1m\\1\x1b[22m'),
    ('```(.*?)```', '<pre>\\1</pre>'),
    ('`(.*?)`', '\x1b[7m\\1\x1b[27m'),
    ('_(.*?)_', '\x1b[3m\\1\x1b[23m')

]


class AnsiConvertor:

    def __init__(self, md_file, ansi_file=None):
        self.md_file = md_file
        self.ansi_file = ansi_file
        self.validator = Validator(self.md_file)
        self.run_converter(self.md_file)

    def read_md_file(self, md_file):
        with open(md_file, 'r', encoding='utf-8') as file:
            for line in file:
                yield line

    def write_to_html_file(self, html_file, html_line):
        with open(html_file, 'a', encoding='utf-8') as file:
            file.write(html_line)

    def convert_to_ansi(self, md_string):
        ansi_string = md_string
        for regex, replacement in REPLACEMENT_ARRAY:
            ansi_string = re.sub(regex, replacement, ansi_string)
        return ansi_string

    def convert_preformatted_text(self, lines):
        in_block = False
        preformatted_block = ""
        for line in lines:
            if line.strip() == "```":
                in_block = not in_block
                if not in_block:
                    yield f"\x1b[7m{preformatted_block.strip()}\x1b[27m'"
                    preformatted_block = ""
                continue
            if in_block:
                preformatted_block += line
            else:
                yield line

    def run_converter(self, md_file):
        lines = self.read_md_file(md_file)
        preformatted_converted_lines = self.convert_preformatted_text(lines)
        for line in preformatted_converted_lines:
            processed_line = self.convert_to_ansi(line)
            if self.ansi_file:
                self.write_to_html_file(self.ansi_file, processed_line)

            print(processed_line)


if __name__ == '__main__':
    ansi_convertor = AnsiConvertor(
        "/home/andrew/PycharmProjects/Methodologies_2/markdown_files/bold.md",
        "some.txt")
