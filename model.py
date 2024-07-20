class User:
    def __init__(self) -> None:
        self.__username = ''
        self.__password = ''
        self.__message  = ''

    # Getter Accessores
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def get_message(self):
        return self.__message
    
    # Setter Accessores
    def set_username(self, param):
        self.__username = param
    def set_password(self, param):
        self.__password = param
    def set_message(self, param):
        self.__message = param

