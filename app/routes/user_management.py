from app import app
from app.controllers import user_management

app.route("/user_management", methods=["GET"])(user_management.UserManagement)

app.route("/user_management/access/find",
          methods=["GET"])(user_management.accessFind)
app.route("/user_management/access/insertOne",
          methods=["POST"])(user_management.accessInsertOne)
app.route("/user_management/access/updateOne",
          methods=["POST"])(user_management.accessUpdateOne)
app.route("/user_management/access/deleteOne",
          methods=["GET"])(user_management.accessDeleteOne)

app.route("/user_management/menu/find",
          methods=["GET"])(user_management.menuFind)
app.route("/user_management/menu/insertOne",
          methods=["POST"])(user_management.menuInsertOne)

app.route("/user_management/unit/find",
          methods=["GET"])(user_management.unitFind)

app.route("/user_management/role/find",
          methods=["GET"])(user_management.roleFind)

app.route("/user_management/user_unit_role/find",
          methods=["GET"])(user_management.user_unit_roleFind)

app.route("/user_management/unit_role/find",
          methods=["GET"])(user_management.unitRoleFind)

app.route("/user_management/unit_role/insertOne",
          methods=["POST"])(user_management.unitRoleInsertOne)

app.route("/user_management/user_unit_role/insertOne",
          methods=["POST"])(user_management.user_unit_roleInsertOne)

app.route("/user_management/permission/find",
          methods=["GET"])(user_management.permissionFind)

app.route("/user_management/permission/insertOne",
          methods=["POST"])(user_management.permissionInsertOne)

app.route("/user_management/user/find",
          methods=["GET"])(user_management.userFind)

app.route("/user_management/user/insertOne",
          methods=["POST"])(user_management.userInsertOne)

app.route("/user_management/menu_permission/find",
          methods=["GET"])(user_management.menuPermissionFind)

app.route("/user_management/permission_access/find",
          methods=["GET"])(user_management.permissionAccessFind)

app.route("/user_management/permission_access/insertOne",
          methods=["POST"])(user_management.permissionAccessInsertOne)

app.route("/user_management/role_permission/find",
          methods=["GET"])(user_management.rolePermissionFind)

app.route("/user_management/role_permission/insertOne",
          methods=["POST"])(user_management.rolePermissionInsertOne)