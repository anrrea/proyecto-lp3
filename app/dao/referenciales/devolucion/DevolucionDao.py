# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class DevolucionDao:

    def getDevoluciones(self):

        devolucionSQL = """
        SELECT id, descripcion
        FROM  devoluciones
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(devolucionSQL)
            devoluciones = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': devolucion[0], 'descripcion': devolucion[1]} for devolucion in devoluciones]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las devoluciones: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getDevolucionById(self, id):

        devolucionSQL = """
        SELECT id, descripcion
        FROM devoluciones WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(devolucionSQL, (id,))
            devolucionEncontrada = cur.fetchone() # Obtener una sola fila
            if devolucionEncontrada:
                return {
                        "id": devolucionEncontrada[0],
                        "descripcion": devolucionEncontrada[1]
                    }  # Retornar los datos de la devolucion
            else:
                return None # Retornar None si no se encuentra la devolucion
        except Exception as e:
            app.logger.error(f"Error al obtener devolucion: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarDevolucion(self, descripcion):

        insertDevolucionSQL = """
        INSERT INTO devoluciones(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertDevolucionSQL, (descripcion,))
            devolucion_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return devolucion_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar devolucion: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateDevolucion(self, id, descripcion):

        updateDevolucionSQL = """
        UPDATE devoluciones
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateDevolucionSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar devolucion: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteDevolucion(self, id):

        updateDevolucionSQL = """
        DELETE FROM devoluciones
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateDevolucionSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar devolucion: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()