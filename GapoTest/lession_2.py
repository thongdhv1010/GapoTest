#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: nguyenthong
    Date Created: 9/29/20
"""

from src.apis.blueprint import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=19931, debug=True)
