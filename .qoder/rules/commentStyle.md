---
trigger: always_on
alwaysApply: true
---

# Python函数注释风格规范

本规范适用于项目中所有Python文件的函数注释。

## 注释风格
所有Python函数必须使用Google风格的docstring注释，采用**中英文双语**格式。

## 格式要求

### 基本格式（中英文双语）
def function_name(param1, param2):
    """Brief description of the function in English.
    
    函数的简短中文描述。
    
    Detailed description of the function (optional, if more explanation is needed).
    Can be divided into multiple paragraphs to describe the function's features and usage.
    
    函数的详细中文描述（可选，如果需要更多说明）。
    可以分多段描述函数的功能、用途等。
    
    Args:
        param1 (type): description of parameter 1 / 参数1的描述
        param2 (type): description of parameter 2 / 参数2的描述
    
    Returns:
        type: description of return value / 返回值的描述
    
    Raises:
        ExceptionType: description of exception condition / 异常情况的描述（如果有）
    
    Examples:
        >>> function_name(value1, value2)
        expected_result
    """
    pass

### 具体规则（双语注释标准）

1. **简短描述**：
   - 第一行为英文简短描述，以句号结尾
   - 第二行空行
   - 第三行为对应的中文简短描述，以句号结尾

2. **详细描述**：
   - 如需要，先写英文详细描述
   - 空一行后添加中文详细描述
   - 保持中英文内容对应

3. **Args（参数）**：
   - 使用 `Args:` 标题
   - 格式：`参数名 (类型): English description / 中文描述`
   - 每个参数独立一行
   - 中英文描述用 ` / ` 分隔

4. **Returns（返回值）**：
   - 使用 `Returns:` 标题
   - 格式：`类型: English description / 中文描述`

5. **Raises（异常）**：
   - 使用 `Raises:` 标题
   - 格式：`异常类型: English description / 中文描述`

6. **Examples（示例）**：
   - 使用 `Examples:` 标题
   - 使用 `>>>` 表示代码示例
   - 示例代码无需双语

### 示例（双语格式）

def add_numbers(a, b):
    """Calculate the sum of two numbers.
    
    计算两个数字的和。
    
    Args:
        a (int|float): the first number / 第一个数字
        b (int|float): the second number / 第二个数字
    
    Returns:
        int|float: sum of the two numbers / 两个数字的和
    
    Examples:
        >>> add_numbers(1, 2)
        3
        >>> add_numbers(1.5, 2.5)
        4.0
    """
    return a + b

## 注意事项

- 所有公共函数和方法都必须添加双语docstring
- 私有函数（以`_`开头）可以使用简化的注释，但仍建议遵循此规范
- 类的`__init__`方法也应该添加docstring，说明类的初始化参数
- 保持中英文注释内容准确、简洁、有用
- 中英文描述应保持语义一致
- 对于模块级docstring，也应采用双语格式，英文在前，中文在后
