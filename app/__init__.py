from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.marca.marca_routes import marmod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.cliente.cliente_routes import climod
from app.rutas.referenciales.empleado.empleado_routes import empmod
from app.rutas.referenciales.sucursal.sucursal_routes import sucmod
from app.rutas.referenciales.impuesto.impuesto_routes import impmod
from app.rutas.referenciales.caja.caja_routes import cajmod
from app.rutas.referenciales.categoria.categoria_routes import catmod
from app.rutas.referenciales.deposito.deposito_routes import depmod
from app.rutas.referenciales.descuento.descuento_routes import desmod
from app.rutas.referenciales.usuario.usuario_routes import usumod
from app.rutas.referenciales.pedido.pedido_routes import pedmod
from app.rutas.referenciales.venta.venta_routes import venmod
from app.rutas.referenciales.devolucion.devolucion_routes import devmod


# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi


modulo0 = '/referenciales'
app.register_blueprint(marmod, url_prefix=f'{modulo0}/marca')

from app.rutas.referenciales.marca.marca_api import marapi


modulo0 = '/referenciales'
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')

from app.rutas.referenciales.pais.pais_api import paiapi


modulo0 = '/referenciales'
app.register_blueprint(climod, url_prefix=f'{modulo0}/cliente')

from app.rutas.referenciales.cliente.cliente_api import cliapi


modulo0 = '/referenciales'
app.register_blueprint(empmod, url_prefix=f'{modulo0}/empleado')

from app.rutas.referenciales.empleado.empleado_api import empapi


modulo0 = '/referenciales'
app.register_blueprint(sucmod, url_prefix=f'{modulo0}/sucursal')

from app.rutas.referenciales.sucursal.sucursal_api import sucapi


modulo0 = '/referenciales'
app.register_blueprint(impmod, url_prefix=f'{modulo0}/impuesto')

from app.rutas.referenciales.impuesto.impuesto_api import impapi


modulo0 = '/referenciales'
app.register_blueprint(cajmod, url_prefix=f'{modulo0}/caja')

from app.rutas.referenciales.caja.caja_api import cajapi


modulo0 = '/referenciales'
app.register_blueprint(catmod, url_prefix=f'{modulo0}/categoria')

from app.rutas.referenciales.categoria.categoria_api import catapi


modulo0 = '/referenciales'
app.register_blueprint(depmod, url_prefix=f'{modulo0}/deposito')

from app.rutas.referenciales.deposito.deposito_api import depapi


modulo0 = '/referenciales'
app.register_blueprint(desmod, url_prefix=f'{modulo0}/descuento')

from app.rutas.referenciales.descuento.descuento_api import desapi


modulo0 = '/referenciales'
app.register_blueprint(usumod, url_prefix=f'{modulo0}/usuario')

from app.rutas.referenciales.usuario.usuario_api import usuapi


modulo0 = '/referenciales'
app.register_blueprint(pedmod, url_prefix=f'{modulo0}/pedido')

from app.rutas.referenciales.pedido.pedido_api import pedapi


modulo0 = '/referenciales'
app.register_blueprint(venmod, url_prefix=f'{modulo0}/venta')

from app.rutas.referenciales.venta.venta_api import venapi


modulo0 = '/referenciales'
app.register_blueprint(devmod, url_prefix=f'{modulo0}/devolucion')

from app.rutas.referenciales.devolucion.devolucion_api import devapi


# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(marapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(paiapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(cliapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(empapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(sucapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(impapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(cajapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(catapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(depapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(desapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(usuapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(pedapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(venapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(devapi, url_prefix=version1)