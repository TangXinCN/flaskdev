#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, current_app
from . import main
#from .forms import NameForm
#from .. import db
#from ..models import User

#@main.route('/', methods=['GET', 'POST'])
#def index():
 #   form = NameForm()
  #  if form.validate_on_submit():
   #     user = User.query.filter_by(username=form.name.data).first()
    #    if user is None:
     #       user = User(username=form.name.data)
      #      db.session.add(user)
       #     session['known'] = False
        #else:
         #   session['known'] = True
       # session['name'] = form.name.data
        #return redirect(url_for('.index'))
    #return render_template('index.html',
     #                      form=form, name=session.get('name'),
      #                     known=session.get('known', False))

from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')