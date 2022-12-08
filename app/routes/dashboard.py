from app import app
from app.controllers import dashboard

app.route("/dashboard",
          methods=["GET"])(dashboard.Dashboard)