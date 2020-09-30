#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: nguyenthong
    Date Created: 9/29/20
"""
from flask import Flask

from src.apis.checking_service import checking_mod

app = Flask(__name__)

app.register_blueprint(checking_mod)
