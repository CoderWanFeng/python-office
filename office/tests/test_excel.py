def test_null():
    assert True


def test_import():
    from .. import excel
    assert excel
    assert dir(excel)


def test_fake2excel():
    from ..excel import fake2excel
    assert fake2excel
    path = "./temp_test_fake2excel.xlsx"
    num = 1234
    fake2excel(rows=num, path=path)
    from os.path import isfile
    assert isfile(path)
    from pandas import read_excel
    assert len(read_excel(path, 0)) == num

    fake2excel(["name", "country"], num, "english", path)
    assert isfile(path)
    assert read_excel(path, 0).shape == (num, 2)

    # the case below will not pass until last commit
    fake2excel(["name", "name"], num, "english", path)
    assert isfile(path)
    assert read_excel(path, 0).shape == (num, 2)

    from os import remove
    remove(path)
    assert not isfile(path)
