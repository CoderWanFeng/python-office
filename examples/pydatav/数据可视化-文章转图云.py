# -*- coding: UTF-8 -*-

import pydatav

if __name__ == '__main__':
    filename = r'.\txt2wordcloud\test.txt'
    color = 'black'
    result_file = r'.\txt2wordcloud\res.jpg'
    pydatav.image.txt2wordcloud(filename, color, result_file)
