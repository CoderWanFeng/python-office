import pandas as pd
import os # os库用来处理文件和文件夹路径

# 第一步：告诉程序你的Excel文件放在哪个文件夹里
# 请把下面的 '你的excel文件所在的文件夹路径' 替换成你实际的文件夹路径
# 例如：如果你把文件放在桌面的一个叫 '我的数据' 的文件夹里，路径可能是 'C:/Users/你的用户名/Desktop/我的数据' (Windows) 或 '/Users/你的用户名/Desktop/我的数据' (macOS)

folder_path = (r"folder_path")

# 第二步：找到这个文件夹里所有的Excel文件
# 我们只找以 .xlsx 或 .xls 结尾的文件
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls')]

# 第三步：创建一个空的“篮子”，准备装所有工作表的数据
all_sheets_data = []

# 第四步：一个一个地处理找到的每个Excel文件
for file_name in excel_files:
    # 拼接出完整的文件路径
    file_path = os.path.join(folder_path, file_name)
    print(f'正在处理文件: {file_name}') # 打印出来让你知道程序在干嘛

    try:
        # 第五步：读取当前Excel文件里的所有工作表
        # sheet_name=None 告诉pandas读取所有工作表，结果是一个字典，
        # 字典的键是工作表的名字，值就是对应工作表的数据（一个DataFrame）
        excel_data = pd.read_excel(file_path, sheet_name=None)

        # 第六步：遍历这个文件里的每一个工作表
        for sheet_name, df in excel_data.items():
            print(f'  正在处理工作表: {sheet_name}') # 打印出来让你知道正在处理哪个工作表
            # 现在 df 就是当前工作表的数据了

            # 可选操作：如果你想知道每行数据原来是哪个文件哪个工作表的，可以加上这两列
            # df['来源文件'] = file_name
            # df['来源工作表'] = sheet_name

            # 把当前工作表的数据（df）放到我们之前准备好的“篮子”里
            all_sheets_data.append(df)

    except Exception as e:
        # 如果处理某个文件出错了，打印错误信息，然后跳过这个文件，继续处理下一个
        print(f'处理文件 {file_name} 时出错: {e}')
        continue # 跳过当前循环的剩余部分，进入下一个文件

# 第七步：检查“篮子”里有没有数据，如果有，就把它们全部拼接到一起
if all_sheets_data:
    # pd.concat() 函数就是用来把多个DataFrame（表格）按行或列拼接起来的
    # ignore_index=True 会重新生成一个连续的行索引，避免原来表格的索引混在一起
    merged_df = pd.concat(all_sheets_data, ignore_index=True)

    # 第八步：把合并好的大表格（merged_df）存到一个新的Excel文件里
    # 请把下面的 '合并后的数据.xlsx' 替换成你想要保存的新文件名和路径
    output_file_path = f'{folder_path}/合并后的数据.xlsx'
    # index=False 告诉pandas不要把DataFrame的行索引写入Excel文件
    merged_df.to_excel(output_file_path, index=False)

    print(f'所有工作表已合并并保存到 {output_file_path}')
else:
    print('没有找到任何可以处理的excel文件或工作表，或者处理过程中都出错了。')
