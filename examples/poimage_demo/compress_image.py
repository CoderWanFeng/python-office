# -*- coding: UTF-8 -*-

import office

office.image.compress_image(input_file=r'D:\workplace\code\github\poimage\tests\头像.jpg',
                            output_file="compressed.jpg",
                            quality=50)  # 质量，1-100之间，数值越低压缩率越高
