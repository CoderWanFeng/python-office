""""
Creator:rs1973-bit
E-mail:dingzheng_2023@qq.com/gunshi98@gmail.com
Description:支持输入一个目录或一张图片,修改它(或者整个目录里)的图片尺寸,色彩通道,并决定是否留下图像的
alpha值,会自动筛选不是图片或不支持的格式 程序为多线程(多进程下使用笔记本测试时cpu过热),但gif合成
暂时不支持多线程

ps:这是我的第一个项目,有很多做得不够好的地方,请多包容
"""

import os
import time
from concurrent.futures import ThreadPoolExecutor


from PIL import Image, ImageOps


def get_img(srcpath=None, sinfile=None):
    """筛选目录中的非图片文件,只筛选一层,不读取子目录里的文件"""

    img_lst = []
    not_img = ''
    if srcpath:
        for dirpath, dirname, filenames in os.walk(srcpath):
            if filenames:
                for img in filenames:
                    img = os.path.join(dirpath, img)
                    if os.path.isfile(img):
                        if os.path.splitext(img)[1].lower() in {".jpg", ".jpeg", ".png", ".bmp", ".tiff", '.webp'}:
                            img_lst.append(img)
                        else:
                            not_img += f'{img}\n'
            else:
                print(f'注意: 目录 {dirpath} 中没有图片')
                return []

        if not_img:
            print(f'提示: 以下文件/目录不是图片:\n{not_img}')
        return img_lst

    if sinfile:
        if os.path.splitext(sinfile)[1].lower() in {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", '.webp'}:
            return [sinfile]
        else:
            print(f'错误: 文件 {sinfile} 不是图片')
            return []


def normal_img(im, input_info: tuple, outpath: str, kind: str, img: str, alpha: bool):
    """图像的缩放处理,每一个格式都会用到"""
    if input_info:
        x, y = input_info
        if round(int(x) / im.size[0], 2) == round(int(y) / im.size[1], 2):
            real_tuple = (int(x), int(y))
            im = im.resize(real_tuple)
        else:
            if not alpha:
                pad_im = ImageOps.pad(im, (int(x), int(y)), color='#FFFFFF')
            else:
                pad_im = ImageOps.pad(im, (int(x), int(y)),
                                      color=(0, 0, 0, 0), centering=(0.5, 0.5))

            im = pad_im

    base_name = os.path.basename(img)
    name_only = os.path.splitext(base_name)[0]
    save_path = os.path.join(outpath, name_only + kind)
    im.save(save_path, format=kind[1:].upper())
    im.close()


def gif(filenames=None, outpath=None, duration=300, name='index'):
    """合成gif"""
    try:
        img_lst = [Image.open(i).copy().convert('RGB') for i in filenames]
        img_lst[0].save(
            os.path.join(outpath, f'{name}.gif'),
            append_images=img_lst[1:],
            duration=duration,
            loop=0,
            optimize=True
        )
    except ValueError as e:
        print(f'错误: 序列中图片大小不一致, {e}')


def process_img(outpath=None, input_info=None, kind=None, alpha=None, img=None):
    """修改图片中的alpha"""
    if kind in ('.png', '.webp', '.bmp'):
        with Image.open(img) as im:
            im = im.convert('RGBA')
            if not alpha:
                new_im = im.copy()
                new_im.convert('RGB')
                alpha_pixel = im.getdata()
                write_pixel = []
                for item in alpha_pixel:
                    r, g, b, a = item
                    if a == 0:
                        write_pixel.append((255, 255, 255))
                    else:
                        write_pixel.append((r, g, b))
                new_im.putdata(write_pixel)
                im = new_im
            normal_img(im, input_info, outpath, kind, img, alpha)
    else:
        with Image.open(img) as im:
            if im.mode == 'RGBA':
                im = im.convert('RGB')
            normal_img(im, input_info, outpath, kind, img, alpha)


def main(srcpath: str = None, outpath: str = None, sinfile: str = None,
         input_info: tuple = None, kind: str = '.jpeg', alpha: bool = False,
         duration: int = 300, process: int = 5):
    """主逻辑函数"""
    start = time.time()

    filenames = get_img(srcpath, sinfile)
    if not filenames:
        return

    if kind == '.gif':
        print('注意:请确保图像列表中所有图片的大小都一样')
        gif(filenames, outpath, duration)
    else:
        with ThreadPoolExecutor(process) as pool:
            futures = [pool.submit(process_img, outpath,
                                   input_info, kind, alpha, img) for img in filenames]
            for fut in futures:
                fut.result()

    end = time.time()
    print(f'处理完成, 耗时: {end - start:.2f}s')
