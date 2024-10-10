# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class UsuarioDao:

    def getUsuarios(self):

        usuarioSQL = """
        SELECT id, descripcion
        FROM usuarios
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(usuarioSQL)
            usuarios = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': usuario[0], 'descripcion': usuario[1]} for usuario in usuarios]

        except Exception as e:
            app.logger.error(f"Error al obtener todos los usuarios: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getUsuarioById(self, id):

        usuarioSQL = """
        SELECT id, descripcion
        FROM usuarios WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(usuarioSQL, (id,))
            usuarioEncontrada = cur.fetchone() # Obtener una sola fila
            if usuarioEncontrada:
                return {
                        "id": usuarioEncontrada[0],
                        "descripcion": usuarioEncontrada[1]
                    }  # Retornar los datos de el usuario
            else:
                return None # Retornar None si no se encuentra el usuario
        except Exception as e:
            app.logger.error(f"Error al obtener usuario: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarUsuario(self, descripcion):

        insertUsuarioSQL = """
        INSERT INTO usuarios(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertUsuarioSQL, (descripcion,))
            usuario_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return usuario_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar usuario: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateUsuario(self, id, descripcion):

        updateUsuarioSQL = """
        UPDATE usuarios
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateUsuarioSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar usuario: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteUsuario(self, id):

        updateUsuarioSQL = """
        DELETE FROM usuarios
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateUsuarioSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar usuario: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()