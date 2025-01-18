import cmd

class BaseShell:
    def do_exit(self, args):
        "End the current session"
        return True
    
    def do_cls(self, args):
        "Clear the console"
        print("\033c", end="")