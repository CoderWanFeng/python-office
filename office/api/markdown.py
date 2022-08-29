from office.core.MarkdownType import MainMarkdown
from office.lib.utils.except_utils import except_dec

mainMarkdown = MainMarkdown()


@except_dec()
def markdown_link_image_to_base64(markdown_path):
    mainMarkdown.markdown_link_image_to_base64(markdown_path)
