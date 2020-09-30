#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: nguyenthong
    Date Created: 9/29/20
"""
from flask import request

from src.general.redis_config import RedisConfig

REDIS_KEY_WORD_BAD = 'WORD_BAD'


class Paragraph():

    def define_word_bad(self):
        """
            - Cấu hình danh sách các từ ngữ xấu
            - Lưu thông tin từ ngữ xấu xuống redis
        :return:
        """
        body = request.get_json()
        list_word = body.get('words_bad')
        if not list_word:
            raise ("Not config word bad")
        else:
            list_word_bad = ','.join(list_word)

        r = RedisConfig.get_redis()
        if body:
            r.set(REDIS_KEY_WORD_BAD, list_word_bad)

        return "DONE"

    def check_paragraph(self):
        body = request.get_json()
        paragraph = body.get('paragraph')

        r = RedisConfig.get_redis()
        word_bad = r.get(REDIS_KEY_WORD_BAD)
        decode_word_bad = word_bad.decode('utf-8')
        list_word_bad = decode_word_bad.split(',')

        result = []
        for word in list_word_bad:
            print("Word: ", word)
            check_word = Paragraph.check_word(word, paragraph, q=3)
            print("Check_word: ", check_word)
            if check_word:
                result.append({
                    "word_bad": word,
                    "location": check_word
                })

        return {
            "result": result
        }

    @staticmethod
    def check_word(pat, txt, q):
        d = 256
        M = len(pat)
        N = len(txt)
        j = 0
        p = 0  # Giá trị băm của mẫu
        t = 0  # Giá trị băm đoạn văn bản
        h = 1
        index_text = []
        if M > N:
            return index_text
        # Giá trị của h sẽ  "pow(d, M-1)% q"
        for i in range(M - 1):
            h = (h * d) % q

            # Tính toán giá trị băm
        for i in range(M):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q

        for i in range(N - M + 1):
            # Kiểm tra giá trị băm của đoạn văn bản và mẫu hiện tại
            # nếu các giá trị băm khớp nhau thì chỉ kiểm tra từng ký tự
            if p == t:
                # Kiểm tra từng ký tự 1
                for j in range(M):
                    if txt[i + j] != pat[j]:
                        break

                j += 1
                if j == M:
                    # print("Pattern found at index " + str(i))
                    index_text.append(i)

            # Tính giá trị băm cho đoạn văn bản tiếp theo
            if i < N - M:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

                if t < 0:
                    t = t + q

        return index_text
