from controllers.manager import User
from shells.init_shell import InitShell
from shells.user_shell import UserShell
from shells.user_adm_shell import UserAdmShell
from shells.adm_shell import AdminShell
from shells.base_shell import BaseShell

class InitShell(BaseShell):
    intro = "Welcome to MIKESM, type 'help' or '?' to get a list of all the commands.\n"
    prompt= f"$__mikeSm__> "

    def do_auth(self, args):
        """Authenticate the user
            Syntax: auth <username> <password> <mode>(--d | --m | --a)
        """
        try:
            username, password, mode = str(args).split(' ')
            auth = User().login(username, password, mode)

            if(auth):
                match(mode):
                    case "--d":
                        UserShell().cmdloop()
                    case "--m":
                        UserAdmShell().cmdloop()
                    case "--a":
                        AdminShell().cmdloop()
                # return True
            else:
                print("\nInvalid username or password!\n")
        except Exception as e:
            print(f"Error {e}")