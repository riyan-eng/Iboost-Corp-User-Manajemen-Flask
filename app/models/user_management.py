from mongoengine import connect
from mongoengine import *
from datetime import datetime

# connect(alias='db_user_management', db='db_user_management', host="localhost", port=27017)
connect(alias='db_user_management', db='management', host="localhost", port=27019)

class Users(Document):
    userName = StringField(max_length=25, required=True, unique=True)
    userEmail = EmailField(required=True, unique=True)
    userPassword = StringField(required=True)
    userPin = StringField(required=True)
    userFirstName = StringField(max_length=25)
    userLastName = StringField(max_length=25)
    userPhoneNumber = StringField(max_length=15, required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField("self", null=True)
    createdBy = ReferenceField("self", null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}

class Units(Document):
    unitParent = ReferenceField("self", null=True)
    unitName = StringField(required=True, unique=True)
    unitEmail = StringField(required=True, unique=True)
    unitAddress = StringField(required=True)
    unitPhone = StringField(required=True, unique=True)
    unitContractAmount = DecimalField(null= True, min_value=0, precision=2)
    unitContractStart = DateField(null= True)
    unitContractEnd = DateField(null= True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class Roles(Document):
    roleName = StringField(max_length=25, required=True, unique=True)
    # roleCode = IntField(required=True, unique=True)
    unitId = ReferenceField(Units, null=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class Sessions(Document):
    userId = ReferenceField(Users, required=True)
    userAgent = StringField(required=True)
    refreshToken = StringField(required=True)
    roleId = ReferenceField(Roles, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class Permissions(Document):
    permissionName = StringField(required=True, unique=True)
    permissionServer = StringField(required=True)
    permissionPath = StringField(required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class Access(Document):
    accessName = StringField(required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class RolePermissions(Document):
    roleId = ReferenceField(Roles, required=True)
    permissionId = ReferenceField(Permissions, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}

class PermissionAccess(Document):
    permissionId = ReferenceField(Permissions, required=True)
    accessId = ReferenceField(Access, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class UnitRoles(Document):
    roleId = ReferenceField(Roles, required=True)
    unitId = ReferenceField(Units, null=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class UserUnitRoles(Document):
    userId = ReferenceField(Users, required=True)
    unitRoleId = ReferenceField(UnitRoles, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'db_user_management'}
    
class Menus(Document):
    menuName = StringField(required=True, unique=True)
    menuSerialNumber = IntField(required=True, unique=True)
    menuParent = ReferenceField("self", null=True)
    menuIcon = StringField(null=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'db_user_management'}
    
class MenuPermissions(Document):
    menuId = ReferenceField(Menus, required=True)
    permissionId = ReferenceField(Permissions, required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'db_user_management'}

# connect(alias='user-management-db', db='user-management-db')

# class Users(Document):
#     userId = StringField(required=True, unique=True)
#     userName = StringField(max_length=25, required=True, unique=True)
#     userEmail = EmailField(required=True, unique=True)
#     userPassword = StringField(required=True)
#     userFirstName = StringField(max_length=25)
#     userLastName = StringField(max_length=25)
#     userPhoneNumber = StringField(max_length=15, required=True, unique=True)
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}


# class Sessions(Document):
#     refreshToken = StringField(required=True)
#     user = ReferenceField(Users)
#     userRole = ListField(required=True)
#     userAgent = StringField(required=True)
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}


# class Roles(Document):
#     roleId = StringField(required=True, unique=True)
#     roleName = StringField(max_length=25, required=True, unique=True)
#     roleCode = IntField(required=True, unique=True)
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}


# class UserRoles(Document):
#     userRoleId = StringField(required=True, unique=True)
#     userId = ReferenceField(Users,
#                             required=True,
#                             unique=True,
#                             reverse_delete_rule=CASCADE)
#     roleId = ListField(ReferenceField(Roles, required=True))
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}


# class Permissions(Document):
#     permissionId = StringField(required=True, unique=True)
#     permissionName = StringField(required=True, unique=True)
#     permissionServer = StringField(required=True)
#     permissionPath = StringField(required=True, unique=True)
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}


# class Accesses(Document):
#     accessId = StringField(required=True, unique=True)
#     accessName = StringField(required=True, unique=True)
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}


# class RolePermissions(Document):
#     rolePermissionId = StringField(required=True, unique=True)
#     roleId = ReferenceField(Roles)
#     permissionId = ReferenceField(Permissions)
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}


# class permissionAccesses(Document):
#     permissionAccessId = StringField(required=True, unique=True)
#     permissionId = ReferenceField(Permissions)
#     accessId = ReferenceField(Accesses)
#     createdAt = DateTimeField(required=True, default=datetime.utcnow())
#     updatedAt = DateTimeField(required=True, default=datetime.utcnow())
#     isActive = BooleanField(required=True, default=True)
#     isDelete = BooleanField(required=True, default=False)

#     meta = {'db_alias': 'user-management-db'}