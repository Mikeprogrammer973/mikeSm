import cmd

class BaseShell(cmd.Cmd):
    intro = "\nWelcome to MIKESM, type 'help' or '?' to get a list of all the commands.\n"
    
    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.do_cls(self)

    def do_exit(self, args):
        "End the current session."
        return True
    
    def do_cls(self, args):
        "Clear the console."
        print("\033c", end="")