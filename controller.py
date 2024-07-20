from model2 import Register
from view import show_items
from login import Login

def setup_routes(app):

    r = Register()

    r.set_address(input("Enter your address: "))
    r.set_fname(input("Enter your fname: "))
    r.set_lname(input("Enter your lname: "))
    r.set_gender(input("Enter your gender: "))
    r.set_username(input("Enter your username: "))
    r.set_password(input("Enter your password: "))
    r.set_parentage(input("Enter your parentage: "))

    l = Login()

  

    result = l.login(r)

    if result:
        print(r.get_message())
        @app.route("/")
        def index():
            return show_items(r)
    else:
        print(r.get_message()) 
    
