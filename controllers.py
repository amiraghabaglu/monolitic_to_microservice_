from flask import Flask # type: ignore
from models import Item
from views import show_items

def setup_routes(app):
    @app.route("/")
    def index():
        items = Item.get_all_items()
        return show_items(items)
