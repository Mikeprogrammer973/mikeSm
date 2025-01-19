from shells.base_shell import BaseShell
from controllers.user_controller import UserController
from controllers.user_admin_controller import UserAdminController
from controllers.adm_controller import AdminController

class UserShell(BaseShell):

    def __init__(self, controller: UserController | UserAdminController | AdminController, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self._controller = controller
        self.prompt= f"$__mikeSm__{self._controller.get_logged_user().username}> "

        print(self.get_controller())

    def get_controller(self):
        return self._controller
