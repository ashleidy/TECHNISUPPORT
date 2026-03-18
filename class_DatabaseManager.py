import sqlite3
import logging
from PyQt5.QtWidgets import QMessageBox


class DatabaseManager:
    def __init__(self, host, user, password, database):
        """
        Para SQLite solo se usa 'database' (ruta del archivo .db).
        host, user y password se ignoran (se mantienen por compatibilidad).
        """
        try:
            self.connection = sqlite3.connect(database)
            self.connection.row_factory = sqlite3.Row  # Permite acceso por nombre de columna
            self.cursor = self.connection.cursor()
            # Habilitar soporte de claves foráneas
            self.cursor.execute("PRAGMA foreign_keys = ON")
            # Crear tablas si no existen
            self._create_tables_if_not_exists()
        except sqlite3.Error as err:
            QMessageBox.critical(
                None,
                "Error de conexión",
                f"No se pudo conectar a la base de datos SQLite: {err}"
            )
            raise

    def _create_tables_if_not_exists(self):
        """Crea las tablas necesarias si no existen en la base de datos."""
        # Tabla Usuarios
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                id_Usuarios INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                cedula_nit TEXT NOT NULL UNIQUE,
                correo TEXT,
                telefono TEXT
            )
        """)
        # Tabla Hoja_vida_equipo (96 columnas sin incluir id)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Hoja_vida_equipo (
                id_Hoja_vida_equipo INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_ingreso TEXT,
                fecha_entrega TEXT,
                tipo TEXT,
                marca TEXT,
                modelo TEXT,
                numero_serie TEXT UNIQUE,
                main_board_marca TEXT,
                main_board_modelo TEXT,
                main_board_numero_serie TEXT,
                wifi_marca TEXT,
                wifi_modelo TEXT,
                wifi_numero_serie TEXT,
                teclado_marca TEXT,
                teclado_modelo TEXT,
                teclado_numero_serie TEXT,
                CPU1_marca TEXT,
                CPU1_modelo TEXT,
                CPU1_numero_serie TEXT,
                CPU2_marca TEXT,
                CPU2_modelo TEXT,
                CPU2_numero_serie TEXT,
                psu_marca TEXT,
                psu_modelo TEXT,
                psu_capacidad TEXT,
                pantalla_marca TEXT,
                pantalla_modelo TEXT,
                pantalla_capacidad TEXT,
                pantalla_numero_serie TEXT,
                bateria_marca TEXT,
                bateria_modelo TEXT,
                bateria_numero_serie TEXT,
                bateria_capacidad TEXT,
                ram1_marca TEXT,
                ram1_modelo TEXT,
                ram1_capacidad TEXT,
                ram1_numero_serie TEXT,
                ram2_marca TEXT,
                ram2_modelo TEXT,
                ram2_capacidad TEXT,
                ram2_numero_serie TEXT,
                ram3_marca TEXT,
                ram3_modelo TEXT,
                ram3_capacidad TEXT,
                ram3_numero_serie TEXT,
                ram4_marca TEXT,
                ram4_modelo TEXT,
                ram4_capacidad TEXT,
                ram4_numero_serie TEXT,
                Unidad_almacenamiento1_marca TEXT,
                Unidad_almacenamiento1_modelo TEXT,
                Unidad_almacenamiento1_capacidad TEXT,
                Unidad_almacenamiento1_numero_serie TEXT,
                Unidad_almacenamiento2_marca TEXT,
                Unidad_almacenamiento2_modelo TEXT,
                Unidad_almacenamiento2_capacidad TEXT,
                Unidad_almacenamiento2_numero_serie TEXT,
                Unidad_almacenamiento3_marca TEXT,
                Unidad_almacenamiento3_modelo TEXT,
                Unidad_almacenamiento3_capacidad TEXT,
                Unidad_almacenamiento3_numero_serie TEXT,
                Unidad_almacenamiento4_marca TEXT,
                Unidad_almacenamiento4_modelo TEXT,
                Unidad_almacenamiento4_capacidad TEXT,
                Unidad_almacenamiento4_numero_serie TEXT,
                Unidad_almacenamiento5_marca TEXT,
                Unidad_almacenamiento5_modelo TEXT,
                Unidad_almacenamiento5_capacidad TEXT,
                Unidad_almacenamiento5_numero_serie TEXT,
                Unidad_almacenamiento6_marca TEXT,
                Unidad_almacenamiento6_modelo TEXT,
                Unidad_almacenamiento6_capacidad TEXT,
                Unidad_almacenamiento6_numero_serie TEXT,
                Unidad_almacenamiento7_marca TEXT,
                Unidad_almacenamiento7_modelo TEXT,
                Unidad_almacenamiento7_capacidad TEXT,
                Unidad_almacenamiento7_numero_serie TEXT,
                Unidad_almacenamiento8_marca TEXT,
                Unidad_almacenamiento8_modelo TEXT,
                Unidad_almacenamiento8_capacidad TEXT,
                Unidad_almacenamiento8_numero_serie TEXT,
                GPU1_marca TEXT,
                GPU1_modelo TEXT,
                GPU1_capacidad TEXT,
                GPU1_numero_serie TEXT,
                GPU2_marca TEXT,
                GPU2_modelo TEXT,
                GPU2_capacidad TEXT,
                GPU2_numero_serie TEXT,
                Unidad_DVD1_marca TEXT,
                Unidad_DVD1_modelo TEXT,
                Unidad_DVD1_capacidad TEXT,
                Unidad_DVD1_numero_serie TEXT,
                Unidad_DVD2_marca TEXT,
                Unidad_DVD2_modelo TEXT,
                Unidad_DVD2_capacidad TEXT,
                Unidad_DVD2_numero_serie TEXT
            )
        """)
        # Tabla reporte_fallas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reporte_fallas (
                id_info INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cedula_nit TEXT NOT NULL,
                id_numero_serie TEXT NOT NULL,
                descripcion_falla TEXT,
                diagnostico TEXT,
                reparacion TEXT,
                Notas TEXT,
                FOREIGN KEY (id_cedula_nit) REFERENCES Usuarios(cedula_nit) ON DELETE CASCADE,
                FOREIGN KEY (id_numero_serie) REFERENCES Hoja_vida_equipo(numero_serie) ON DELETE CASCADE
            )
        """)
        self.connection.commit()

    # ------------------------------------------------------------
    # Métodos para tabla Usuarios
    # ------------------------------------------------------------
    def fetch_all(self):
        self.cursor.execute("SELECT * FROM Usuarios")
        return self.cursor.fetchall()

    def add_record(self, cliente, cedula_nit, correo, telefono):
        try:
            # Verificar si ya existe cliente o cédula
            self.cursor.execute(
                "SELECT COUNT(*) FROM Usuarios WHERE cliente = ? OR cedula_nit = ?",
                (cliente, cedula_nit)
            )
            result = self.cursor.fetchone()
            if result[0] > 0:
                return "El cliente o la cédula ya existen en la base de datos."

            # Insertar nuevo registro
            self.cursor.execute("""
                INSERT INTO Usuarios (cliente, cedula_nit, correo, telefono)
                VALUES (?, ?, ?, ?)
            """, (cliente, cedula_nit, correo, telefono))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            return str(e)

    def update_record(self, id_Usuarios, cliente, cedula_nit, correo, telefono):
        query = """
            UPDATE Usuarios
            SET cliente = ?, cedula_nit = ?, correo = ?, telefono = ?
            WHERE id_Usuarios = ?
        """
        self.cursor.execute(query, (cliente, cedula_nit, correo, telefono, id_Usuarios))
        self.connection.commit()

    def delete_record(self, id_Usuarios):
        try:
            # Obtener cédula del usuario
            self.cursor.execute(
                "SELECT cedula_nit FROM Usuarios WHERE id_Usuarios = ?",
                (id_Usuarios,)
            )
            result = self.cursor.fetchone()
            if not result:
                return {"success": False, "message": "No se encontró el usuario especificado"}

            cedula_nit = result[0]

            # Verificar si hay registros relacionados en reporte_fallas
            self.cursor.execute(
                "SELECT COUNT(*) FROM reporte_fallas WHERE id_cedula_nit = ?",
                (cedula_nit,)
            )
            count_fallas = self.cursor.fetchone()[0]
            if count_fallas > 0:
                return {
                    "success": False,
                    "message": "No se puede eliminar el usuario porque tiene registros relacionados en la tabla de reportes y fallas"
                }

            # Proceder con eliminación
            self.cursor.execute("DELETE FROM Usuarios WHERE id_Usuarios = ?", (id_Usuarios,))
            if self.cursor.rowcount == 0:
                return {"success": False, "message": "No se pudo eliminar el usuario"}

            self.connection.commit()
            return {"success": True, "message": "Usuario eliminado exitosamente"}
        except Exception as e:
            self.connection.rollback()
            return {"success": False, "message": f"Error al eliminar el usuario: {str(e)}"}

    def search_record(self, search_term):
        query = "SELECT * FROM Usuarios WHERE cliente LIKE ? OR cedula_nit LIKE ? OR correo LIKE ?"
        self.cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        return self.cursor.fetchall()

    def fetch_by_id(self, record_id):
        query = "SELECT * FROM Usuarios WHERE id_Usuarios = ?"
        self.cursor.execute(query, (record_id,))
        return self.cursor.fetchone()

    def refresh_data(self):
        try:
            self.cursor.execute("SELECT * FROM Usuarios")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener los datos: {str(e)}")
            return []

    # ------------------------------------------------------------
    # Métodos para tabla Hoja_vida_equipo
    # ------------------------------------------------------------
    def fetch_all_equipos(self):
        self.cursor.execute("SELECT * FROM Hoja_vida_equipo")
        return self.cursor.fetchall()

    def add_equipo(self,
                   fecha_ingreso, fecha_entrega, tipo, marca, modelo, numero_serie,
                   main_board_marca, main_board_modelo, main_board_numero_serie,
                   wifi_marca, wifi_modelo, wifi_numero_serie,
                   teclado_marca, teclado_modelo, teclado_numero_serie,
                   CPU1_marca, CPU1_modelo, CPU1_numero_serie,
                   CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                   psu_marca, psu_modelo, psu_capacidad,
                   pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                   bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                   ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie,
                   ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                   ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie,
                   ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                   Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo,
                   Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                   Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo,
                   Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                   Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo,
                   Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                   Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo,
                   Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                   Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo,
                   Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                   Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo,
                   Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                   Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo,
                   Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                   Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo,
                   Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                   GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie,
                   GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                   Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                   Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie):
        """
        Inserta un nuevo equipo en la tabla Hoja_vida_equipo.
        Recibe exactamente 96 parámetros (todas las columnas excepto id).
        """
        try:
            # Verificar si el número de serie ya existe
            self.cursor.execute(
                "SELECT COUNT(*) FROM Hoja_vida_equipo WHERE numero_serie = ?",
                (numero_serie,)
            )
            result = self.cursor.fetchone()
            if result[0] > 0:
                QMessageBox.warning(None, "Advertencia", "El número de serie ya existe en la base de datos.")
                return False

            # Construir la consulta con 96 placeholders
            columnas = """
                fecha_ingreso, fecha_entrega, tipo, marca, modelo, numero_serie,
                main_board_marca, main_board_modelo, main_board_numero_serie,
                wifi_marca, wifi_modelo, wifi_numero_serie,
                teclado_marca, teclado_modelo, teclado_numero_serie,
                CPU1_marca, CPU1_modelo, CPU1_numero_serie,
                CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                psu_marca, psu_modelo, psu_capacidad,
                pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie,
                ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie,
                ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo,
                Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo,
                Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo,
                Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo,
                Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo,
                Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo,
                Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo,
                Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo,
                Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie,
                GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie
            """
            placeholders = ','.join(['?'] * 96)
            query = f"INSERT INTO Hoja_vida_equipo ({columnas}) VALUES ({placeholders})"

            valores = (
                fecha_ingreso, fecha_entrega, tipo, marca, modelo, numero_serie,
                main_board_marca, main_board_modelo, main_board_numero_serie,
                wifi_marca, wifi_modelo, wifi_numero_serie,
                teclado_marca, teclado_modelo, teclado_numero_serie,
                CPU1_marca, CPU1_modelo, CPU1_numero_serie,
                CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                psu_marca, psu_modelo, psu_capacidad,
                pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie,
                ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie,
                ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo,
                Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo,
                Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo,
                Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo,
                Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo,
                Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo,
                Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo,
                Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo,
                Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie,
                GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie
            )

            # Verificar que la cantidad de valores sea 96
            if len(valores) != 96:
                raise ValueError(f"Número incorrecto de valores: se esperaban 96, se recibieron {len(valores)}")

            self.cursor.execute(query, valores)
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            return str(e)

    def update_equipo(self, id_Hoja_vida_equipo,
                      fecha_ingreso, fecha_entrega, tipo, marca, modelo, numero_serie,
                      main_board_marca, main_board_modelo, main_board_numero_serie,
                      wifi_marca, wifi_modelo, wifi_numero_serie,
                      teclado_marca, teclado_modelo, teclado_numero_serie,
                      CPU1_marca, CPU1_modelo, CPU1_numero_serie,
                      CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                      psu_marca, psu_modelo, psu_capacidad,
                      pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                      bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                      ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie,
                      ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                      ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie,
                      ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                      Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo,
                      Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                      Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo,
                      Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                      Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo,
                      Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                      Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo,
                      Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                      Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo,
                      Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                      Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo,
                      Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                      Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo,
                      Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                      Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo,
                      Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                      GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie,
                      GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                      Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                      Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie):
        try:
            asignaciones = """
                fecha_ingreso = ?, fecha_entrega = ?, tipo = ?, marca = ?, modelo = ?, numero_serie = ?,
                main_board_marca = ?, main_board_modelo = ?, main_board_numero_serie = ?,
                wifi_marca = ?, wifi_modelo = ?, wifi_numero_serie = ?,
                teclado_marca = ?, teclado_modelo = ?, teclado_numero_serie = ?,
                CPU1_marca = ?, CPU1_modelo = ?, CPU1_numero_serie = ?,
                CPU2_marca = ?, CPU2_modelo = ?, CPU2_numero_serie = ?,
                psu_marca = ?, psu_modelo = ?, psu_capacidad = ?,
                pantalla_marca = ?, pantalla_modelo = ?, pantalla_capacidad = ?, pantalla_numero_serie = ?,
                bateria_marca = ?, bateria_modelo = ?, bateria_numero_serie = ?, bateria_capacidad = ?,
                ram1_marca = ?, ram1_modelo = ?, ram1_capacidad = ?, ram1_numero_serie = ?,
                ram2_marca = ?, ram2_modelo = ?, ram2_capacidad = ?, ram2_numero_serie = ?,
                ram3_marca = ?, ram3_modelo = ?, ram3_capacidad = ?, ram3_numero_serie = ?,
                ram4_marca = ?, ram4_modelo = ?, ram4_capacidad = ?, ram4_numero_serie = ?,
                Unidad_almacenamiento1_marca = ?, Unidad_almacenamiento1_modelo = ?,
                Unidad_almacenamiento1_capacidad = ?, Unidad_almacenamiento1_numero_serie = ?,
                Unidad_almacenamiento2_marca = ?, Unidad_almacenamiento2_modelo = ?,
                Unidad_almacenamiento2_capacidad = ?, Unidad_almacenamiento2_numero_serie = ?,
                Unidad_almacenamiento3_marca = ?, Unidad_almacenamiento3_modelo = ?,
                Unidad_almacenamiento3_capacidad = ?, Unidad_almacenamiento3_numero_serie = ?,
                Unidad_almacenamiento4_marca = ?, Unidad_almacenamiento4_modelo = ?,
                Unidad_almacenamiento4_capacidad = ?, Unidad_almacenamiento4_numero_serie = ?,
                Unidad_almacenamiento5_marca = ?, Unidad_almacenamiento5_modelo = ?,
                Unidad_almacenamiento5_capacidad = ?, Unidad_almacenamiento5_numero_serie = ?,
                Unidad_almacenamiento6_marca = ?, Unidad_almacenamiento6_modelo = ?,
                Unidad_almacenamiento6_capacidad = ?, Unidad_almacenamiento6_numero_serie = ?,
                Unidad_almacenamiento7_marca = ?, Unidad_almacenamiento7_modelo = ?,
                Unidad_almacenamiento7_capacidad = ?, Unidad_almacenamiento7_numero_serie = ?,
                Unidad_almacenamiento8_marca = ?, Unidad_almacenamiento8_modelo = ?,
                Unidad_almacenamiento8_capacidad = ?, Unidad_almacenamiento8_numero_serie = ?,
                GPU1_marca = ?, GPU1_modelo = ?, GPU1_capacidad = ?, GPU1_numero_serie = ?,
                GPU2_marca = ?, GPU2_modelo = ?, GPU2_capacidad = ?, GPU2_numero_serie = ?,
                Unidad_DVD1_marca = ?, Unidad_DVD1_modelo = ?, Unidad_DVD1_capacidad = ?, Unidad_DVD1_numero_serie = ?,
                Unidad_DVD2_marca = ?, Unidad_DVD2_modelo = ?, Unidad_DVD2_capacidad = ?, Unidad_DVD2_numero_serie = ?
            """
            query = f"UPDATE Hoja_vida_equipo SET {asignaciones} WHERE id_Hoja_vida_equipo = ?"

            valores = (
                fecha_ingreso, fecha_entrega, tipo, marca, modelo, numero_serie,
                main_board_marca, main_board_modelo, main_board_numero_serie,
                wifi_marca, wifi_modelo, wifi_numero_serie,
                teclado_marca, teclado_modelo, teclado_numero_serie,
                CPU1_marca, CPU1_modelo, CPU1_numero_serie,
                CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                psu_marca, psu_modelo, psu_capacidad,
                pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie,
                ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie,
                ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo,
                Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo,
                Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo,
                Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo,
                Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo,
                Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo,
                Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo,
                Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo,
                Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie,
                GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie,
                id_Hoja_vida_equipo
            )

            if len(valores) != 97:  # 96 columnas + id
                raise ValueError(f"Número incorrecto de valores: se esperaban 97, se recibieron {len(valores)}")

            self.cursor.execute(query, valores)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e

    def delete_equipo(self, id_Hoja_vida_equipo):
        try:
            # Obtener número de serie
            self.cursor.execute(
                "SELECT numero_serie FROM Hoja_vida_equipo WHERE id_Hoja_vida_equipo = ?",
                (id_Hoja_vida_equipo,)
            )
            result = self.cursor.fetchone()
            if not result:
                return {"success": False, "message": "No se encontró el registro especificado"}

            numero_serie = result[0]

            # Verificar si hay registros relacionados en reporte_fallas
            self.cursor.execute(
                "SELECT COUNT(*) FROM reporte_fallas WHERE id_numero_serie = ?",
                (numero_serie,)
            )
            count_fallas = self.cursor.fetchone()[0]
            if count_fallas > 0:
                return {
                    "success": False,
                    "message": "No se puede eliminar el registro porque tiene registros relacionados en la tabla de reportes y fallas"
                }

            # Proceder con eliminación
            self.cursor.execute(
                "DELETE FROM Hoja_vida_equipo WHERE id_Hoja_vida_equipo = ?",
                (id_Hoja_vida_equipo,)
            )
            if self.cursor.rowcount == 0:
                return {"success": False, "message": "No se pudo eliminar el registro"}

            self.connection.commit()
            return {"success": True, "message": "Registro eliminado exitosamente"}
        except Exception as e:
            self.connection.rollback()
            return {"success": False, "message": f"Error al eliminar el registro: {str(e)}"}

    def refresh_data_equipo(self):
        try:
            self.cursor.execute("SELECT * FROM Hoja_vida_equipo")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener los datos: {str(e)}")
            return []

    def search_equipo(self, search_term):
        # Construir una condición WHERE que cubra muchos campos relevantes
        campos_busqueda = [
            "tipo", "marca", "modelo", "numero_serie",
            "main_board_marca", "main_board_modelo", "main_board_numero_serie",
            "wifi_marca", "wifi_modelo", "wifi_numero_serie",
            "teclado_marca", "teclado_modelo", "teclado_numero_serie",
            "CPU1_marca", "CPU1_modelo", "CPU1_numero_serie",
            "CPU2_marca", "CPU2_modelo", "CPU2_numero_serie",
            "psu_marca", "psu_modelo", "psu_capacidad",
            "pantalla_marca", "pantalla_modelo", "pantalla_capacidad", "pantalla_numero_serie",
            "bateria_marca", "bateria_modelo", "bateria_numero_serie", "bateria_capacidad",
            "ram1_marca", "ram1_modelo", "ram1_capacidad", "ram1_numero_serie",
            "ram2_marca", "ram2_modelo", "ram2_capacidad", "ram2_numero_serie",
            "ram3_marca", "ram3_modelo", "ram3_capacidad", "ram3_numero_serie",
            "ram4_marca", "ram4_modelo", "ram4_capacidad", "ram4_numero_serie",
            "Unidad_almacenamiento1_marca", "Unidad_almacenamiento1_modelo",
            "Unidad_almacenamiento1_capacidad", "Unidad_almacenamiento1_numero_serie",
            "Unidad_almacenamiento2_marca", "Unidad_almacenamiento2_modelo",
            "Unidad_almacenamiento2_capacidad", "Unidad_almacenamiento2_numero_serie",
            "Unidad_almacenamiento3_marca", "Unidad_almacenamiento3_modelo",
            "Unidad_almacenamiento3_capacidad", "Unidad_almacenamiento3_numero_serie",
            "Unidad_almacenamiento4_marca", "Unidad_almacenamiento4_modelo",
            "Unidad_almacenamiento4_capacidad", "Unidad_almacenamiento4_numero_serie",
            "Unidad_almacenamiento5_marca", "Unidad_almacenamiento5_modelo",
            "Unidad_almacenamiento5_capacidad", "Unidad_almacenamiento5_numero_serie",
            "Unidad_almacenamiento6_marca", "Unidad_almacenamiento6_modelo",
            "Unidad_almacenamiento6_capacidad", "Unidad_almacenamiento6_numero_serie",
            "Unidad_almacenamiento7_marca", "Unidad_almacenamiento7_modelo",
            "Unidad_almacenamiento7_capacidad", "Unidad_almacenamiento7_numero_serie",
            "Unidad_almacenamiento8_marca", "Unidad_almacenamiento8_modelo",
            "Unidad_almacenamiento8_capacidad", "Unidad_almacenamiento8_numero_serie",
            "GPU1_marca", "GPU1_modelo", "GPU1_capacidad", "GPU1_numero_serie",
            "GPU2_marca", "GPU2_modelo", "GPU2_capacidad", "GPU2_numero_serie",
            "Unidad_DVD1_marca", "Unidad_DVD1_modelo", "Unidad_DVD1_capacidad", "Unidad_DVD1_numero_serie",
            "Unidad_DVD2_marca", "Unidad_DVD2_modelo", "Unidad_DVD2_capacidad", "Unidad_DVD2_numero_serie"
        ]
        condiciones = " OR ".join([f"{campo} LIKE ?" for campo in campos_busqueda])
        query = f"SELECT * FROM Hoja_vida_equipo WHERE {condiciones}"
        params = (f"%{search_term}%",) * len(campos_busqueda)
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_by_id_equipo(self, record_id_equipo):
        query = "SELECT * FROM Hoja_vida_equipo WHERE id_Hoja_vida_equipo = ?"
        self.cursor.execute(query, (record_id_equipo,))
        return self.cursor.fetchone()

    # ------------------------------------------------------------
    # Métodos para tabla reporte_fallas
    # ------------------------------------------------------------
    def add_fallas(self, id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas):
        try:
            logging.info("Iniciando validación de datos...")

            # Validar si el usuario existe
            self.cursor.execute(
                "SELECT cedula_nit FROM Usuarios WHERE LOWER(cedula_nit) = LOWER(?)",
                (id_cedula_nit,)
            )
            usuario_existente = self.cursor.fetchone()
            if not usuario_existente:
                self.connection.rollback()
                raise ValueError(f"La cédula {id_cedula_nit} no existe en la base de datos.")

            # Validar si el equipo existe
            self.cursor.execute(
                "SELECT numero_serie FROM Hoja_vida_equipo WHERE LOWER(numero_serie) = LOWER(?)",
                (id_numero_serie,)
            )
            equipo_existente = self.cursor.fetchone()
            if not equipo_existente:
                self.connection.rollback()
                raise ValueError(f"El número de serie {id_numero_serie} no existe en la base de datos.")

            # Insertar registro de falla
            query = """
                INSERT INTO reporte_fallas
                (id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(query, (id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas))
            self.connection.commit()
            logging.info("Registro agregado correctamente.")

        except ValueError as e:
            logging.error(f"Error de validación: {e}")
            raise e
        except Exception as e:
            self.connection.rollback()
            logging.error(f"Error general: {e}")
            raise Exception(f"Error al agregar el registro: {str(e)}")

    def fetch_all_fallas(self):
        self.cursor.execute("SELECT * FROM reporte_fallas")
        return self.cursor.fetchall()

    def update_fallas(self, id_info, id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas):
        try:
            # Verificar si el registro existe
            self.cursor.execute("SELECT id_info FROM reporte_fallas WHERE id_info = ?", (id_info,))
            registro_existente = self.cursor.fetchone()
            if not registro_existente:
                raise ValueError(f"Error: No existe un registro con ID {id_info}.")

            # Verificar si la cédula existe
            self.cursor.execute(
                "SELECT cedula_nit FROM Usuarios WHERE LOWER(cedula_nit) = LOWER(?)",
                (id_cedula_nit,)
            )
            usuario_existente = self.cursor.fetchone()
            if not usuario_existente:
                raise ValueError(f"La cédula {id_cedula_nit} no existe en la base de datos.")

            # Verificar si el número de serie existe
            self.cursor.execute(
                "SELECT numero_serie FROM Hoja_vida_equipo WHERE LOWER(numero_serie) = LOWER(?)",
                (id_numero_serie,)
            )
            equipo_existente = self.cursor.fetchone()
            if not equipo_existente:
                raise ValueError(f"El número de serie {id_numero_serie} no existe en la base de datos.")

            # Actualizar registro
            query = """
                UPDATE reporte_fallas
                SET id_cedula_nit=?, id_numero_serie=?, descripcion_falla=?, diagnostico=?, reparacion=?, Notas=?
                WHERE id_info=?
            """
            self.cursor.execute(query, (
                id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas, id_info
            ))
            self.connection.commit()

        except ValueError as e:
            raise e
        except Exception as e:
            self.connection.rollback()
            raise Exception(f"Error al actualizar el registro: {str(e)}")

    def delete_fallas(self, id_info):
        try:
            # Verificar si el registro existe
            self.cursor.execute("SELECT id_info FROM reporte_fallas WHERE id_info = ?", (id_info,))
            if not self.cursor.fetchone():
                self.connection.rollback()
                return {"success": False, "message": f"Error: No existe un registro con id_info {id_info}."}

            # Eliminar el registro de reporte_fallas
            self.cursor.execute("DELETE FROM reporte_fallas WHERE id_info = ?", (id_info,))
            self.connection.commit()
            return {"success": True, "message": "Registro eliminado correctamente."}

        except Exception as e:
            self.connection.rollback()
            return {"success": False, "message": f"Error al eliminar el registro: {e}"}

    def search_fallas(self, search_term):
        query = """
            SELECT * FROM reporte_fallas
            WHERE id_cedula_nit LIKE ? OR id_numero_serie LIKE ? OR descripcion_falla LIKE ?
        """
        self.cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        return self.cursor.fetchall()

    def fetch_by_id_fallas(self, record_id):
        query = "SELECT * FROM reporte_fallas WHERE id_info = ?"
        self.cursor.execute(query, (record_id,))
        return self.cursor.fetchone()

    def delete_related_fallas(self, id_informacion_usuario):
        self.cursor.execute("DELETE FROM reporte_fallas WHERE id_info = ?", (id_informacion_usuario,))
        self.connection.commit()

    def delete_related_fallas_equipo(self, id_Hoja_vida_equipo):
        self.cursor.execute("DELETE FROM reporte_fallas WHERE id_Hoja_vida_equipo = ?", (id_Hoja_vida_equipo,))
        self.connection.commit()

    # ------------------------------------------------------------
    # Métodos auxiliares para combos (nuevos, necesarios para la interfaz)
    # ------------------------------------------------------------
    def fetch_cedulas_for_add(self):
        """Obtener cédulas/NITs que no están en reporte_fallas (para agregar nueva falla)."""
        self.cursor.execute("""
            SELECT cedula_nit 
            FROM Usuarios 
            WHERE cedula_nit NOT IN (SELECT id_cedula_nit FROM reporte_fallas)
        """)
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_all_cedulas(self):
        """Obtener todas las cédulas/NITs (para modo actualizar)."""
        self.cursor.execute("SELECT cedula_nit FROM Usuarios")
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_numeros_serie_for_add(self):
        """Obtener números de serie que no están en reporte_fallas (para agregar nueva falla)."""
        self.cursor.execute("""
            SELECT numero_serie 
            FROM Hoja_vida_equipo 
            WHERE numero_serie NOT IN (SELECT id_numero_serie FROM reporte_fallas)
        """)
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_all_numeros_serie(self):
        """Obtener todos los números de serie (para modo actualizar)."""
        self.cursor.execute("SELECT numero_serie FROM Hoja_vida_equipo")
        return [row[0] for row in self.cursor.fetchall()]

    # ------------------------------------------------------------
    # Métodos para búsqueda combinada (legado)
    # ------------------------------------------------------------
    def search_data(self, search_text):
        try:
            query = """
                SELECT
                    U.*,
                    H.*,
                    R.*
                FROM Usuarios U
                JOIN reporte_fallas R ON U.cedula_nit = R.id_cedula_nit
                JOIN Hoja_vida_equipo H ON R.id_numero_serie = H.numero_serie
            """
            if search_text:
                query += " WHERE U.cliente LIKE ? OR U.cedula_nit LIKE ?"
                self.cursor.execute(query, (f"%{search_text}%", f"%{search_text}%"))
            else:
                self.cursor.execute(query)

            results = self.cursor.fetchall()
            headers = [desc[0] for desc in self.cursor.description]
            return results, headers
        except Exception as e:
            return None, None

    def load_data(self):
        try:
            query = """
                SELECT
                    U.*,
                    H.*,
                    R.*
                FROM Usuarios U
                JOIN reporte_fallas R ON U.cedula_nit = R.id_cedula_nit
                JOIN Hoja_vida_equipo H ON R.id_numero_serie = H.numero_serie
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            headers = [desc[0] for desc in self.cursor.description]
            return results, headers
        except Exception as e:
            return None, None