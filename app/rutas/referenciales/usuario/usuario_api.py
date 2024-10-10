from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.usuario.UsuarioDao import UsuarioDao

usuapi = Blueprint('usuapi', __name__)

# Trae todas las usuarios
@usuapi.route('/usuarios', methods=['GET'])
def getUsuarios():
    usudao = UsuarioDao()

    try:
        usuarios = usudao.getUsuarios()

        return jsonify({
            'success': True,
            'data': usuarios,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los usuarios: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@usuapi.route('/usuarios/<int:usuario_id>', methods=['GET'])
def getUsuario(usuario_id):
    usudao = UsuarioDao()

    try:
        usuario = usudao.getUsuarioById(usuario_id)

        if usuario:
            return jsonify({
                'success': True,
                'data': usuario,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el usuario con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva usuario
@usuapi.route('/usuarios', methods=['POST'])
def addUsuario():
    data = request.get_json()
    usudao = UsuarioDao()

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
        usuario_id = usudao.guardarUsuario(descripcion)
        if usuario_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': usuario_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el usuario. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@usuapi.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def updateUsuario(usuario_id):
    data = request.get_json()
    usudao = UsuarioDao()

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
        if usudao.updateUsuario(usuario_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': usuario_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró elusuario con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@usuapi.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def deleteUsuario(usuario_id):
    usudao = UsuarioDao()

    try:
        # Usar el retorno de eliminarUsuario para determinar el éxito
        if usudao.deleteUsuario(usuario_id):
            return jsonify({
                'success': True,
                'mensaje': f'Usuario con ID {usuario_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el usuario con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500