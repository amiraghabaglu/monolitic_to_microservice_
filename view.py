from flask import render_template_string # type: ignore

def show_items(items):
    template = """
    <h1>Items List</h1>
    <ul>
  
        <li>{{ items.get_fname() }} - ${{ items.get_lname() }}</li>
        <li>{{ items.get_gender() }} - ${{ items.get_parentage() }}</li>
        <li>{{ items.get_address() }}</li>
    
    </ul>
    """
    return render_template_string(template, items=items)
