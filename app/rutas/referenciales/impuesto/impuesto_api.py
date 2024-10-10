from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.impuesto.ImpuestoDao import ImpuestoDao

impapi = Blueprint('impapi', __name__)

# Trae todas las impuestos
@impapi.route('/impuestos', methods=['GET'])
def getImpuestos():
    impdao = ImpuestoDao()

    try:
        impuestos = impdao.getImpuestos()

        return jsonify({
            'success': True,
            'data': impuestos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los impuestos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@impapi.route('/impuestos/<int:impuesto_id>', methods=['GET'])
def getImpuesto(impuesto_id):
    impdao = ImpuestoDao()

    try:
        impuesto = impdao.getImpuestoById(impuesto_id)

        if impuesto:
            return jsonify({
                'success': True,
                'data': impuesto,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el impuesto con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo impuesto
@impapi.route('/impuestos', methods=['POST'])
def addImpuesto():
    data = request.get_json()
    impdao = ImpuestoDao()

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
        impuesto_id = impdao.guardarImpuesto(descripcion)
        if impuesto_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': impuesto_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el impuesto. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@impapi.route('/impuestos/<int:impuesto_id>', methods=['PUT'])
def updateImpuesto(impuesto_id):
    data = request.get_json()
    impdao = ImpuestoDao()

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
        if impdao.updateImpuesto(impuesto_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': impuesto_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el impuesto con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@impapi.route('/impuestos/<int:impuesto_id>', methods=['DELETE'])
def deleteImpuesto(impuesto_id):
    impdao = ImpuestoDao()

    try:
        # Usar el retorno de eliminarImpuesto para determinar el éxito
        if impdao.deleteImpuesto(impuesto_id):
            return jsonify({
                'success': True,
                'mensaje': f'Impuesto con ID {impuesto_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el impuesto con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500