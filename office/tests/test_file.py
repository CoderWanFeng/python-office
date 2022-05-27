def test_import():
    from .. import file
    assert file
    assert dir(file)


def test_replace4filename():
    path = "./temp_test_test_replace4filename.txt"
    open(path, "w").close()
    from os.path import isfile
    assert isfile(path)
    from ..file import replace4filename
    assert replace4filename
    replace4filename(".", "temp", "tmp")
    assert not isfile(path)
    path = path.replace("temp", "tmp")
    assert path
    assert isfile(path)
    from os import remove
    remove(path)
    assert not isfile(path)
