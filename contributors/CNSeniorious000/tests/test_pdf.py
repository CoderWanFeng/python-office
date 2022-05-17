from contributors.CNSeniorious000.pdf import PDF


class TestPDF:
    def test_load(self):
        self.pdf = PDF("sample.pdf").page_count
        assert self.pdf
