# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/1 21:14
@Auth ： Zoey
@File ：test_calc.py
@Description：
"""

import pytest
import yaml

from python_code.calc import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator()
        print("【开始计算】")

    def teardown(self):
        print("【结束计算】")

    # 参数化
    # @pytest.mark.parametrize(
    #     "a, b, expect",
    #     [
    #         (1, 1, 2),
    #         (0.1, 0.1, 0.2),
    #         (-1, -1, -2),
    #         (0.1, 0.2, 0.3)
    #     ], ids=['int', 'float', 'negative', 'round']
    # )

    # 读取yaml文件内容进行参数化操作
    @pytest.mark.parametrize(
        "a, b, expect",
        yaml.safe_load(open("../datas/calc.yaml"))["add"]["datas"],
        ids=yaml.safe_load(open("../datas/calc.yaml"))["add"]["myid"]
    )
    def test_add(self, a, b, expect):
        # 调用add方法
        result = self.calc.add(a, b)
        # 判断 result是浮点数，做出保留2位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，需要写断言
        assert result == expect

    @pytest.mark.parametrize(
        "a, b, expect",
        yaml.safe_load(open("../datas/calc.yaml"))["div"]["datas"],
        ids=yaml.safe_load(open("../datas/calc.yaml"))["div"]["myid"]
    )
    def test_div(self, a, b, expect):
        # 调用div方法
        if expect == "error":
            raise Exception("除数不能为0")
        else:
            result = self.calc.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)
            assert result == expect
