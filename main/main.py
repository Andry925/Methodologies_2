import argparse
from convertors.ansi_convertor import AnsiConvertor
from convertors.html_convertor import HtmlConvertor


class ParseCommand:

    def __init__(self, input_file, output_format, output_file):
        self.input_file = input_file
        self.output_format = output_format
        self.output_file = output_file
        self.choose_convertor(
            self.input_file,
            self.output_format,
            self.output_file)

    @staticmethod
    def parse_command_line_args():
        parser = argparse.ArgumentParser(description='Parse command line')
        parser.add_argument('input_filepath', default=None)
        parser.add_argument('--format', default=None)
        parser.add_argument('--out', default=None)
        args = parser.parse_args()
        return args

    def choose_convertor(self, input_file, output_format, output_file):
        if output_format == 'ansi':
            return AnsiConvertor(input_file, ansi_file=output_file)
        elif output_format == 'html':
            return HtmlConvertor(input_file, html_file=output_file)
        return AnsiConvertor(input_file)


if __name__ == '__main__':
    ParseCommand(
        ParseCommand.parse_command_line_args().input_filepath,
        ParseCommand.parse_command_line_args().format,
        ParseCommand.parse_command_line_args().out
    )
