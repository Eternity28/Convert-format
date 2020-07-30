import os
from time import sleep

import docx
from pandas import DataFrame

from config import STEM_CONTENT_COLUMN_NAME, ANSWER_A_COLUMN_NAME, ANSWER_B_COLUMN_NAME, \
    ANSWER_C_COLUMN_NAME, ANSWER_D_COLUMN_NAME, ANSWER_COLUMN_NAME, SERIAL_NUMBER_COLUMN_NAME, XLSX_FILES_DIR
from tools import get_content, get_docx_file

for name, docx_file_path in get_docx_file():
    f = docx.Document(docx_file_path)
    print('-----%s-----' % name)

    serial, stem, answer_a, answer_b, answer_c, answer_d, answer = get_content(f.paragraphs)

    stru_dict = {
        SERIAL_NUMBER_COLUMN_NAME: serial,
        STEM_CONTENT_COLUMN_NAME: stem,
        ANSWER_A_COLUMN_NAME: answer_a,
        ANSWER_B_COLUMN_NAME: answer_b,
        ANSWER_C_COLUMN_NAME: answer_c,
        ANSWER_D_COLUMN_NAME: answer_d,
        ANSWER_COLUMN_NAME: answer
    }

    df = DataFrame(stru_dict)

    xlsx_name = os.path.join(XLSX_FILES_DIR, '%s.xlsx' % name)
    print('-------成功将 %s 转成 xlsx' % name)

    df.to_excel(xlsx_name, index=False)


'''
28. SQL语言集数据查询、数据操作、数据定义和数据控制功能于一体，语句INSERT、DELETE、UPDATE实现哪类功能

'''