from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def accessFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collAccess = models.Access.objects(isDelete=False).skip( offset ).limit( items_per_page )

    access = models.Access.objects(isDelete=False).all()
 
    pagination = Pagination(page=page, total=access.count(), search=search, record_name='access', per_page=items_per_page)
    
    return render_template("user_management/access/find.html", access=collAccess, pagination=pagination)

def accessInsertOne():
    try:
        accessName = request.form.get("accessName")
        collAccess = models.Access(
            accessName = accessName
        )
        collAccess.save()
        flash('You were successfully insert data.')
        return redirect("/user_management/access/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/user_management/access/find")
    
def accessUpdateOne():
    try:
        accessId = request.args["accessId"]
        accessName = request.form.get("accessName")
        models.Access.objects(id=ObjectId(accessId)).update(accessName=accessName)
        flash('You were successfully update data.')
        return redirect("/user_management/access/find")
    except Exception as err:
        print(err)
        flash('You were failed update data.')
        return redirect("/user_management/access/find")

def accessDeleteOne():
    try:
        accessId = request.args["accessId"]
        models.Access.objects(id=ObjectId(accessId)).update(isDelete=True)
        flash('You were successfully delete data.')
        return redirect("/user_management/access/find")
    except Exception as err:
        print(err)
        flash('You were failed delete data.')
        return redirect("/user_management/access/find")