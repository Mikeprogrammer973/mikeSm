from database.manager import Database

class BaseController:
   def __init__(self):
      self._db = Database()

   def get_db(self):
      return self._db

   def __delete__(self):
      self.db.close()