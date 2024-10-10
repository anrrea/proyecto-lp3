from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.deposito.DepositoDao import DepositoDao

depapi = Blueprint('depapi', __name__)

# Trae todas las depositos
@depapi.route('/depositos', methods=['GET'])
def getDepositos():
    depdao = DepositoDao()

    try:
        depositos = depdao.getDepositos()

        return jsonify({
            'success': True,
            'data': depositos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las depositos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@depapi.route('/depositos/<int:deposito_id>', methods=['GET'])
def getDeposito(deposito_id):
    depdao = DepositoDao()

    try:
        deposito = depdao.getDepositoById(deposito_id)

        if deposito:
            return jsonify({
                'success': True,
                'data': deposito,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el deposito con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener deposito: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva deposito
@depapi.route('/depositos', methods=['POST'])
def addDeposito():
    data = request.get_json()
    depdao = DepositoDao()

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
        deposito_id = depdao.guardarDeposito(descripcion)
        if deposito_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': deposito_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el deposito. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar deposito: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@depapi.route('/depositos/<int:deposito_id>', methods=['PUT'])
def updateDeposito(deposito_id):
    data = request.get_json()
    depdao = DepositoDao()

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
        if depdao.updateDeposito(deposito_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': deposito_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el deposito con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar deposito: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@depapi.route('/depositos/<int:deposito_id>', methods=['DELETE'])
def deleteDeposito(deposito_id):
    depdao = DepositoDao()

    try:
        # Usar el retorno de eliminarDeposito para determinar el éxito
        if depdao.deleteDeposito(deposito_id):
            return jsonify({
                'success': True,
                'mensaje': f'Deposito con ID {deposito_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la deposito con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar : {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500