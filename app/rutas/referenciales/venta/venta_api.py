from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.venta.VentaDao import VentaDao

venapi = Blueprint('venapi', __name__)

# Trae todas las ventas
@venapi.route('/ventas', methods=['GET'])
def getVentas():
    vendao = VentaDao()

    try:
        ventas = vendao.getVentas()

        return jsonify({
            'success': True,
            'data': ventas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las ventas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@venapi.route('/ventas/<int:venta_id>', methods=['GET'])
def getVenta(venta_id):
    vendao = VentaDao()

    try:
        venta = vendao.getVentaById(venta_id)

        if venta:
            return jsonify({
                'success': True,
                'data': venta,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la venta con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener venta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva venta
@venapi.route('/ventas', methods=['POST'])
def addVenta():
    data = request.get_json()
    vendao = VentaDao()

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
        venta_id = vendao.guardarVenta(descripcion)
        if venta_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': venta_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la venta. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar venta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@venapi.route('/ventas/<int:venta_id>', methods=['PUT'])
def updateVenta(venta_id):
    data = request.get_json()
    vendao = VentaDao()

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
        if vendao.updateVenta(venta_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': venta_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la venta con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar venta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@venapi.route('/ventas/<int:venta_id>', methods=['DELETE'])
def deleteVenta(venta_id):
    vendao = VentaDao()

    try:
        # Usar el retorno de eliminarVenta para determinar el éxito
        if vendao.deleteVenta(venta_id):
            return jsonify({
                'success': True,
                'mensaje': f'Venta con ID {venta_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la venta con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar venta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500