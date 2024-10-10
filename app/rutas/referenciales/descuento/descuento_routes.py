from flask import Blueprint, render_template

desmod = Blueprint('descuento', __name__, template_folder='templates')

@desmod.route('/descuento-index')
def descuentoIndex():
    return render_template('descuento-index.html')