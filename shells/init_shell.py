from shells.user_shell import UserShell
from shells.user_adm_shell import UserAdmShell
from shells.adm_shell import AdminShell
from shells.base_shell import BaseShell
from controllers.init_controller import InitController

class InitShell(BaseShell):
    prompt= f"$__mikeSm__> "

    def do_auth(self, args):
        """Authenticate the user.
            Syntax: auth <username> <password> <--d|--m|--a>
        """
        try:
            username, password, mode = str(args).split(' ')
            auth = InitController().login(username, password, mode)

            if(auth):
                match(mode):
                    case "--d":
                        UserShell(auth).cmdloop()
                    case "--m":
                        UserAdmShell(auth).cmdloop()
                    case "--a":
                        AdminShell(auth).cmdloop()
            else:
                print("\nInvalid username, password or mode!\n")
        except Exception as e:
            print(f"Error {e}")
