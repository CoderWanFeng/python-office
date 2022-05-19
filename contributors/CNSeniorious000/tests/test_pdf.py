from contributors.CNSeniorious000.pdf import PDF


class TestPDF:
    filename = "sample.pdf"

    @property
    def pdf(self):
        return PDF(self.filename)

    def test_init(self):
        assert self.pdf.page_count

    def test_new(self):
        another = PDF(self.filename)
        assert self.pdf == another
        assert self.pdf is another

    def test_download(self):
        assert PDF("https://zh.wikipedia.org/api/rest_v1/page/pdf/Wikipedia:首页").page_count

    def test_get_image(self):
        import numpy as np
        assert isinstance(self.pdf.get_image(), np.ndarray)
