# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/4 21:07
@Auth ： Zoey
@File ：conftest.py
@Description：
"""

import pytest

from python_code.calc import Calculator


@pytest.fixture(scope="class")
def get_calc():
    """
    实例化Calculator
    :return: calc
    """
    calc = Calculator()
    return calc


# 用例执行前后输出【开始计算】和【计算结束】
@pytest.fixture(scope="module")
def out_message():
    print("开始计算")
    yield
    print("计算结束")
