import pomarkdown


def excel2markdown(input_file, output_file=r'./excel2markdown.md', sheet_name=None):
    pomarkdown.excel2markdown(input_file, output_file, sheet_name)
