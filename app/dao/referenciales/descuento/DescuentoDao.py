# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class DescuentoDao:

    def getDescuentos(self):

        descuentoSQL = """
        SELECT id, descripcion
        FROM descuentos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(descuentoSQL)
            descuentos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': descuento[0], 'descripcion': descuento[1]} for descuento in descuentos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las descuentos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getDescuentoById(self, id):

        descuentoSQL = """
        SELECT id, descripcion
        FROM descuentos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(descuentoSQL, (id,))
            descuentoEncontrada = cur.fetchone() # Obtener una sola fila
            if descuentoEncontrada:
                return {
                        "id": descuentoEncontrada[0],
                        "descripcion": descuentoEncontrada[1]
                    }  # Retornar los datos de la descuento
            else:
                return None # Retornar None si no se encuentra la descuento
        except Exception as e:
            app.logger.error(f"Error al obtener descuento: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarDescuento(self, descripcion):

        insertDescuentoSQL = """
        INSERT INTO descuentos(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertDescuentoSQL, (descripcion,))
            descuento_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return descuento_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar descuento: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateDescuento(self, id, descripcion):

        updateDescuentoSQL = """
        UPDATE descuentos
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateDescuentoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar descuento: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteDescuento(self, id):

        updateDescuentoSQL = """
        DELETE FROM descuentos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateDescuentoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar descuento: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()