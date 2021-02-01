# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/1 22:40
@Auth ： Zoey
@File ：test_demo.py
@Description：
"""

import pytest
import yaml


class TestDemo:
    # # 参数组合
    # @pytest.mark.parametrize("a", [1, 2, 3])
    # @pytest.mark.parametrize("b", [4, 5, 6])
    # def test_param(self, a, b):
    #     print(f'a = {a}, b = {b}')

    # 读取yaml文件内容
    with open("../datas/calc.yaml") as f:
        data = yaml.safe_load(f)["add"]
        datas = data["datas"]
        myid = data["myid"]
        print(datas, myid)
