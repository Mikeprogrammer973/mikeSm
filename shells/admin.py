from . import user_adm

class AdminShell(user_adm.UserAdmShell):
    intro = "Welcome to MIKESM, type 'help' or '?' to get a list of all the commands.\n"
    prompt= f"$__mikeSm__admin> "