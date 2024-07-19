from flask import render_template_string # type: ignore

def show_items(items):
    template = """
    <h1>Items List</h1>
    <ul>
    {% for item in items %}
        <li>{{ item.name }} - ${{ item.price }}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(template, items=items)
