from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.descuento.DescuentoDao import DescuentoDao

desapi = Blueprint('desapi', __name__)

# Trae todas las descuentos
@desapi.route('/descuentos', methods=['GET'])
def getDescuentos():
    desdao = DescuentoDao()

    try:
        descuentos = desdao.getDescuentos()

        return jsonify({
            'success': True,
            'data': descuentos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@desapi.route('/descuentos/<int:descuento_id>', methods=['GET'])
def getDescuento(descuento_id):
    desdao = DescuentoDao()

    try:
        descuento = desdao.getDescuentoById(descuento_id)

        if descuento:
            return jsonify({
                'success': True,
                'data': descuento,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el descuento con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva descuento
@desapi.route('/descuentos', methods=['POST'])
def addDescuento():
    data = request.get_json()
    desdao = DescuentoDao()

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
        descuento_id = desdao.guardarDescuento(descripcion)
        if descuento_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': descuento_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el descuento. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@desapi.route('/descuentos/<int:descuento_id>', methods=['PUT'])
def updateDescuento(descuento_id):
    data = request.get_json()
    desdao = DescuentoDao()

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
        if desdao.updateDescuento(descuento_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': descuento_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el descuento con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@desapi.route('/descuentos/<int:descuento_id>', methods=['DELETE'])
def deleteDescuento(descuento_id):
    desdao = DescuentoDao()

    try:
        # Usar el retorno de eliminarDescuento para determinar el éxito
        if desdao.deleteDescuento(descuento_id):
            return jsonify({
                'success': True,
                'mensaje': f'Descuento con ID {descuento_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el descuento con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500