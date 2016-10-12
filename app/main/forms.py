#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, InputRequired, Length, Email, Regexp, ValidationError
from ..models import User, Role

class NameForm(Form):
    name = StringField('What id your name?', validators=[InputRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(Form):
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[InputRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                                                          0, 'Usernames must have only letters,'
                                                                                             'numbers, dots or underscores')])
    role = SelectField('Role', coerce=int)
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class PostForm(Form):
    body = TextAreaField("Write what you think now", validators=[InputRequired()])
    submit = SubmitField('Submit')