# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/3 23:42
@Auth ： Zoey
@File ：test_calculator.py
@Description：计算器测试用例
"""

import yaml
import pytest
import allure


with open("../datas/calc.yaml") as f:
    datas = yaml.safe_load(f)["datas"]
    add_datas = datas["add_datas"]  # 读取加法数据
    sub_datas = datas["sub_datas"]  # 读取减法数据
    mul_datas = datas["mul_datas"]  # 读取乘法数据
    div_datas = datas["div_datas"]  # 读取除法数据
    myid = datas["myid"]    # 读取myid
    f.close()


# 获取加法数据
@pytest.fixture(params=add_datas, ids=myid)
def get_add_data(request):
    data = request.param
    yield data

# 获取减法数据
@pytest.fixture(params=sub_datas, ids=myid)
def get_sub_data(request):
    data = request.param
    yield data

# 获取乘法数据
@pytest.fixture(params=mul_datas, ids=myid)
def get_mul_data(request):
    data = request.param
    yield data

# 获取除法数据
@pytest.fixture(params=div_datas, ids=myid)
def get_div_data(request):
    data = request.param
    yield data


@allure.feature("计算器测试用例")
class TestCalculator:
    # 加法测试用例
    @pytest.mark.run(order=1)
    @allure.story("加法测试用例")
    def test_add(self, get_calc, get_add_data, out_message):
        with allure.step("执行加法操作"):
            result = get_calc.add(get_add_data[0], get_add_data[1])
        with allure.step("判断计算结果类型，如果是float则保留2位小数"):
            if isinstance(result, float):
                result = round(result, 2)
        assert result == get_add_data[2]

    # 除法测试用例
    @pytest.mark.run(order=4)
    @allure.story("除法测试用例")
    def test_div(self, get_calc, get_div_data, out_message):
        try:
            with allure.step("执行除法"):
                result = get_calc.div(get_div_data[0], get_div_data[1])
        except:
            with allure.step("当除数为0时，发生异常并输出【除数不能为0】"):
                print("除数不能为0")
        else:
            with allure.step("判断计算结果类型，如果是float则保留2位小数"):
                if isinstance(result, float):
                    result = round(result, 2)
            assert result == get_div_data[2]

    # 减法测试用例
    @pytest.mark.run(order=2)
    @allure.story("减法测试用例")
    def test_sub(self, get_calc, get_sub_data, out_message):
        with allure.step("执行减法"):
            result = get_calc.sub(get_sub_data[0], get_sub_data[1])
        with allure.step("判断计算结果类型，如果是float则保留2位小数"):
            if isinstance(result, float):
                result = round(result, 2)
        assert result == get_sub_data[2]

    # 乘法测试用例
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul_data, out_message):
        with allure.step("执行乘法"):
            result = get_calc.mul(get_mul_data[0], get_mul_data[1])
        with allure.step("判断计算结果类型，如果是float则保留2位小数"):
            if isinstance(result, float):
                result = round(result, 2)
        assert result == get_mul_data[2]


