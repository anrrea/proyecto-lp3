from flask import Blueprint, render_template

marmod = Blueprint('marca', __name__, template_folder='templates')

@marmod.route('/marca-index')
def marcaIndex():
    return render_template('marca-index.html')