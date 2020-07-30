import docx
import pandas as pd

from config import TEST_DOCX_FILE_PATH, TEST_CONTENT_COLUMN_NAME, ANSWER_A_COLUMN_NAME, ANSWER_B_COLUMN_NAME, \
    ANSWER_C_COLUMN_NAME, ANSWER_D_COLUMN_NAME, ANSWER_COLUMN_NAME, SERIAL_NUMBER_COLUMN_NAME, TEST_XLSX_FILE_PATH
from tools import get_content

f = docx.Document(TEST_DOCX_FILE_PATH)

serial, stem, answer_a, answer_b, answer_c, answer_d, answer = get_content(f.paragraphs[2:])

'''
TEST_CONTENT_COLUMN_NAME = '试题内容'
ANSWER_A_COLUMN_NAME = '可选答案A'
ANSWER_B_COLUMN_NAME = '可选答案B'
ANSWER_C_COLUMN_NAME = '可选答案C'
ANSWER_D_COLUMN_NAME = '可选答案D'
ANSWER_COLUMN_NAME = '答案'
'''
structure_dict = {
    SERIAL_NUMBER_COLUMN_NAME: serial,
    TEST_CONTENT_COLUMN_NAME: stem,
    ANSWER_A_COLUMN_NAME: answer_a,
    ANSWER_B_COLUMN_NAME: answer_b,
    ANSWER_C_COLUMN_NAME: answer_c,
    ANSWER_D_COLUMN_NAME: answer_d,
    ANSWER_COLUMN_NAME: answer
}

df = pd.DataFrame(structure_dict)
# df.set_index(SERIAL_NUMBER_COLUMN_NAME)
df.to_excel(TEST_XLSX_FILE_PATH, index=False)
