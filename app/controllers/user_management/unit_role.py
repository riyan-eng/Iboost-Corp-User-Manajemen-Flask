from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def unitRoleFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collMenu = models.UnitRoles.objects(isDelete=False).skip( offset ).limit( items_per_page )

    menu = models.UnitRoles.objects(isDelete=False).all()
    role = models.Roles.objects(isDelete=False)
    unit = models.Units.objects(isDelete=False)
    pagination = Pagination(page=page, total=menu.count(), search=search, record_name='menu', per_page=items_per_page)
    
    return render_template("user_management/unit_role/find.html", menu=collMenu, pagination=pagination, role=role, unit=unit)

def unitRoleInsertOne():
    try:
        roleId = request.form.get("roleId")
        unitId = request.form.get("unitId")
        collUnitRole = models.UnitRoles(
            roleId = ObjectId(roleId),
            unitId = ObjectId(unitId),
        )
        collUnitRole.save()
        # print(roleId)
        # print(unitId)
        flash('You were successfully insert data.')
        return redirect("/user_management/unit_role/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/user_management/unit_role/find")