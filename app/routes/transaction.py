from app import app
from app.controllers import transaction

app.route("/transaction", methods=["GET"])(transaction.Transaction)

app.route("/transaction/budget/find",
          methods=["GET"])(transaction.budgetFind)

app.route("/transaction/budget/insertOne",
          methods=["POST"])(transaction.budgetInsertOne)

app.route("/transaction/budget/allocation",
          methods=["POST"])(transaction.budgetAllocation)

app.route("/transaction/wallet/find",
          methods=["GET"])(transaction.walletFind)

app.route("/transaction/wallet/transfer",
          methods=["POST"])(transaction.walletTransfer)