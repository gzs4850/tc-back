#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 16:08
# @Author  : z.g

from flask import Blueprint

api = Blueprint('api', __name__)

from . import errors