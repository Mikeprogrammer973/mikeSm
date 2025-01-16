import cmd
from user.manager import User
import shells

class InitShell(cmd.Cmd):
    intro = "Welcome to MIKESM, type 'help' or '?' to get a list of all the commands.\n"
    prompt= f"$__mikeSm__> "

    def do_auth(self, args):
        """Authenticate the user
            Syntax: auth <username> <password> <mode>(--default | --manager | --admin)
        """
        try:
            username, password, mode = str(args).split(' ')
            auth = User().login(username, password, mode)

            if(auth):
                match(mode):
                    case "--default":
                        shells.user.UserShell().cmdloop()
                    case "--manager":
                        shells.user_adm.UserAdmShell().cmdloop()
                    case "--admin":
                        shells.admin.AdminShell().cmdloop()
                # return True
            else:
                print("\nInvalid username or password!\n")
        except Exception as e:
            print(f"Error {e}")

    def do_exit(self, arg):
        "End the app"
        return True

    def do_cls(self, arg):
        "Clear the console"
        print("\033c", end="")