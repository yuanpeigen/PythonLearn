import os

# print('++++++++++读取部分内容++++++++++')
#
# file = open('./test.txt', 'r', encoding='utf-8')
# print(file.read(3))
# file.close()
#
# print('++++++++++二进制模式++++++++++')
# file = open('./test.txt', 'rb')
# print(file.read())
# file.close()
#
# print('++++++++++逐行读取++++++++++')
# file = open('./test.txt', 'r', encoding='utf-8')
# for c in file:
#     print(c)
# file.close()
#
# print('++++++++++分批读取++++++++++')
# with open('./test.txt', 'r', encoding='utf-8') as f:
#     while True:
#         c = f.read(1)
#         if not c:
#             break
#         print(c)
#
# file_path = './test.txt'
# print('++++++++++追加模式写入++++++++++')
#
#
# def printContent(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         print(f.read())
#
#
# with open(file_path, 'a', encoding='utf-8') as f:
#     f.write("追加内容\r\n")
#
# printContent(file_path)
#
# print('++++++++++W模式写入++++++++++')
#
# with open('./test.txt', 'w', encoding='utf-8') as f:
#     f.write("追加内容\r\n")
#
# printContent(file_path)


# 删除文件
def removeTest(path):
    os.remove(path)


def renameTxt():
    os.rename('./test.txt', './abc.txt')


if __name__ == '__main__':
    removeTest('./abc.txt')
