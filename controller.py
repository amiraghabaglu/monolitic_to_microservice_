#controller
class AccountController:
    def login(self, user):
        if self.inValid(user):
            if self.inCorrect(user):
                user.setMess('login')
                return True
            else:
                
                return False
    def inValid(self, user):
        if user.getName() == "" and user.getPass() == "":
            user.setMess("name or password is  invalid")
            return False
        else:
            return True
    def inCorrect(self, user):
        if user.getName() == "Amir" and user.getPass() == "Amir@031":
            return True
        else:
            user.setMess("name or password is  correct")
            return False
