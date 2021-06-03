class Authenticate:
    def __init__(self):
        self.username = ""
        self.role = ""

    def login(self, username, role):
        print("login")
        self.username = username
        self.role = role

    def logout(self):
        print("logout")
        self.username = ""
        self.role = ""

    def checkAuthen(self):
        if len(self.username) > 0:
            return self.role
        else:
            return False


authen = Authenticate()
