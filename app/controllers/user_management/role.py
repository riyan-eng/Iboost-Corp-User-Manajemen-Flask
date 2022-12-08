from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def roleFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collrole = models.Roles.objects(isDelete=False).skip( offset ).limit( items_per_page )

    role = models.Roles.objects(isDelete=False).all()
 
    pagination = Pagination(page=page, total=role.count(), search=search, record_name='role', per_page=items_per_page)
    
    return render_template("user_management/role/find.html", role=collrole, pagination=pagination)