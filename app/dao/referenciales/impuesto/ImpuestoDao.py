# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ImpuestoDao:

    def getImpuestos(self):

        impuestoSQL = """
        SELECT id, descripcion
        FROM impuestos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(impuestoSQL)
            impuestos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': impuesto[0], 'descripcion': impuesto[1]} for impuesto in impuestos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las impuestos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getImpuestoById(self, id):

        impuestoSQL = """
        SELECT id, descripcion
        FROM impuestos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(impuestoSQL, (id,))
            impuestoEncontrada = cur.fetchone() # Obtener una sola fila
            if impuestoEncontrada:
                return {
                        "id": impuestoEncontrada[0],
                        "descripcion": impuestoEncontrada[1]
                    }  # Retornar los datos de el impuesto
            else:
                return None # Retornar None si no se encuentra el impuesto
        except Exception as e:
            app.logger.error(f"Error al obtener impuesto: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarImpuesto(self, descripcion):

        insertImpuestoSQL = """
        INSERT INTO impuestos(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertImpuestoSQL, (descripcion,))
            impuesto_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return impuesto_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar impuesto: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateImpuesto(self, id, descripcion):

        updateImpuestoSQL = """
        UPDATE impuestos
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateImpuestoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar impuesto: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteImpuesto(self, id):

        updateImpuestoSQL = """
        DELETE FROM impuestos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateImpuestoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar impuesto: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()