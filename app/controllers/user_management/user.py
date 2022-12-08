from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId
from hashlib import sha256

def userFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collAccess = models.Users.objects(isDelete=False).skip( offset ).limit( items_per_page )

    access = models.Users.objects(isDelete=False).all()
 
    pagination = Pagination(page=page, total=access.count(), search=search, record_name='access', per_page=items_per_page)
    
    return render_template("user_management/user/find.html", access=collAccess, pagination=pagination)

def userInsertOne():
    try:
        userName = request.form.get("userName")
        userEmail = request.form.get("userEmail")
        userPassword = request.form.get("userPassword")
        userPhone = request.form.get("userPhone")
        collPermission = models.Users(
            userName = userName,
            userEmail = userEmail,
            userPassword = sha256((userPassword + "secret").encode("utf-8")).hexdigest(),
            userPhoneNumber = userPhone,
            userFirstName = "",
            userLastName = "",
        )
        collPermission.save()
        flash('You were successfully insert data.')
        return redirect("/user_management/user/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/user_management/user/find")