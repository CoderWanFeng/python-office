# -*- coding: UTF-8 -*-

import office

office.pdf.add_mark(pdf_file=r'./test_files/add_mark/程序员晚枫（没加水印）.pdf', mark_str='程序员晚枫',
                    output_path=r'./test_files/add_mark/output', output_file_name='程序员晚枫（加了水印）.pdf')
