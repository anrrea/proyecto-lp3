from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.cliente.ClienteDao import ClienteDao

cliapi = Blueprint('cliapi', __name__)

# Trae todos los clientes
@cliapi.route('/clientes', methods=['GET'])
def getClientes():
    clidao = ClienteDao()

    try:
        clientes = clidao.getClientes()

        return jsonify({
            'success': True,
            'data': clientes,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las clientes: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cliapi.route('/clientes/<int:cliente_id>', methods=['GET'])
def getCliente(cliente_id):
    clidao = ClienteDao()

    try:
        cliente = clidao.getClienteById(cliente_id)

        if cliente:
            return jsonify({
                'success': True,
                'data': cliente,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el cliente con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener cliente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva cliente
@cliapi.route('/clientes', methods=['POST'])
def addCliente():
    data = request.get_json()
    clidao = ClienteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        descripcion = data['descripcion'].upper()
        cliente_id = clidao.guardarCliente(descripcion)
        if cliente_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': cliente_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el cliente. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar cliente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cliapi.route('/clientes/<int:cliente_id>', methods=['PUT'])
def updateCliente(cliente_id):
    data = request.get_json()
    clidao = ClienteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    descripcion = data['descripcion']
    try:
        if clidao.updateCliente(cliente_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': cliente_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el cliente con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar cliente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cliapi.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def deleteCliente(cliente_id):
    clidao = ClienteDao()

    try:
        # Usar el retorno de eliminarCliente para determinar el éxito
        if clidao.deleteCliente(cliente_id):
            return jsonify({
                'success': True,
                'mensaje': f'Cliente con ID {cliente_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el cliente con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar cliente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500