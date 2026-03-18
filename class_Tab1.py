
import sys

# PyQt5 para la interfaz gráfica
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
    QInputDialog,
    QDialog,  
)

from class_InputWindow import InputWindow
from class_DatabaseManager import DatabaseManager


class Tab1(QWidget):
    
    def __init__(self, connection_data):
        super().__init__()
        self.db = DatabaseManager(**connection_data)  # Pasar los datos de conexión
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Gestión de Información de Usuarios")
        self.resize(800, 600)

        layout = QVBoxLayout(self)

        # Formulario de entrada de datos
        form_layout = QHBoxLayout()

        

        layout.addLayout(form_layout)

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Buscar...")
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_records)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "ID", "Cliente", "Cédula/NIT", "Correo", "Teléfono"
        ])
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f8f9fa; /* Fondo claro */
                border: 1px solid #ddd; /* Borde suave */
                border-radius: 5px;
                gridline-color: #ddd; /* Color de las líneas de la cuadrícula */
            }
            QHeaderView::section {
                background-color: #2E86C1; /* Azul oscuro para los encabezados */
                color: white;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border: none;
            }
            QTableWidget::item {
                padding: 8px;
                font-size: 14px;
                border-bottom: 1px solid #ddd; /* Línea divisoria entre filas */
            }
            QTableWidget::item:selected {
                background-color: #2E86C1; /* Azul oscuro para elementos seleccionados */
                color: white;
            }
        """)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Ajustar columnas al ancho
        layout.addWidget(self.table)

        # Buttons
        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.open_input_window)

        self.update_button = QPushButton("Actualizar")
        self.update_button.clicked.connect(self.update_record)

        
        self.eliminar_button = QPushButton("Eliminar")
        self.eliminar_button.clicked.connect(self.eliminar)

        # Estilos modernos para los botones (tonos de azul)
        button_style = """
            QPushButton {
                background-color: #2E86C1; /* Azul oscuro */
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #1B4F72; /* Azul más oscuro al pasar el mouse */
            }
            QPushButton:pressed {
                background-color: #154360; /* Azul aún más oscuro al presionar */
            }
        """
       
        
        self.add_button.setStyleSheet(button_style)
        self.update_button.setStyleSheet(button_style)
        self.eliminar_button.setStyleSheet(button_style)
        self.search_button.setStyleSheet(button_style)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.eliminar_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_data()


    def load_data(self):
        self.table.setRowCount(0)
        records = self.db.fetch_all()
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def open_input_window(self):
        try:
            self.input_window = InputWindow(mode="add")
            result = self.input_window.exec_()

            if result == QDialog.Accepted:
                cliente = self.input_window.cliente_input.text()
                cedula_nit = self.input_window.cedula_input.text()
                correo = self.input_window.correo_input.text()
                telefono = self.input_window.telefono_input.text()
                

                try:
                    self.add_record(cliente, cedula_nit, correo, telefono)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error al agregar el registro: {str(e)}")
            else:
                return

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir la ventana: {str(e)}")

    def add_record(self, cliente, cedula_nit, correo, telefono):
        try:
            result = self.db.add_record(cliente, cedula_nit, correo, telefono)
            if result is True:
                self.load_data()
                QMessageBox.information(self, "Éxito", "Registro agregado correctamente.")
            elif isinstance(result, str):  # Si es un mensaje de error
                QMessageBox.warning(self, "Advertencia", result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al agregar el registro: {str(e)}")

    def update_record(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "Selecciona un registro para actualizar.")
            return

        try:
            id_informacion_usuario = self.table.item(selected_row, 0).text()
            cliente = self.table.item(selected_row, 1).text()
            cedula_nit = self.table.item(selected_row, 2).text()
            correo = self.table.item(selected_row, 3).text()
            telefono = self.table.item(selected_row, 4).text()
            

            self.input_window = InputWindow(mode="update")
            self.input_window.cliente_input.setText(cliente)
            self.input_window.cedula_input.setText(cedula_nit)
            self.input_window.correo_input.setText(correo)
            self.input_window.telefono_input.setText(telefono)
          

            result = self.input_window.exec_()

            if result == QDialog.Accepted:
                cliente = self.input_window.cliente_input.text()
                cedula_nit = self.input_window.cedula_input.text()
                correo = self.input_window.correo_input.text()
                telefono = self.input_window.telefono_input.text()
               

                if not all([cliente, cedula_nit, correo, telefono]):
                    QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
                    return

                self.db.update_record(id_informacion_usuario, cliente, cedula_nit, correo, telefono)
                self.load_data()
                QMessageBox.information(self, "Éxito", "Registro actualizado correctamente.")
            else:
                QMessageBox.information(self, "Cancelado", "Actualización cancelada.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir la ventana o actualizar el registro: {e}")

        
   
             
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los datos: {str(e)}")
        
    def eliminar(self):
            selected_row = self.table.currentRow()

            if selected_row < 0:
                QMessageBox.warning(self, "Error", "Selecciona un registro para eliminar.")
                return

            id_Usuarios = self.table.item(selected_row, 0).text()

            # Mostrar cuadro de diálogo de confirmación
            reply = QMessageBox.question(
                self, 
                "Confirmación", 
                f"¿Estás seguro de que deseas eliminar el registro ?", 
                QMessageBox.Yes | QMessageBox.No, 
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # Obtener el resultado de delete_record
                resultado = self.db.delete_record(id_Usuarios)

                # Verificar si la eliminación fue exitosa
                if resultado["success"]:
                    self.load_data()
                    QMessageBox.information(self, "Éxito", resultado["message"])
                else:
                    QMessageBox.warning(self, "Error", resultado["message"])

    def search_records(self):
        search_term = self.search_bar.text()
        results = self.db.search_record(search_term)
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(results):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                
    def get_record_data(self):
        cliente, ok = QInputDialog.getText(self, "Cliente", "Nombre del cliente:")
        if not ok or not cliente:
            return None, None, None, None, None, None

        cedula_nit, ok = QInputDialog.getText(self, "Cédula/NIT", "Cédula/NIT:")
        correo, ok = QInputDialog.getText(self, "Correo", "Correo electrónico:")
        telefono, ok = QInputDialog.getText(self, "Teléfono", "Número de teléfono:")
       

        return cliente, cedula_nit, correo, telefono


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= Tab1()
    window.show()
    sys.exit(app.exec_())
