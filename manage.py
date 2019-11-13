#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 16:48
# @Author  : z.g
import os
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app.models import User, Project

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Project=Project)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
