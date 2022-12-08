from .access import *
from .menu import *
from .unit import *
from .role import *
from .user_unit_role import *
from .unit_role import *
from .permission import *
from .user import *
from .menu_permission import *
from .permission_access import *
from .role_permission import *

def UserManagement():
    return render_template("user_management/index.html")