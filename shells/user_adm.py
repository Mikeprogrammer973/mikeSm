from . import user

class UserAdmShell(user.UserShell):
    intro = "Welcome to MIKESM, type 'help' or '?' to get a list of all the commands.\n"
    prompt= f"$__mikeSm__user_adm> "