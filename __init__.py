# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2017 by Alex Bodnaru
    :license: see LICENSE for details.
"""
from trytond.pool import Pool


def register():
    Pool.register(
        module='eds', type_='model'
    )
