class Login:
    def login(self, user):
        if self.inValid(user):
            if self.inCorrect(user):
                user.set_message('login')
                return True
        else:
            return False
    def inValid(self, user):
        if user.get_username() == "" and user.get_password() == "":
            user.set_message("name or password is  invalid")
            return False
        else:
            return True
    def inCorrect(self, user):
        if user.get_username() == "Amir" and user.get_password() == "pass":
            return True
        else:
            user.set_message("name or password is  correct")
            return False