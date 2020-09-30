#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: nguyenthong
    Date Created: 9/30/20
"""
from src.controller.check_paragraph_controller import Paragraph


def check_function(fun, expect):
    check = False
    if fun:
        check = True
    if check == expect:
        return 'passed'
    else:
        return fun


def test_check_paragraph():
    list_case = [
        {
            "input": {
                "pattern": "Bán hàng",
                "paragraph": "Bán hàng online"
            },
            "expected": True
        },
        {
            "input": {
                "pattern": "Đoạn",
                "paragraph": "Đoạn đường mà mình đã đi qua bao nhiêu ngày"
            },
            "expected": True
        },
        {
            "input": {
                "pattern": "Hasagi",
                "paragraph": "Dead is like the wind, always by my side"
            },
            "expected": False
        }
    ]
    i = 0
    for case in list_case:
        input = case.get('input')
        pattern = input.get('pattern')
        paragraph = input.get('paragraph')
        expected = case.get('expected')

        check_case = check_function(Paragraph.check_word(pattern, paragraph, 3), expected)
        print(i, ': ', check_case)
        i = i + 1


if __name__ == '__main__':
    test_check_paragraph()
