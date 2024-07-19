#view 
from controller import AccountController
from model import User

u = Users()
ac = AccountController()

u.setName(input("username"))
u.setPass(input("password"))
ac.login(u)
print(u.getMess())
