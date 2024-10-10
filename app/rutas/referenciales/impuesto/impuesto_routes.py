from flask import Blueprint, render_template

impmod = Blueprint('impuesto', __name__, template_folder='templates')

@impmod.route('/impuesto-index')
def impuestoIndex():
    return render_template('impuesto-index.html')