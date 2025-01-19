from . import base_controller
from database import models

class UserController(base_controller.BaseController):
   def __init__(self, userData: models.Admin | models.User):
      super().__init__()
      self._logged_user = userData[0]

   def get_logged_user(self) -> models.Admin | models.User :
      return self._logged_user
