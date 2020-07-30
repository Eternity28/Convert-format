import os
import subprocess

from config import DOCX_FILES_DIR

# subprocess.check_output(["soffice","--headless","--invisible","--convert-to","docx",DOC_FILE_PATH,"--outdir",DOCX_FILES_DIR])
from tools import get_doc_file


def doc_to_docx():
    for doc_file_path in get_doc_file():
        print("-------正在转化文件: %s --------" % os.path.basename(doc_file_path))

        subprocess.check_output(
            ["soffice", "--headless", "--invisible", "--convert-to", "docx", doc_file_path, "--outdir", DOCX_FILES_DIR]
        )

if __name__ == '__main__':
    '''
    将所有doc文件转成docx文件
    '''
    doc_to_docx()