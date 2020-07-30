import os

# 项目文件绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 所有文件存放目录
FILES_DIR = os.path.join(BASE_DIR, 'file')

# doc 文件存放目录
DOC_FILES_DIR = os.path.join(FILES_DIR, 'doc')
# docx 文件存放目录
DOCX_FILES_DIR = os.path.join(FILES_DIR, 'docx')
# xlsx 文件存目录
XLSX_FILES_DIR = os.path.join(FILES_DIR, 'xlsx')

# doc 测试文件路径
TEST_DOC_FILE_PATH = os.path.join(DOC_FILES_DIR, 'test.doc')
# docx 测试文件路径
TEST_DOCX_FILE_PATH = os.path.join(DOCX_FILES_DIR, 'test.docx')
# xlsx 测试文件路径
TEST_XLSX_FILE_PATH = os.path.join(XLSX_FILES_DIR, 'test.xlsx')

'''xlsx 文件 列名'''
SERIAL_NUMBER_COLUMN_NAME = '序号'
STEM_CONTENT_COLUMN_NAME = '试题内容'
ANSWER_A_COLUMN_NAME = '可选答案A'
ANSWER_B_COLUMN_NAME = '可选答案B'
ANSWER_C_COLUMN_NAME = '可选答案C'
ANSWER_D_COLUMN_NAME = '可选答案D'
ANSWER_COLUMN_NAME = '答案'