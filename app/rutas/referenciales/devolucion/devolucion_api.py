from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.devolucion.DevolucionDao import DevolucionDao

devapi = Blueprint('devapi', __name__)

# Trae todas las devoluciones
@devapi.route('/devoluciones', methods=['GET'])
def getDevoluciones():
    devdao = DevolucionDao()

    try:
        devoluciones = devdao.getDevoluciones()

        return jsonify({
            'success': True,
            'data': devoluciones,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las devoluciones: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@devapi.route('/devoluciones/<int:devolucion_id>', methods=['GET'])
def getDevolucion(devolucion_id):
    devdao = DevolucionDao()

    try:
        devolucion = devdao.getDevolucionById(devolucion_id)

        if devolucion:
            return jsonify({
                'success': True,
                'data': devolucion,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la devolucion con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener devolucion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva devolucion
@devapi.route('/devoluciones', methods=['POST'])
def addDevolucion():
    data = request.get_json()
    devdao = DevolucionDao()

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
        devolucion_id = devdao.guardarDevolucion(descripcion)
        if devolucion_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': devolucion_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la devolucion. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar devolucion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@devapi.route('/devoluciones/<int:devolucion_id>', methods=['PUT'])
def updateDevolucion(devolucion_id):
    data = request.get_json()
    devdao = DevolucionDao()

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
        if devdao.updateDevolucion(devolucion_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': devolucion_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la devolucion con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar devolucion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@devapi.route('/devoluciones/<int:devolucion_id>', methods=['DELETE'])
def deleteDevolucion(devolucion_id):
    devdao = DevolucionDao()

    try:
        # Usar el retorno de eliminarDevolucion para determinar el éxito
        if devdao.deleteDevolucion(devolucion_id):
            return jsonify({
                'success': True,
                'mensaje': f'Devolucion con ID {devolucion_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la devolucion con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar devolucion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500