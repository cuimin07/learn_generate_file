# -*- coding: utf-8 -*-

# @File    : generate_md.py
# @Date    : 2020-08-12
# @Author  : CuiMin

'''
open函数：'w' -> 写入，会覆盖;
         'r' -> 只读；
         'a' -> 打开追加，不会覆盖；
'''

def generate_md():
    with open('data.md', 'a', encoding='utf8') as f:
        f.write("### abc")


if __name__ == '__main__':
    generate_md()