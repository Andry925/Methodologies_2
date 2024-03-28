import re

NOT_CLOSED_TAG_REGEX = (r'(^[\*_`]+\w+[^_\*`]+$)|([\*]+[\w]+[`_]+$)'
                        r'|([_]+\w+[\*`]+$)|([`]+\w+[\*_]+$)')
COMBINATION_TAG_REGEX = (r'(([\*]+[_`]+[\w\u0410-\u044F `\*]+[_`]*[\*]*)|([_]+[\*`]+'
                         r'[\w\u0410-\u044F `\*]+[\*`]*[_]*)|([`]+[\*_]+[\w\u0410-\u044F `\*]+[\*_]*[`]*))')


class Validator:

    def __init__(self, file_path):
        self.file_path = file_path
        self.run_validation(file_path)


    def read_markdown_file(self, md_file):
        with open(md_file, 'r') as file:
            for line in file:
                yield line

    def validate_not_closed_tag(self, line):
        if re.match(NOT_CLOSED_TAG_REGEX, line):
            raise ValueError("You forgot to close the tag")
        return line

    def validate_tag_combination(self, line):
        if re.match(COMBINATION_TAG_REGEX, line):
            raise ValueError("The sequence of special characters is incorrect")
        return line

    def run_validation(self, file_path):
        for line in self.read_markdown_file(file_path):
            self.validate_not_closed_tag(line)
            self.validate_tag_combination(line)



