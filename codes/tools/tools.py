#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
Created on 2019-10-24 15:32:02
@author: Xu Gaoliang
'''

import os
from config import CF
import json

def get_item_md(file_path):
    _,file_type = os.path.splitext(file_path)
    _,file_name = os.path.split(file_path)

    name = file_name.replace(file_type,"")
    href = file_path.replace(CF.root,"")
    return "* [%s](%s)"%(name,href)

def get_md_obj(md_dir):
    g = os.walk(md_dir)
    obj = {}
    for dirpath,_,filenames in g:
        abs_dirpath = os.path.abspath(dirpath)
        rel_dirpath = abs_dirpath.replace(CF.root,"")
        if rel_dirpath not in obj:
            obj[rel_dirpath] = []
        for filename in filenames:
            filepath = os.path.join(abs_dirpath, filename)
            if filepath.endswith(".md"):
                obj[rel_dirpath].append(get_item_md(filepath))
        # if len(obj[rel_dirpath]) == 0:
        #     del obj[rel_dirpath]
    return obj

def get_md_txt(md_dir):
    txt = ""
    obj = get_md_obj(md_dir)
    for k,v in obj.items():
        arr = k.split("/")
        txt += "#"*(len(arr)-1) + " " + arr[-1] + "\n"
        for i in v:
            txt += i+"\n"
    return txt

def get_summary():
    txt = ""
    txt += get_md_txt("./docs/基础")
    txt += get_md_txt("./docs/python")
    txt += get_md_txt("./docs/机器学习")
    txt += get_md_txt("./docs/计算机视觉")
    txt += get_md_txt("./docs/自然语言处理")
    txt += get_md_txt("./docs/Markdown")
    txt += get_md_txt("./docs/LateX")
    txt += get_md_txt("./docs/其他")
    return txt

if __name__ == "__main__":
    print(get_summary())