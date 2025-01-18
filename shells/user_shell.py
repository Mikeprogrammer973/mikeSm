import cmd 

class UserShell(cmd.Cmd):
    intro = "Welcome to MIKESM, type 'help' or '?' to get a list of all the commands.\n"
    prompt= f"$__mikeSm__user> "

    def do_exit(self, arg):
        "End the session"
        return True

    def do_cls(self, arg):
        "Clear the console"
        print("\033c", end="")