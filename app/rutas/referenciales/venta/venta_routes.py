from flask import Blueprint, render_template

venmod = Blueprint('venta', __name__, template_folder='templates')

@venmod.route('/venta-index')
def ventaIndex():
    return render_template('venta-index.html')