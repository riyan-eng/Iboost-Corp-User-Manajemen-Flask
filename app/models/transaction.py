from mongoengine import connect
from mongoengine import *
from datetime import datetime
from .user_management import Users, Units, UserUnitRoles

# connect(alias='db_transaction', db='db_transaction', host="localhost", port=27017)
connect(alias='db_transaction', db='transaction', host="localhost", port=27019)

class Budgets(Document):
    unitId = ReferenceField(Units, required=True)
    budgetDC = StringField(required=True)
    budgetAmount = DecimalField(required=True, min_value=0, precision=2)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'db_transaction'}

class PaymentStatus(Document):
    paymentStatusName = StringField(required=True, unique=True)
    paymentStatusCode = StringField(required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'db_transaction'}
    
class Mutations(Document):
    fromUserUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    toUserUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    mutationAmount = DecimalField(required=True, min_value=0, precision=2)
    mutationNote = StringField()
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'db_transaction'}
    
class Wallets(Document):
    walletDC = StringField(required=True)
    walletAmount = DecimalField(required=True, min_value=0, precision=2)
    userUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    mutationId = ReferenceField(Mutations, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'db_transaction'}