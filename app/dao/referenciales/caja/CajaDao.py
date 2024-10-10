# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CajaDao:

    def getCajas(self):

        cajaSQL = """
        SELECT id, descripcion
        FROM cajas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cajaSQL)
            cajas = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': caja[0], 'descripcion': caja[1]} for caja in cajas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las cajas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getCajaById(self, id):

        cajaSQL = """
        SELECT id, descripcion
        FROM cajas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cajaSQL, (id,))
            cajaEncontrada = cur.fetchone() # Obtener una sola fila
            if cajaEncontrada:
                return {
                        "id": cajaEncontrada[0],
                        "descripcion": cajaEncontrada[1]
                    }  # Retornar los datos de la caja
            else:
                return None # Retornar None si no se encuentra la caja
        except Exception as e:
            app.logger.error(f"Error al obtener caja: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarCaja(self, descripcion):

        insertCajaSQL = """
        INSERT INTO cajas(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCajaSQL, (descripcion,))
            caja_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return caja_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar caja: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateCaja(self, id, descripcion):

        updateCajaSQL = """
        UPDATE cajas
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCajaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar caja: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteCaja(self, id):

        updateCajaSQL = """
        DELETE FROM cajas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCajaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar caja: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()