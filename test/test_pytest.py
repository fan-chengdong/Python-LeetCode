#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_pytest.py    
@Contact :   437918310@qq.com
@License :   (C)Copyright 2019-2020
@Modify Time      @Author           @Version    @Desciption
------------      -------           --------    -----------
2020-02-14 13:24   Fan Chengdong     1.0         None
'''
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

