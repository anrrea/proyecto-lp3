# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class VentaDao:

    def getVentas(self):

        ventaSQL = """
        SELECT id, descripcion
        FROM ventas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ventaSQL)
            ventas = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': venta[0], 'descripcion': venta[1]} for venta in ventas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las ventas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getVentaById(self, id):

        ventaSQL = """
        SELECT id, descripcion
        FROM ventas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ventaSQL, (id,))
            ventaEncontrada = cur.fetchone() # Obtener una sola fila
            if ventaEncontrada:
                return {
                        "id": ventaEncontrada[0],
                        "descripcion": ventaEncontrada[1]
                    }  # Retornar los datos de la venta
            else:
                return None # Retornar None si no se encuentra la venta
        except Exception as e:
            app.logger.error(f"Error al obtener venta: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarVenta(self, descripcion):

        insertVentaSQL = """
        INSERT INTO ventas(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertVentaSQL, (descripcion,))
            venta_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return venta_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar venta: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateVenta(self, id, descripcion):

        updateVentaSQL = """
        UPDATE ventas
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateVentaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar venta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteVenta(self, id):

        updateVentaSQL = """
        DELETE FROM ventas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateVentaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar venta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()