"""
检索指定路径下后缀是 py 的所有文件
"""

import os
import os.path

ls = []


def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.') + 1:].upper() == "PY":
                ls.append(pathTmp)
    except PermissionError:
        pass


def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path):
            break

    getAppointFile(path, ls)
    print(ls)
    print(len(ls))


main()
