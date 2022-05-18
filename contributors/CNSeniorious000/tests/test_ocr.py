from contributors.CNSeniorious000.ocr import ImgReader


class TestOCR:
    filename = "sample.png"

    @property
    def img(self):
        return ImgReader(self.filename)

    def test_new(self):
        another = ImgReader(self.filename)
        assert self.img == another
        assert self.img is another

    def test_download(self):
        ImgReader("https://pic3.zhimg.com/80/v2-d0289dc0a46fc5b15b3363ffa78cf6c7.png").show()

    def test_bbox(self):
        self.img.show_image_with_bbox((255, 255, 0))
