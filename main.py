# import cmd
# from user.manager import User
# from database.manager import Database

# class AppShell(cmd.Cmd):
#     intro = "Welcome to MIKESM, type 'help' or '?' to get a list of all the commands.\n"
#     user = "not_user"
#     prompt= f"$__mikeSm__{user}> "

#     def __init__(self, completekey = "tab", stdin = None, stdout = None):
#         super().__init__(completekey, stdin, stdout)
#         self.user_manager = User()

#     def do_auth(self, args):
#         "Authenticate with an existent user. Syntax: auth <username> <password>"
#         try:
#             username, password = str(args).split(' ')
#             self.user_manager.login(username, password)
#         except Exception as e:
#             print(f"Error {e}: The corect syntax is 'auth <username> <password>' ")

#     def do_exit(self, arg):
#         "End the app."
#         print("Logging out...")
#         return True
    
#     def default(self, line):
#         return super().default(line)
    
#     def do_help(self, arg):
#         return super().do_help(arg)
    
#     def do_cls(self, arg):
#         print("\033c", end="")
    

# if __name__ == "__main__":
#     AppShell().cmdloop()
# db = Database()
import os
from database.manager import Database

db = Database()

# print(db.create_test_u())

os.system("cls")
os.system("pause")