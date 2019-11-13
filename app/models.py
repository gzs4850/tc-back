#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 16:20
# @Author  : z.g

from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(64))
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    def to_json(self):
        json_user = {
            'username': self.username,
            'last_seen': self.last_seen
        }
        return json_user


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pro_name = db.Column(db.String(128), unique=True)
    pro_desc = db.Column(db.String(db.Text))
    status = db.Column(db.Boolean)
    create_time = db.Column(db.DateTime(), default=datetime.utcnow)

