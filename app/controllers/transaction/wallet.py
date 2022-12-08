from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def bubu(userUnitRoleId):
    collWalletCredit = models.Wallets.objects(
        userUnitRoleId = userUnitRoleId,
        isDelete=False).aggregate([
            { "$match": {"walletDC": "C"} },
            { "$group": { "_id": "$userUnitRoleId", "walletAmount": { "$sum": "$walletAmount" } } },

        ])
    credit = []
    countCredit = 0
    for d in collWalletCredit:
        credit.append(d["walletAmount"])
        countCredit += 1
    if countCredit == 0:
        credit = [0]
    
    
    collWalletDebit = models.Wallets.objects(
        userUnitRoleId = userUnitRoleId,
        isDelete=False).aggregate([
            { "$match": {"walletDC": "D"} },
            { "$group": { "_id": "$userUnitRoleId", "walletAmount": { "$sum": "$walletAmount" } } },

        ])
    debet = []
    countDebet = 0
    for d in collWalletDebit:
        debet.append(d["walletAmount"])
        countDebet += 1
    if countDebet == 0:
        debet = [0]
        
    balance = credit[0] - debet[0]
    return balance

def walletFind():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    items_per_page = 10

    offset = (page - 1) * items_per_page
    collbudget = models.Budgets.objects(isDelete=False).skip( offset ).limit( items_per_page )

    # budget = models.Budgets.objects(isDelete=False).all()
    budget = models.Units.objects(isDelete=False).all()

    pagination = Pagination(page=page, total=budget.count(), search=search, record_name='budget', per_page=items_per_page)
    
    unit = models.Units.objects(isDelete=False).skip( offset ).limit( items_per_page )
    
    user = models.UserUnitRoles.objects(isDelete=False).all()
    
    userUnitRole = models.UserUnitRoles.objects(isDelete=False)
    
    wallet = []
    for d in userUnitRole:
        wallet.append({
            "id": str(d.id),
            "userName": d.userId.userName,
            "walletAmount": bubu(d.id)
        })
    
    return render_template("transaction/wallet/find.html", budget=wallet, pagination=pagination, unit=unit, user=user)

def walletTransfer():
    try:
        # unitId = request.form.get("unitId")
        # budgetDC = "D"
        # collBudget = models.Budgets(
        #             unitId = ObjectId(unitId),
        #             budgetDC = budgetDC,
        #             budgetAmount = float(budgetAmount),
        #         )
        # collBudget.save()
        
        fromUserUnitRoleId = request.form.get("fromUserUnitRoleId")
        toUserUnitRoleId = request.form.get("phoneNumber")
        mutationAmount = request.form.get("mutationAmount")
        mutationNote = request.form.get("mutationNote")
        
        collUser = models.Users.objects(userPhoneNumber=toUserUnitRoleId).first()
        collUserUnitRole = models.UserUnitRoles.objects(userId=collUser).first()
        
        # print(collUserUnitRole)
        
        collMutation = models.Mutations(
            fromUserUnitRoleId=ObjectId(fromUserUnitRoleId),
            toUserUnitRoleId=collUserUnitRole,
            mutationAmount=float(mutationAmount),
            mutationNote=mutationNote
        )
        collMutation.save()
        
        collWalletPlus = models.Wallets(
            walletDC="C",
            walletAmount=float(mutationAmount),
            userUnitRoleId=collUserUnitRole,
            mutationId=collMutation
        )
        collWalletPlus.save()
        
        collWalletMin = models.Wallets(
            walletDC="D",
            walletAmount=float(mutationAmount),
            userUnitRoleId=ObjectId(fromUserUnitRoleId),
            mutationId=collMutation
        )
        collWalletMin.save()

        flash('You were successfully insert data.')
        return redirect("/transaction/wallet/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/transaction/wallet/find")