#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: nguyenthong
    Date Created: 9/29/20
"""
import math as m


class Calculate():
    """
        Công ty cần xây dựng một hệ thống tính toán báo cáo động dựa trên dữ liệu thu thập được.
        Các số liệu của báo cáo được tính toán dựa trên công thức do người dùng chủ động nhập vào theo cú pháp có sẵn.
        Bạn cần implement hàm tính toán cho báo cáo dựa trên dữ liệu của công ty và công thức từ người dùng.
        Công thức chỉ cần hỗ trợ 4 phép tính cơ bản là cộng trừ nhân chia (và dấu ngoặc, optional)
    """

    def is_number_try_except(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def handle_result_data(self, number):
        if number % 1 == 0:
            number = m.ceil(number)

        return number

    def calc(self, math, data):
        math = math.replace(" ", "")
        point = ''
        while len(math) > 0:
            opt, math, type = self.sub_math(math)
            if type == 1:
                point = point + opt
            else:
                value = data.get(opt)
                if value is None:
                    check_number = self.is_number_try_except(opt)
                    if check_number:
                        value = opt
                    else:
                        raise ("The formula is not applicable to data")
                point += str(value)
        cal_point = eval(point)
        result = self.handle_result_data(cal_point)

        return result

    def sub_math(self, math):
        """
            Type: 1: Toán tử, 2: biến
        :param math:
        :return:
        """
        list_math = ['+', '-', '*', '/', '(', ')']
        i = 0
        k = 1
        point = ''
        math_temp = math
        if math[i] in list_math:
            while k <= len(math):
                if k < len(math):
                    if math_temp[k] not in list_math:
                        point = math[i:k]
                        math = math[k:len(math_temp)]
                        break
                    k += 1
                else:
                    point = math[i:k]
                    math = ''
            type = 1
        else:
            while k <= len(math):
                if k < len(math):
                    if math_temp[k] in list_math:
                        point = math[i:k]
                        math = math[k:len(math_temp)]
                        break
                    k += 1
                else:
                    point = math[i:k]
                    math = ''
            type = 2
        return point, math, type


if __name__ == '__main__':
    data = {
        "price": 100,
        "amount": 50,
        "discount": 0.5,
        "unit": 1000,
        "added_tax": 50000
    }
    list_math = [
        "price * amount * discount",
        "price * amount * discount + 1000",
        "price * amount * unit",
        "discount * 1000 + amount * price",
        "(price * amount + added_tax) * (1 - discount)",
        "(price * amount + added_tax) * (1 - discount) / unit"
    ]
    for math in list_math:
        print("Math: ", math)
        result = Calculate().calc(math, data)
        print("Result: ", result)
        print("\n")
