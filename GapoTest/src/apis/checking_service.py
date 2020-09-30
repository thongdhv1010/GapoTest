#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: nguyenthong
    Date Created: 9/29/20
"""
from flask import Blueprint

from src.controller.check_paragraph_controller import Paragraph

checking_mod = Blueprint(__name__, __name__)


@checking_mod.route("/check_paragraph", methods=["POST"])
def check_paragraph():
    return Paragraph().check_paragraph()

@checking_mod.route("/define/word/bad", methods=["POST"])
def define_word_bad():
    return Paragraph().define_word_bad()

