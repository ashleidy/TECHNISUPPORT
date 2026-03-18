
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
    QAbstractScrollArea,
    QInputDialog,
    QDialog,
)

from PyQt5.QtCore import Qt
from class_ReporteFallas import ReporteFallasWindow
from class_DatabaseManager import DatabaseManager

class Tab3(QWidget):
    
    def __init__(self,connection_data):
        super().__init__()
        self.connection_data = connection_data  # Guardar los datos de conexión
        self.db = DatabaseManager(**connection_data)  # Pasar los datos de conexión
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Gestión de Reporte de Fallas")
        self.resize(800, 600)

        layout = QVBoxLayout(self)

        # Formulario de entrada de datos
        form_layout = QHBoxLayout()

      

        layout.addLayout(form_layout)

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Buscar...")
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_fallas)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(7)  # Número de columnas en la tabla "reporte_fallas"
        self.table.setHorizontalHeaderLabels([
            "ID Info", "Cédula/NIT", "Número de Serie", "Descripción Falla", "Diagnóstico", "Reparación", "Notas"
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
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Ajustar columnas al contenido
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)  # Ajustar el tamaño de la tabla al contenido
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Habilitar barra de desplazamiento horizontal
        layout.addWidget(self.table)

        # Buttons
        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.open_ReporteFallas_Window)

        self.update_button = QPushButton("Actualizar")
        self.update_button.clicked.connect(self.update_fallas)
        

        self.delete_button = QPushButton("Eliminar")
        self.delete_button.clicked.connect(self.delete_fallas)

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
        self.search_button.setStyleSheet(button_style)
        self.update_button.setStyleSheet(button_style)
        self.delete_button.setStyleSheet(button_style)
      
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
       

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_data()


    def load_data(self):
        self.table.setRowCount(0)
        records = self.db.fetch_all_fallas()
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def open_ReporteFallas_Window(self):
        try:
        # Abrir la ventana en modo "add"
            dialog = ReporteFallasWindow(self.connection_data, mode="add")
            result = dialog.exec_()

            if result == QDialog.Accepted:
                id_cedula_nit = dialog.cedula_nit_combo.currentText()
                id_numero_serie = dialog.numero_serie_combo.currentText()
                descripcion_falla = dialog.descripcion_falla_input.toPlainText()
                diagnostico = dialog.diagnostico_input.toPlainText()
                reparacion = dialog.reparacion_input.toPlainText()
                Notas = dialog.Notas_input.toPlainText()

                try:
                    self.add_fallas(id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error al agregar el registro: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir la ventana: {str(e)}")

    def add_fallas(self, id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas):
        try:
            self.db.add_fallas(id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas)
            self.load_data()
            QMessageBox.information(self, "Éxito", "Registro agregado correctamente.")
        except ValueError as e:
        # Captura específicamente los errores de validación (cédula o número de serie no existente)
           QMessageBox.warning(self, "Error de validación", str(e))
        except Exception as e:
        # Captura otros errores que puedan ocurrir
           QMessageBox.critical(self, "Error", f"Error al agregar el registro: {str(e)}")
    
  

  
  
    def update_fallas(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "Selecciona un registro para actualizar.")
            return

        try:
            # Obtener datos de la fila seleccionada
            id_info = self.table.item(selected_row, 0).text()
            id_cedula_nit = self.table.item(selected_row, 1).text()
            id_numero_serie = self.table.item(selected_row, 2).text()
            descripcion_falla = self.table.item(selected_row, 3).text()
            diagnostico = self.table.item(selected_row, 4).text()
            reparacion = self.table.item(selected_row, 5).text()
            Notas = self.table.item(selected_row, 6).text()

            # Abrir la ventana en modo "update" y pasar los valores de la fila seleccionada
            dialog = ReporteFallasWindow(
                self.connection_data,
                mode="update",
                cedula_nit=id_cedula_nit,
                numero_serie=id_numero_serie
            )

            # Establecer los valores iniciales en el diálogo
            dialog.descripcion_falla_input.setPlainText(descripcion_falla)
            dialog.diagnostico_input.setPlainText(diagnostico)
            dialog.reparacion_input.setPlainText(reparacion)
            dialog.Notas_input.setPlainText(Notas)

            result = dialog.exec_()

            if result == QDialog.Accepted:
                # Obtener datos actualizados desde la ventana de edición
                new_cedula_nit = dialog.cedula_nit_combo.currentText()
                new_numero_serie = dialog.numero_serie_combo.currentText()
                new_descripcion_falla = dialog.descripcion_falla_input.toPlainText()
                new_diagnostico = dialog.diagnostico_input.toPlainText()
                new_reparacion = dialog.reparacion_input.toPlainText()
                new_Notas = dialog.Notas_input.toPlainText()

                try:
                    self.db.update_fallas(
                        id_info,
                        new_cedula_nit,
                        new_numero_serie,
                        new_descripcion_falla,
                        new_diagnostico,
                        new_reparacion,
                        new_Notas
                    )
                    self.load_data()
                    QMessageBox.information(self, "Éxito", "Registro actualizado correctamente.")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error al actualizar el registro: {str(e)}")
            else:
                QMessageBox.information(self, "Cancelado", "Actualización cancelada.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir la ventana: {str(e)}")


    def delete_fallas(self):
        # Verificar que la fila seleccionada es válida
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "Selecciona un registro para eliminar.")
            return

        id_info = self.table.item(selected_row, 0).text()

        # Mostrar cuadro de diálogo de confirmación
        reply = QMessageBox.question(
            self, 
            "Confirmación", 
            f"¿Estás seguro de que deseas eliminar el registro?", 
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Obtener el resultado de delete_fallas
            resultado = self.db.delete_fallas(id_info)

            # Verificar si la eliminación fue exitosa
            if resultado["success"]:
                self.load_data()  # Recargar los datos en la tabla
                QMessageBox.information(self, "Éxito", resultado["message"])
            else:
                QMessageBox.warning(self, "Error", resultado["message"])

    def search_fallas(self):
        search_term = self.search_bar.text()
        results = self.db.search_fallas(search_term)
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(results):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                
    def get_record_data(self):
       # Recoger datos del usuario a través de cuadros de diálogo
        id_cedula_nit, ok = QInputDialog.getText(self, "Cédula/NIT", "Cédula/NIT:")
        if not ok or not id_cedula_nit:
            return None

        id_numero_serie, ok = QInputDialog.getText(self, "Número de serie", "Número de serie del equipo:")
        if not ok or not id_numero_serie:
            return None

        descripcion_falla, ok = QInputDialog.getText(self, "Descripción de la falla", "Descripción de la falla:")
        if not ok or not descripcion_falla:
            return None

        diagnostico, ok = QInputDialog.getText(self, "Diagnóstico", "Diagnóstico de la falla:")
        if not ok or not diagnostico:
            return None

        reparacion, ok = QInputDialog.getText(self, "Reparación", "Reparación realizada:")
        if not ok or not reparacion:
            return None

        Notas, ok = QInputDialog.getText(self, "Notas", "Notas:")
        if not ok or not Notas:
            return None

        return id_cedula_nit, id_numero_serie, descripcion_falla, diagnostico, reparacion, Notas
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= Tab3()
    window.show()
    sys.exit(app.exec_())
