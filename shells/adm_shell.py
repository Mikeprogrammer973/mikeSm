from . import user_adm_shell

class AdminShell(user_adm_shell.UserAdmShell):
    
    def do_fill(self, args):
        """Fill the color_groups|color_numbers table.
            Syntax: fill <cg|cn> <init> <end>
        """

        try:
            model, init, end = str(args).split(' ')

            fill = self._controller.fill_cg
            if model == "cn":
                fill = self._controller.fill_cn

            done = fill(int(init), int(end))
            
            if not done:
                print("\nSomething went wrong...try again!\n")
        except Exception as e:
            print(f"\nError: {e}")

    def do_del(self, args):
        """Delete one or all groups or numbers from color_groups|color_numbers table.
            Syntaxes: del <cg|cn> * | del <cg|cn|--s> <color_group|color_number|store_code>
        """
        try:
            model, qtd = str(args).split(" ")

            delete = self._controller.del_cg
            if model == "cn":
                delete = self._controller.del_cn
            if model == "--s":
                delete = self._controller.del_store

            if qtd == "":
                raise Exception("Invalid syntax!")
            delete(qtd)
        except Exception as e:
            print(f"\nError: {e}\n")

    def do_show(self, args):
        """Display the required info.
            Syntax: show <required_info>
        """

        try:
            req = str(args).split(" ")

            match req[0]:
                case "cgs":
                    self._controller.display_cgs()
                case "cns":
                    self._controller.display_cns()
                case _:
                    raise Exception("Invalid syntax!")
        except Exception as e:
            print(f"\nError: {e}\n")

    def do_setSm(self, args):
        """Set the store manager.
            Syntax: setSm <user_code> <store_code>
        """

        try:
            user, store = str(args).split(" ")

            self._controller.set_store_manager(store, user)
        except Exception as e:
            print(f"\nError: {e}\n")

    def do_u2dS(self, args):
        """Update the store info.
            Syntax: u2dS <store_code> <--n|--c|--l|--e> <new_value>
        """

        try:
            store, key, value = str(args).split(" ")

            self._controller.store_up2dt_info((key, value), store)
        except Exception as e:
            print(f"\nError: {e}\n")

    def do_add(self, args):
        """Register a new store, user or color pallet.
            Syntaxes: add --s <name> <location> <code> <email> | add --sp <store_code>
        """
        try:
            model, *prms = str(args).split(" ")
            expt = Exception("Invalid syntax!")
            match model:
                case "--sp":
                    if len(prms) != 1:
                        raise expt
                    else:
                        self._controller.add_store_pallet(prms[0])
                case '--s':
                    if len(prms) != 4:
                        raise expt
                    else:
                        self._controller.add_store(*prms)
                case _:
                    raise expt
        except Exception as e:
            print(f"\nError: {e}\n")
