from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def menuFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collMenu = models.Menus.objects(isDelete=False).skip( offset ).limit( items_per_page )

    menu = models.Menus.objects(isDelete=False).all()
 
    pagination = Pagination(page=page, total=menu.count(), search=search, record_name='menu', per_page=items_per_page)
    
    menuParent = models.Menus.objects(isDelete=False, menuParent=None).all()
    return render_template("user_management/menu/find.html", menu=collMenu, pagination=pagination, menuParent=menuParent)

def menuInsertOne():
    try:
        menuName = request.form.get("menuName")
        menuSerialNumber = request.form.get("menuSerialNumber")
        menuParent = request.form.get("menuParent")
        menuIcon = request.form.get("menuIcon")
        
        if menuParent == "":
            menuParent = None
        if menuIcon == "":
            menuIcon = None
            
        if menuParent:
            menuParent = ObjectId(menuParent)
        collMenu = models.Menus(
            menuName = menuName,
            menuSerialNumber = menuSerialNumber,
            menuParent = menuParent,
            menuIcon = menuIcon,
        )
        collMenu.save()
        flash('You were successfully insert data.')
        return redirect("/user_management/menu/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/user_management/menu/find")
    
# def accessUpdateOne():
#     try:
#         accessId = request.args["accessId"]
#         accessName = request.form.get("accessName")
#         models.Access.objects(id=ObjectId(accessId)).update(accessName=accessName)
#         flash('You were successfully update data.')
#         return redirect("/user_management/access/find")
#     except Exception as err:
#         print(err)
#         flash('You were failed update data.')
#         return redirect("/user_management/access/find")

# def accessDeleteOne():
#     try:
#         accessId = request.args["accessId"]
#         models.Access.objects(id=ObjectId(accessId)).update(isDelete=True)
#         flash('You were successfully delete data.')
#         return redirect("/user_management/access/find")
#     except Exception as err:
#         print(err)
#         flash('You were failed delete data.')
#         return redirect("/user_management/access/find")