from . import user_admin_controller
import sqlalchemy
from database import models

class AdminController(user_admin_controller.UserAdminController):
   
   def fill_cg(self, init, end):
      groups = ["A", "B", "C", "D"]

      if init >= end or init < 0 or end < 0 or init >= len(groups) or end >= len(groups):
         return False
      
      if not self._db.clear_table(models.ColorGroup):
         return False

      try:
         for i in range(init, (end + 1)):
            self._db.execute(sqlalchemy.insert(models.ColorGroup).values(name=groups[i]))
      except Exception as e:
         print(f"\nError: {e}\n")
         return False
      
      return True
   
   def fill_cn(self, init, end):
      if init >= end or init < 0 or end < 0:
         return False
      
      if not self._db.clear_table(models.ColorNumber):
         return False
      
      try:
         for i in range(init, (end + 1)):
            self._db.execute(sqlalchemy.insert(models.ColorNumber).values(code=i))
      except Exception as e:
         print(f"\nError: {e}\n")
         return False
      
      return True

   def del_cg(self, qtd):
      if qtd == "*":
         self._db.clear_table(models.ColorGroup)
      else:
         self._db.execute(sqlalchemy.delete(models.ColorGroup).where(models.ColorGroup.name == qtd))
      return True
   
   def del_cn(self, qtd):
      if qtd == "*":
         self._db.clear_table(models.ColorNumber)
      else:
         self._db.execute(sqlalchemy.delete(models.ColorNumber).where(models.ColorNumber.code == int(qtd)))

      return True
   
   def display_cgs(self):
      cgs = self._db.execute(sqlalchemy.select(models.ColorGroup)).fetchall()

      print("\nCOLOR GROUPS\n")
      for cg in cgs:
         print(cg[0].name)
      if len(cgs) == 0:
         print("Empty")
      print("\n")

   def display_cns(self):
      cns = self._db.execute(sqlalchemy.select(models.ColorNumber)).fetchall()

      print("\nCOLOR NUMBERS\n")
      for cn in cns:
         print(cn[0].code)
      if len(cns) == 0:
         print("Empty")
      print("\n")

   def add_store(self, name, location, code, email):
      if self._db.execute(sqlalchemy.select(models.Store).where(models.Store.code == code)).fetchone():
         raise Exception("Store <code> already in use...choose another one!")
      else:
         data = {
            "code": code,
            "name": name,
            "location": location,
            "email": email
         }
         return self._db.execute(sqlalchemy.insert(models.Store).values(**data))

   def del_store(self, store_code):
      return self._db.execute(sqlalchemy.delete(models.Store).where(models.Store.code == store_code))

   def set_store_manager(self, store_code, manager_code):
      store = self._db._session.query(models.Store).filter_by(code=store_code).first()

      if store:
         manager = self._db._session.query(models.User).filter_by(code=manager_code).first()
         
         if manager:
            store.manager = manager.code
         else:
            raise Exception("Invalid <user_code>!")
         
         self._db._session.commit()
      else:
         raise Exception("Invalid <store_code>!")

   def store_up2dt_info(self, info: tuple, store_code):
      store = self._db._session.query(models.Store).filter_by(code=store_code).first()

      if store:
         match info[0]:
            case "--n":
               if hasattr(store, "name"):
                  store.name = info[1]
            case "--c":
               if hasattr(store, "code"):
                  store.code = info[1]
            case "--l":
               if hasattr(store, "location"):
                  store.location = info[1]
            case "--e":
               if hasattr(store, "email"):
                  store.email = info[1]
            case _:
               raise Exception("Invalid <key>!")
         self._db._session.commit()
      else:
         raise Exception("Invalid <store_code>!")

   def add_store_pallet(self, store):
      pass