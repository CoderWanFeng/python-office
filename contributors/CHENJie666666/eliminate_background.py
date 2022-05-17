"""
功能：消除图片背景
"""

from PIL import Image

def _hex_to_rgb(hex):
    """
    十六进制转RGB
    """
    if hex[0] != '#' or len(hex) != 7:   
        print('注意：十六进制格式颜色错误，请输入7位以\'#\'开头的字符串\n')
        return None
    else:
        r = int('0x' + hex[1:3], 16)
        g = int('0x' + hex[3:5], 16)
        b = int('0x' + hex[5:7], 16)
        return (r, g, b)

def eliminate_bc(src_img_path, save_img_path, margin=30, bc_color=None):
    """
    将图片的背景变成透明色
    参数：
        src_img_path: string, 原始图片存储路径
        margin: int, 和背景颜色的差异值
        bc_color, string or tuple 背景颜色值（十六进制或RGB值）
    """
    img = Image.open(src_img_path)
    width, height = img.size
    
    # 获取背景颜色的RGB值
    if bc_color:
        # 给定背景色
        if isinstance(bc_color, str):
            r, g, b = _hex_to_rgb(bc_color)
        else:
            r, g, b = bc_color
    else:
        # 未给定背景色，拾取图片左上角颜色作为背景色
        pix = img.load()
        if src_img_path.endswith('.jpg'):
            r, g, b = pix[int(width / 20), int(height / 20)]
        elif src_img_path.endswith('.png'):
            r, g, b, _ = pix[int(width / 20), int(height / 20)]

    img = img.convert("RGBA")
    datas = img.getdata()
    newData = list()

    # 背景填充零透明度
    for item in datas:
        if (item[0] >= max(r - margin, 0) and item[0] <= min(r + margin, 255)) \
            and (item[1] >= max(g - margin, 0) and item[1] <= min(g + margin, 255)) \
            and (item[2] >= max(b - margin, 0) and item[2] <= min(b + margin, 255)):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)    
    img.putdata(newData)

    # 保存新图片
    img.save(save_img_path, "PNG")

if __name__ == '__main__':

    # 未设定背景颜色        
    eliminate_bc('test.jpg', 'a.png')

    # 设定背景颜色
    # eliminate_bc('test.jpg', 'a.png', bc_color=(255, 255, 255))
    # eliminate_bc('test.jpg', 'a.png', bc_color='#FFFFFF')
