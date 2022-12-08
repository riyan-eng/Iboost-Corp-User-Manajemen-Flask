from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def unitFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collMenu = models.Units.objects(isDelete=False).skip( offset ).limit( items_per_page )

    menu = models.Units.objects(isDelete=False).all()
 
    pagination = Pagination(page=page, total=menu.count(), search=search, record_name='menu', per_page=items_per_page)
    
    return render_template("user_management/unit/find.html", menu=collMenu, pagination=pagination)
