#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import time

random.seed(time.time())
# random.sample(string,num)从指定string中获取长度为num的随机字符



def random_col():  # 颜色值
    return (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))


def make(strs, width=400, height=200):
    im = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('verdana.ttf', width // 4)  # //浮点数除法，结果四舍五入
    font_width, font_height = font.getsize(strs)
    print
    font_width, font_height
    strs_len = len(strs)
    print
    'strs_len: ' + str(strs_len)
    x = (width - font_width) // 2
    y = (height - font_height) // 2
    print
    x, y
    total_dex = 0
    for i in strs:
        draw.text((x, y), i, random_col(), font)
        temp = random.randint(-30, 30)
        total_dex += temp
        im = im.rotate(temp)  # 旋转角度
        draw = ImageDraw.Draw(im)
        x += font_width / strs_len
    im = im.rotate(-total_dex)
    draw = ImageDraw.Draw(im)
    draw.line(  # 下面三段代码用来画直线，参数分别是直线起始、终止位置，颜色以及宽度
        [(random.randint(0, width // 4),
          random.randint(0, height // 4)
          ),
         (random.randint(width // 4 * 3, width),
          random.randint(height // 4 * 3, height)
          )],
        fill=random_col(),
        width=width // 80
    )
    draw.line(
        [(random.randint(0, width // 4),
          random.randint(height // 4 * 3, height)
          ),
         (random.randint(width // 3 * 2, width),
          random.randint(0, height // 3)
          )],
        fill=random_col(),
        width=width // 80
    )
    draw.line(
        [(random.randint(width // 4 * 3, width),
          random.randint(height // 4 * 3, height)
          ),
         (random.randint(width // 3 * 2, width),
          random.randint(0, height // 3)
          )],
        fill=random_col(),
        width=width // 80
    )
    # im = im.crop((width//10,height//10,width,height))
    for x in range(width):
        for y in range(height):
            col = im.getpixel((x, y))  # 获取坐标点像素的RGB值
            if col == (255, 255, 255) or col == (0, 0, 0):
                draw.point((x, y), fill=random_col())  # 将背景中的黑白两色重新随机涂色
    im = im.filter(ImageFilter.BLUR)  # 模糊效果
    # im.show()
    # im = im.convert('L')
    im.save('out.jpg')
    return strs


def verification():
    random.seed(time.time())
    num = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 4))
    return make(num)