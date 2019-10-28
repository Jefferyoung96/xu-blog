#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
Created on 2019-10-24 15:46:05
@author: Xu Gaoliang
'''

import os

class Config(object):
    def __init__(self,root_name="xu-blog"):
        self.root_name = root_name 
        self.root = self.__get_root()

    def __get_root(self):
        p = os.path.dirname(__file__)
        i = p.rindex(self.root_name)
        return os.path.join(p[:i],self.root_name)

CF = Config()
