from model import User
class Register(User):
    __fname = ''
    __lname = ''
    __address = ''
    __gender = ''
    __parentage = ''
    
    # Getter Accessores
    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_address(self):
        return self.__address
    def get_gender(self):
        return self.__gender
    def get_parentage(self):
        return self.__parentage
        
    # Setter Accessores
    def set_fname(self, param):
        self.__fname = param
    def set_lname(self, param):
        self.__lname = param
    def set_address(self, param):
        self.__address = param
    def set_gender(self, param):
        self.__gender = param
    def set_parentage(self, param):
        self.__parentage = param