'''
@create_time: 2026/3/17 下午9:13
@Author: GeChao
@File: knowledge_base.py
'''

"""
知识库
"""
import os
import config_data as config
import hashlib

def check_md5(md5_str: str):
    """
    检查文件MD5
    return False(md5未处理过) True(已经处理过)
    """
    if not os.path.exists(config.md5_path):
        open(config.md5_path, 'w', encoding='utf-8').close()
        return False
    else:
        for line in open(config.md5_path, 'r', encoding='utf-8').readlines():
            line = line.strip()
            if line == md5_str:
                return True


def save_md5(md5_str: str):
    """
    保存文件MD5
    """
    with open(config.md5_path, 'a', encoding='utf-8') as f:
        f.write(md5_str + '\n')
    pass


def get_string_md5(input_str: str, encoding: str = 'utf-8'):
    """
    获取字符串MD5
    """
    str_bytes = input_str.encode(encoding=encoding)

    # 创建md5对象
    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    md5_hex = md5_obj.hexdigest()
    return md5_hex

class KnowledgeBaseService(object):
    def __init__(self):
        self.chroma = None  # 向量存储的实例 Chroma向量库对象
        self.spliter = None  # 文本分割器的对象

    def upload_by_str(self, data, filename):
        """将传入的字符串，进行向量化，存入向量数据库中"""
        pass

if __name__ == '__main__':
    r1 = get_string_md5("AI开发1")
    r2 = get_string_md5("AI开发1")
    r3 = get_string_md5("AI开发3")
    save_md5("747211adaeb43406bd69aa62ac04e017")

    print(check_md5("747211adaeb43406bd69aa62ac04e017"))
