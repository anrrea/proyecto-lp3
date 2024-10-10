from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.caja.CajaDao import CajaDao

cajapi = Blueprint('cajapi', __name__)

# Trae todas las cajas
@cajapi.route('/cajas', methods=['GET'])
def getCajas():
    cajdao = CajaDao()

    try:
        cajas = cajdao.getCajas()

        return jsonify({
            'success': True,
            'data': cajas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las cajas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cajapi.route('/cajas/<int:caja_id>', methods=['GET'])
def getCaja(caja_id):
    cajdao = CajaDao()

    try:
        caja = cajdao.getCajaById(caja_id)

        if caja:
            return jsonify({
                'success': True,
                'data': caja,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la caja con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva caja
@cajapi.route('/cajas', methods=['POST'])
def addCaja():
    data = request.get_json()
    cajdao = CajaDao()

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
        caja_id = cajdao.guardarCaja(descripcion)
        if caja_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': caja_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la caja. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cajapi.route('/cajas/<int:caja_id>', methods=['PUT'])
def updateCaja(caja_id):
    data = request.get_json()
    cajdao = CajaDao()

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
        if cajdao.updateCaja(caja_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': caja_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la caja con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cajapi.route('/cajas/<int:caja_id>', methods=['DELETE'])
def deleteCaja(caja_id):
    cajdao = CajaDao()

    try:
        # Usar el retorno de eliminarCaja para determinar el éxito
        if cajdao.deleteCaja(caja_id):
            return jsonify({
                'success': True,
                'mensaje': f'Caja con ID {caja_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la caja con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500