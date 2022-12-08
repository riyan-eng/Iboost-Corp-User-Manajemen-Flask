from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def user_unit_roleFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collMenu = models.UserUnitRoles.objects(isDelete=False).skip( offset ).limit( items_per_page )

    menu = models.UserUnitRoles.objects(isDelete=False).all()
    
    user = models.Users.objects(isDelete=False)
    unitRole = models.UnitRoles.objects(isDelete=False)
    
    pagination = Pagination(page=page, total=menu.count(), search=search, record_name='menu', per_page=items_per_page)
    
    return render_template("user_management/user_unit_role/find.html", menu=collMenu, pagination=pagination, user= user, unitRole=unitRole)

def user_unit_roleInsertOne():
    try:
        userId = request.form.get("userId")
        unitRoleId = request.form.get("unitRoleId")
        collAccess = models.UserUnitRoles(
            userId = ObjectId(userId),
            unitRoleId = ObjectId(unitRoleId),
        )
        collAccess.save()
        flash('You were successfully insert data.')
        return redirect("/user_management/user_unit_role/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/user_management/user_unit_role/find")