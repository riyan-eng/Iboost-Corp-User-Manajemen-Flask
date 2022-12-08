from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def rolePermissionFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collAccess = models.RolePermissions.objects(isDelete=False).skip( offset ).limit( items_per_page )

    access = models.RolePermissions.objects(isDelete=False).all()
 
    pagination = Pagination(page=page, total=access.count(), search=search, record_name='access', per_page=items_per_page)
    
    permission = models.Permissions.objects()
    role = models.Roles.objects()
    return render_template("user_management/role_permission/find.html", access=collAccess, pagination=pagination, permission=permission, role=role)

def rolePermissionInsertOne():
    try:
        permissionId = request.form.get("permissionId")
        roleId = request.form.get("roleId")
        collPermission = models.RolePermissions(
            permissionId = permissionId,
            roleId = roleId,
        )
        collPermission.save()
        flash('You were successfully insert data.')
        return redirect("/user_management/role_permission/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/user_management/role_permission/find")