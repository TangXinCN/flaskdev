#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What id your name?', validators=[Required()])
    submit = SubmitField('Submit')