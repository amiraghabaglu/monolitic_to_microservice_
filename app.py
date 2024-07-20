from flask import Flask # type: ignore
from controller import setup_routes

app = Flask(__name__)
setup_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
