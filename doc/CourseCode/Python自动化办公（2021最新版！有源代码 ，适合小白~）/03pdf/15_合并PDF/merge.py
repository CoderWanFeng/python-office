from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # 把每张PDF页面加入到这个可读取对象中
            pdf_writer.addPage(pdf_reader.getPage(page))

    # 把这个已合并了的PDF文档存储起来
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['静夜思.pdf', '静夜思.pdf']
    merge_pdfs(paths, output='pandas官方文档中文版.pdf')