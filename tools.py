import os

from config import DOC_FILES_DIR, DOCX_FILES_DIR


def get_doc_file():
    doc_files_list = os.listdir(DOC_FILES_DIR)

    for doc_file in doc_files_list:
        yield os.path.join(DOC_FILES_DIR, doc_file)


def get_docx_file():
    docx_files_list = os.listdir(DOCX_FILES_DIR)

    for docx_file in docx_files_list:
        yield os.path.splitext(docx_file)[0], os.path.join(DOCX_FILES_DIR, docx_file)


'''
0
5
10
'''
'''
A       1       6
B       2       7
C       3       8
D       4       9
'''


def get_answer(content, start_str):
    if content.startswith(start_str):
        return content.split('.', 1)[-1]
    return content


def get_content(paragraphs):
    is_start = 0

    stem_or_answer = 0

    stem = []
    answer_a = []
    answer_b = []
    answer_c = []
    answer_d = []
    for p in paragraphs:

        content = p.text.strip()

        if content and is_start != 2:

            is_start += 1
        elif content and is_start == 2:
            if stem_or_answer % 5 == 0:
                stem.append(p.text.split('.', 1)[-1])
            elif stem_or_answer % 5 == 1:
                A = get_answer(content, 'A')
                answer_a.append(A)
            elif stem_or_answer % 5 == 2:
                B = get_answer(content, 'B')
                answer_b.append(B)
            elif stem_or_answer % 5 == 3:
                C = get_answer(content, 'C')
                answer_c.append(C)
            elif stem_or_answer % 5 == 4:
                D = get_answer(content, 'D')
                answer_d.append(D)
            stem_or_answer += 1

    serial = [i for i in range(1, len(stem) + 1)]
    answer = [' ' for i in range(len(stem))]

    print(len(serial))
    print(len(stem))
    for i in stem:
        print(i)
    print(len(answer_a))
    print(len(answer_b))
    print(len(answer_c))
    print(len(answer_d))
    print(len(answer))

    return serial, stem, answer_a, answer_b, answer_c, answer_d, answer


if __name__ == '__main__':

    for file_path in get_doc_file():
        print(file_path)
