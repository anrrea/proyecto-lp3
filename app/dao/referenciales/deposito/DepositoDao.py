# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class DepositoDao:

    def getDepositos(self):

        depositoSQL = """
        SELECT id, descripcion
        FROM depositos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(depositoSQL)
            depositos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': deposito[0], 'descripcion': deposito[1]} for deposito in depositos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las depositos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getDepositoById(self, id):

        depositoSQL = """
        SELECT id, descripcion
        FROM depositos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(depositoSQL, (id,))
            depositoEncontrada = cur.fetchone() # Obtener una sola fila
            if depositoEncontrada:
                return {
                        "id": depositoEncontrada[0],
                        "descripcion": depositoEncontrada[1]
                    }  # Retornar los datos de el deposito
            else:
                return None # Retornar None si no se encuentra el deposito
        except Exception as e:
            app.logger.error(f"Error al obtener deposito: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarDeposito(self, descripcion):

        insertDepositoSQL = """
        INSERT INTO depositos(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertDepositoSQL, (descripcion,))
            deposito_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return deposito_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar deposito: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateDeposito(self, id, descripcion):

        updateDepositoSQL = """
        UPDATE depositos
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateDepositoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar deposito: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteDeposito(self, id):

        updateDepositoSQL = """
        DELETE FROM depositos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateDepositoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar deposito: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()