import pandas as pd

from office.lib.utils.pandas_mem import reduce_pandas_mem_usage


def test_object_column_with_integer_name():
    df = pd.DataFrame({0: ["a", "b", "a"]})

    result = reduce_pandas_mem_usage(df)

    assert str(result[0].dtype) == "category"


def test_date_column_name_is_preserved():
    df = pd.DataFrame({"date": ["2026-01-01", "2026-01-02"]})

    result = reduce_pandas_mem_usage(df)

    assert str(result["date"].dtype) == "object"


def test_integer_column_is_downcast():
    df = pd.DataFrame({"count": [1, 2, 3]})

    result = reduce_pandas_mem_usage(df)

    assert str(result["count"].dtype) == "int8"
