
import sys

# Generación de archivos PDF


# PyQt5 para la interfaz gráfica
from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
    QDialogButtonBox,
    QTextEdit,
    QDialog,
    QGridLayout,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from class_DatabaseManager import DatabaseManager


class ReporteFallasWindow(QDialog):
    def __init__(self, connection_data, mode="add", cedula_nit=None, numero_serie=None):
        super().__init__()
        self.db = DatabaseManager(**connection_data)  # Pasar los datos de conexión
        self.mode = mode  # Modo: "add" o "update"
        self.cedula_nit = cedula_nit  # Valor de cédula/NIT para el modo "update"
        self.numero_serie = numero_serie  # Valor de número de serie para el modo "update"
        self.setWindowTitle("Reporte de Fallas")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setMinimumSize(1000, 900)
        self.resize(1000, 800)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        # Título de la ventana
        title_label = QLabel("Reporte de Fallas")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2E86C1; padding: 10px;")
        layout.addWidget(title_label)

        # Layout de formulario
        form_layout = QGridLayout()

        # Crear fuente para las etiquetas y campos de entrada
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)

        input_font = QFont()
        input_font.setPointSize(12)

        button_font = QFont()
        button_font.setPointSize(10)
        button_font.setBold(True)

        # Campos de entrada
        self.cedula_nit_combo = QComboBox()
        self.numero_serie_combo = QComboBox()
        if self.mode == "update":
            # Modo actualizar: deshabilitar comboboxes
            self.cedula_nit_combo.setEnabled(False)
            self.numero_serie_combo.setEnabled(False)
        else:
            # Modo agregar: habilitar comboboxes
            self.cedula_nit_combo.setEnabled(True)
            self.numero_serie_combo.setEnabled(True)
            
        self.descripcion_falla_input = QTextEdit()
        self.diagnostico_input = QTextEdit()
        self.reparacion_input = QTextEdit()
        self.Notas_input = QTextEdit()

        # Configurar tamaños mínimos más grandes
        self.descripcion_falla_input.setMinimumHeight(150)
        self.diagnostico_input.setMinimumHeight(150)
        self.reparacion_input.setMinimumHeight(150)
        self.Notas_input.setMinimumHeight(150)

        # Cargar datos en los combobox
        self.load_cedulas()
        self.load_numeros_serie()

        # Configurar estilos y tamaños
        inputs = [
            self.cedula_nit_combo,
            self.numero_serie_combo,
            self.descripcion_falla_input,
            self.diagnostico_input,
            self.reparacion_input,
            self.Notas_input
        ]

        for input_field in inputs:
            if isinstance(input_field, QComboBox):
                input_field.setFont(input_font)
                input_field.setStyleSheet("""
                    QComboBox {
                        padding: 8px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                """)
            elif isinstance(input_field, QTextEdit):
                input_field.setFont(input_font)
                input_field.setStyleSheet("""
                    QTextEdit {
                        padding: 8px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                """)

        labels = [
            QLabel("Cédula/NIT:"),
            QLabel("Número de Serie:"),
            QLabel("Descripción de la Falla:"),
            QLabel("Diagnóstico:"),
            QLabel("Reparación:"),
            QLabel("Notas:")
        ]

        for label in labels:
            label.setFont(label_font)
            label.setStyleSheet("color: #34495E;")
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Añadir widgets al diseño en dos columnas
        for i, (label, input_field) in enumerate(zip(labels, inputs)):
            form_layout.addWidget(label, i, 0)
            form_layout.addWidget(input_field, i, 1)

        form_layout.setVerticalSpacing(20)
        form_layout.setHorizontalSpacing(15)

        # Crear botones adicionales
        self.fill_button = QPushButton("LLENAR ESPACIOS")

        # Crear botones de QDialogButtonBox (OK y Cancel)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal,
            self
        )
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.buttons.button(QDialogButtonBox.Ok).setText("GUARDAR")
        self.buttons.button(QDialogButtonBox.Cancel).setText("CANCELAR")

        # Configurar fuente y estilo para todos los botones
        button_style = """
            QPushButton {
                background-color: #2E86C1;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #3498DB;
            }
        """
        self.fill_button.setFont(button_font)
        self.fill_button.setStyleSheet(button_style)
       
        for button in self.buttons.buttons():
            button.setFont(button_font)
            button.setStyleSheet(button_style)

        # Layout horizontal para los botones
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.fill_button)
        button_layout.addWidget(self.buttons.button(QDialogButtonBox.Ok))
        button_layout.addWidget(self.buttons.button(QDialogButtonBox.Cancel))
        button_layout.addStretch()

        # Añadir layouts y botones al layout principal
        layout.addLayout(form_layout)
        layout.addStretch()
        layout.addLayout(button_layout)

        # Márgenes
        layout.setContentsMargins(30, 20, 30, 20)

        # Conectar señales de los botones
        self.fill_button.clicked.connect(self.fill_fields)

    def load_cedulas(self):
      
        try:
            if self.mode == "add":
                # Modo agregar: cargar solo cédulas/NITs que no están en reporte_fallas
                cedulas = self.db.fetch_cedulas_for_add()
            else:
                # Modo actualizar: cargar todas las cédulas/NITs
                cedulas = self.db.fetch_all_cedulas()

            self.cedula_nit_combo.clear()
            self.cedula_nit_combo.addItems(cedulas)

            # Si estamos en modo actualizar, establecer el valor de la fila seleccionada
            if self.mode == "update" and self.cedula_nit:
                self.cedula_nit_combo.setCurrentText(self.cedula_nit)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar cédulas/NITs: {str(e)}")

    def load_numeros_serie(self):
        """Cargar los números de serie en el combobox según el modo."""
        try:
            if self.mode == "add":
                # Modo agregar: cargar solo números de serie que no están en reporte_fallas
                numeros_serie = self.db.fetch_numeros_serie_for_add()
            else:
                # Modo actualizar: cargar todos los números de serie
                numeros_serie = self.db.fetch_all_numeros_serie()

            self.numero_serie_combo.clear()
            self.numero_serie_combo.addItems(numeros_serie)

            # Si estamos en modo actualizar, establecer el valor de la fila seleccionada
            if self.mode == "update" and self.numero_serie:
                self.numero_serie_combo.setCurrentText(self.numero_serie)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar números de serie: {str(e)}")

    def fill_fields(self):
        """Llenar campos vacíos con 'N/A'."""
        if self.cedula_nit_combo.currentText() == "":
            self.cedula_nit_combo.setCurrentText("N/A")
        if self.numero_serie_combo.currentText() == "":
            self.numero_serie_combo.setCurrentText("N/A")
        if not self.descripcion_falla_input.toPlainText():
            self.descripcion_falla_input.setPlainText("N/A")
        if not self.diagnostico_input.toPlainText():
            self.diagnostico_input.setPlainText("N/A")
        if not self.reparacion_input.toPlainText():
            self.reparacion_input.setPlainText("N/A")
        if not self.Notas_input.toPlainText():
            self.Notas_input.setPlainText("N/A")

    def accept(self):
        """Validar campos antes de cerrar el diálogo."""
        if not all([
            self.cedula_nit_combo.currentText(),
            self.numero_serie_combo.currentText(),
            self.descripcion_falla_input.toPlainText(),
            self.diagnostico_input.toPlainText(),
            self.reparacion_input.toPlainText(),
            self.Notas_input.toPlainText()
        ]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        super().accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= ReporteFallasWindow()
    window.show()
    sys.exit(app.exec_())
