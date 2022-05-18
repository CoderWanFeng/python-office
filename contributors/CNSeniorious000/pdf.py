import os
from functools import cache, cached_property


# PDF与栅格化
# noinspection PyPackageRequirements
class PDF:
    """
    a pdf document with optimized lazy processing
    @Author & Date:CNSeniorious000 2022/5/17
    """

    @cache
    def __new__(cls, *args, **kwargs):
        """a path refers to only one document"""
        return object.__new__(cls)

    def __init__(self, path: str):
        """load from disk or internet"""
        if path.startswith("http"):
            import requests
            self.raw = requests.get(path).content
        else:
            self.raw = open(path, "rb").read()

    @cached_property
    def doc(self):
        import fitz
        # noinspection PyUnresolvedReferences
        return fitz.open(stream=self.raw)

    @property
    def page_count(self):
        return self.doc.page_count

    @cache
    def get_pixmap(self, page=0, dpi=108, alpha=True):
        return self.doc[page].get_pixmap(dpi=dpi, alpha=alpha)

    @cache
    def get_image(self, *args, **kwargs):
        from imageio import imread
        from numpy import asarray
        return asarray(imread(self.get_pixmap(*args, **kwargs).tobytes()))

    @staticmethod
    def show(image):
        from matplotlib.pyplot import imshow, show
        imshow(image)
        return show()

    def show_image(self, *args, **kwargs):
        return self.show(self.get_image(*args, **kwargs))

    def save_image(self, file_path: str, page=0, dpi=144, alpha=True):
        return self.get_pixmap(page, dpi, alpha).save(file_path)

    def save_images(self, dir_path: str, pages=..., dpi=144, alpha=True, encode="png", show_bar=True):
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

        it = range(self.page_count) if pages is ... else pages

        if show_bar:
            from alive_progress import alive_it
            it = alive_it(it)

        for page in it:
            self.save_image(f"{dir_path}/{page}.{encode}", page, dpi, alpha)
