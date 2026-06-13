import numpy as np


def reduce_pandas_mem_usage(df) -> object:
    """遍历DataFrame的所有列并修改数据类型以减少内存使用。
    
    Args:
        df: pandas DataFrame对象
    
    Returns:
        object: 优化后的DataFrame对象
    """
    # start_mem = df.memory_usage().sum() / 1024 ** 2
    # print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
        else:
            if 'date' in col:
                pass
            else:
                df[col] = df[col].astype('category')

    # end_mem = df.memory_usage().sum() / 1024 ** 2
    # print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    # print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df
