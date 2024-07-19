#model
class Users:
    def __init__(self):
        self.name = ""
        self.pas = ""
        self.mess = ""

    def setName(self, uname):
        self.name = uname
    def setPass(self, passw):
        self.pas = passw
    def setMess(self, messa):
        self.mess = messa

    def getName(self):
        return self.name
    def getPass(self):
        return self.pas
    def getMess(self):
        return self.mess
