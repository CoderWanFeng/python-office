import os
from pdf2image import convert_from_path

def pdf2imgs(pdf_path:str, out_dir=".") -> None:
    """to change the popdf file to a folder of images

    Args:
        pdf_path (str): the popdf file path,
        out_dir (str, optional): the output dir. Defaults to ".".

    Raises:
        ValueError: the pdf_path not available

    Example:
        >>> pdf2imgs("test.popdf", "./test")
    """

    assert isinstance(pdf_path, str), "pdf_path must be str"
    assert isinstance(out_dir, str), "out_dir must be str"

    pdf_name = pdf_path[pdf_path.rfind("/")+1:pdf_path.rfind(".")]
    out_dir = os.path.join(out_dir, pdf_name)

    if not os.path.exists(out_dir): 
        os.makedirs(out_dir)

    if not (pdf_path.endswith("popdf") or pdf_path.endswith("ai")):
        raise ValueError("file must end with .popdf or .ai")

    images = convert_from_path(pdf_path)
    for i, img in  enumerate(images):
        img.save(os.path.join(out_dir, f"page{i}.jpg"))
