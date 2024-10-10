# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CategoriaDao:

    def getCategorias(self):

        categoriaSQL = """
        SELECT id, descripcion
        FROM categorias
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(categoriaSQL)
            categorias = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': categoria[0], 'descripcion': categoria[1]} for categoria in categorias]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las categorias: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getCategoriaById(self, id):

        categoriaSQL = """
        SELECT id, descripcion
        FROM categorias WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(categoriaSQL, (id,))
            categoriaEncontrada = cur.fetchone() # Obtener una sola fila
            if categoriaEncontrada:
                return {
                        "id": categoriaEncontrada[0],
                        "descripcion": categoriaEncontrada[1]
                    }  # Retornar los datos de la categoria
            else:
                return None # Retornar None si no se encuentra la categoria
        except Exception as e:
            app.logger.error(f"Error al obtener categoria: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarCategoria(self, descripcion):

        insertCategoriaSQL = """
        INSERT INTO categorias(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCategoriaSQL, (descripcion,))
            categoria_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return categoria_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar categoria: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateCategoria(self, id, descripcion):

        updateCategoriaSQL = """
        UPDATE categorias
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCategoriaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar categoria: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteCategoria(self, id):

        updateCategoriaSQL = """
        DELETE FROM categorias
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCategoriaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar categoria: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()