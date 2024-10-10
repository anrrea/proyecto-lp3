from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.empleado.EmpleadoDao import EmpleadoDao

empapi = Blueprint('empapi', __name__)

# Trae todas las empleados
@empapi.route('/empleados', methods=['GET'])
def getEmpleados():
    empdao = EmpleadoDao()

    try:
        empleados = empdao.getEmpleados()

        return jsonify({
            'success': True,
            'data': empleados,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las empleados: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@empapi.route('/empleados/<int:empleado_id>', methods=['GET'])
def getEmpleado(empleado_id):
    empdao = EmpleadoDao()

    try:
        empleado = empdao.getEmpleadoById(empleado_id)

        if empleado:
            return jsonify({
                'success': True,
                'data': empleado,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la empleado con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo empleado
@empapi.route('/empleados', methods=['POST'])
def addEmpleado():
    data = request.get_json()
    empdao = EmpleadoDao()

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
        empleado_id = empdao.guardarEmpleado(descripcion)
        if empleado_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': empleado_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el empleado. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@empapi.route('/empleados/<int:empleado_id>', methods=['PUT'])
def updateEmpleado(empleado_id):
    data = request.get_json()
    empdao = EmpleadoDao()

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
        if empdao.updateEmpleado(empleado_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': empleado_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el empleado con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@empapi.route('/empleados/<int:empleado_id>', methods=['DELETE'])
def deleteEmpleado(empleado_id):
    empdao = EmpleadoDao()

    try:
        # Usar el retorno de eliminarEmpleado para determinar el éxito
        if empdao.deleteEmpleado(empleado_id):
            return jsonify({
                'success': True,
                'mensaje': f'Empleado con ID {empleado_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el empleado con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500