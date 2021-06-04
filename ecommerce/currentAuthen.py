class Authenticate:
    def __init__(self):
        self.username = ""
        self.userId = ""
        self.personId = ""
        self.role = ""

    def login(self, username, role, userId, personId):
        print("login")
        self.username = username
        self.role = role
        self.userId = userId
        self.personId = personId

    def logout(self):
        print("logout")
        self.username = ""
        self.role = ""
        self.userId = ""
        # self.personId = ""

    def checkAuthen(self):
        if len(self.username) > 0:
            return self.role
        else:
            return False


authen = Authenticate()
