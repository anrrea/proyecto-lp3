from flask import Blueprint, render_template

depmod = Blueprint('deposito', __name__, template_folder='templates')

@depmod.route('/deposito-index')
def depositoIndex():
    return render_template('deposito-index.html')