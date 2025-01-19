from . import base_controller
from .user_controller import UserController
from .user_admin_controller import UserAdminController
from .adm_controller import AdminController
import sqlalchemy
from database import models

class InitController(base_controller.BaseController):

   def login(self, username, password, mode) -> UserController | UserAdminController | AdminController | bool:
         """Authenticate the user"""

         allow_modes = ["--d", "--m", "--a"]

         if mode not in allow_modes:
               return False
        
         model = models.User

         if mode == allow_modes[2]:
            model = models.Admin

         auth_user = self._db.execute(sqlalchemy.select(model).where(model.username == username, model.password == password)).fetchone()

         if not auth_user:
            return False

         match mode:
            case "--d":
               return UserController(auth_user)
            case "--m":
               return UserAdminController(auth_user)
            case "--a":
                 return AdminController(auth_user)