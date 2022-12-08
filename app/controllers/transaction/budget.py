from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from app import models
from flask_paginate import Pagination, get_page_parameter
from bson import ObjectId

def bubu(unitId):
    collBudgetCredit = models.Budgets.objects(
        unitId = unitId,
        isDelete=False).aggregate([
            { "$match": {"budgetDC": "C"} },
            { "$group": { "_id": "$unitId", "budgetAmount": { "$sum": "$budgetAmount" } } },

        ])
    credit = []
    countCredit = 0
    for d in collBudgetCredit:
        credit.append(d["budgetAmount"])
        countCredit += 1
    if countCredit == 0:
        credit = [0]
    
    
    collBudgetDebit = models.Budgets.objects(
        unitId = unitId,
        isDelete=False).aggregate([
            { "$match": {"budgetDC": "D"} },
            { "$group": { "_id": "$unitId", "budgetAmount": { "$sum": "$budgetAmount" } } },

        ])
    debet = []
    countDebet = 0
    for d in collBudgetDebit:
        debet.append(d["budgetAmount"])
        countDebet += 1
    if countDebet == 0:
        debet = [0]
        
    balance = credit[0] - debet[0]
    return balance

def budgetFind():
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
    
    unitBudget = []
    for d in unit:
        unitBudget.append({
            "unitId": str(d.id),
            "unitName": d.unitName,
            "budgetAmount": bubu(d.id)
        })
    
    return render_template("transaction/budget/find.html", budget=unitBudget, pagination=pagination, unit=unit, user=user)

def budgetInsertOne():
    try:
        positionDC = ["D", "C"]
        
        unitId = request.form.get("unitId")
        budgetDC = request.form.get("budgetDC")
        budgetAmount = request.form.get("budgetAmount")
        
        print(unitId)
        print(budgetDC)
        print(budgetAmount)
        if budgetDC in positionDC:
            collBudget = models.Budgets(
                unitId = ObjectId(unitId),
                budgetDC = budgetDC,
                budgetAmount = float(budgetAmount),
            )
            collBudget.save()
            flash('You were successfully insert data.')
            return redirect("/transaction/budget/find")
        
        flash('You were failed insert data.')
        return redirect("/transaction/budget/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/transaction/budget/find")
    
    
def budgetAllocation():
    try:
        unitId = request.form.get("unitId")
        budgetDC = "D"
        budgetAmount = request.form.get("budgetAmount")
        collBudget = models.Budgets(
                    unitId = ObjectId(unitId),
                    budgetDC = budgetDC,
                    budgetAmount = float(budgetAmount),
                )
        collBudget.save()
        
        fromUserUnitRoleId = request.form.get("fromUserUnitRoleId")
        toUserUnitRoleId = request.form.get("toUserUnitRoleId")
        mutationNote = request.form.get("mutationNote")
        
        collMutation = models.Mutations(
            fromUserUnitRoleId=ObjectId(fromUserUnitRoleId),
            toUserUnitRoleId=ObjectId(toUserUnitRoleId),
            mutationAmount=float(budgetAmount),
            mutationNote=mutationNote
        )
        collMutation.save()
        
        collWallet = models.Wallets(
            walletDC="C",
            walletAmount=float(budgetAmount),
            userUnitRoleId=ObjectId(toUserUnitRoleId),
            mutationId=collMutation
        )
        collWallet.save()

        flash('You were successfully insert data.')
        return redirect("/transaction/budget/find")
    except Exception as err:
        print(err)
        flash('You were failed insert data.')
        return redirect("/transaction/budget/find")