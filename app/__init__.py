from flask import Flask 

app = Flask (__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.pais.pais_routes import paismod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod
from app.rutas.referenciales.producto.producto_routes import promod
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.proveedor.proveedor_routes import provmod
from app.rutas.referenciales.cliente.cliente_routes import climod
from app.rutas.referenciales.sucursal.sucursal_routes import sucmod
from app.rutas.referenciales.deposito.deposito_routes import depomod
from app.rutas.referenciales.estado_civil.estado_civil_routes import estmod
from app.rutas.referenciales.sexo.sexo_routes import sexomod
from app.rutas.referenciales.marca.marca_routes import marcmod
from app.rutas.referenciales.tipo_producto.tipo_producto_routes import tipprodmod
 
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')

app.register_blueprint(paismod, url_prefix=f'{modulo0}/pais')

app.register_blueprint(nacmod, url_prefix=f'{modulo0}/nacionalidad')

app.register_blueprint(promod, url_prefix=f'{modulo0}/producto')

app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')

app.register_blueprint(provmod, url_prefix=f'{modulo0}/proveedor')

app.register_blueprint(climod, url_prefix=f'{modulo0}/cliente')

app.register_blueprint(sucmod, url_prefix=f'{modulo0}/sucursal')

app.register_blueprint(depomod, url_prefix=f'{modulo0}/deposito')

app.register_blueprint(estmod, url_prefix=f'{modulo0}/estado_civil')

app.register_blueprint(sexomod, url_prefix=f'{modulo0}/sexo')

app.register_blueprint(marcmod, url_prefix=f'{modulo0}/marca')

app.register_blueprint(tipprodmod, url_prefix=f'{modulo0}/tipo_producto')


from app.rutas.referenciales.ciudad.ciudad_api import ciuapi

from app.rutas.referenciales.pais.pais_api import paiapi

from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacapi

from app.rutas.referenciales.producto.producto_api import proapi

from app.rutas.referenciales.persona.persona_api import perapi

from app.rutas.referenciales.proveedor.proveedor_api import provapi

from app.rutas.referenciales.cliente.cliente_api import cliapi

from app.rutas.referenciales.sucursal.sucursal_api import sucapi

from app.rutas.referenciales.deposito.deposito_api import depoapi

from app.rutas.referenciales.estado_civil.estado_civil_api import estadocivilapi

from app.rutas.referenciales.sexo.sexo_api import sexoapi

from app.rutas.referenciales.marca.marca_api import marcaapi

from app.rutas.referenciales.tipo_producto.tipo_producto_api import tipo_producto_api

version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

app.register_blueprint(paiapi, url_prefix=version1)

app.register_blueprint(nacapi, url_prefix=version1)

app.register_blueprint(proapi, url_prefix=version1)

app.register_blueprint(perapi, url_prefix=version1)

app.register_blueprint(provapi, url_prefix=version1)

app.register_blueprint(cliapi, url_prefix=version1)

app.register_blueprint(sucapi, url_prefix=version1)

app.register_blueprint(depoapi, url_prefix=version1)

app.register_blueprint(estadocivilapi, url_prefix=version1)

app.register_blueprint(sexoapi, url_prefix=version1)

app.register_blueprint(marcaapi, url_prefix=version1)

app.register_blueprint(tipo_producto_api, url_prefix=version1)