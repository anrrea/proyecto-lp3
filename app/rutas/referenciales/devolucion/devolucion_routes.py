from flask import Blueprint, render_template

devmod = Blueprint('devolucion', __name__, template_folder='templates')

@devmod.route('/devolucion-index')
def devolucionIndex():
    return render_template('devolucion-index.html')