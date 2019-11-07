#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 16:43
# @Author  : z.g

from flask import request, jsonify, render_template
from . import api


@api.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error', 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@api.app_errorhandler(500)
def internal_server_error(e):
    pass
