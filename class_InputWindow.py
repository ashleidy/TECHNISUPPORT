
import sys




# PyQt5 para la interfaz gráfica
from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QDialogButtonBox,
    QDialog,
    QGridLayout,

)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDate


class InputWindow(QDialog):
    def __init__(self,mode):
        super().__init__()
        self.setWindowTitle("Registro de usuarios")  # Cambiar el título de la ventana
        self.mode = mode  # Modo: "add" o "update"

        # Configurar banderas para evitar el signo de interrogación
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Configurar tamaño mínimo y tamaño inicial
        self.setMinimumSize(600, 450)  # Tamaño mínimo
        self.resize(700, 550)         # Tamaño inicial

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setSpacing(20)  # Espaciado entre elementos

        # Título de la ventana
        title_label = QLabel("Registro de usuarios")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2E86C1; padding: 10px;")  # Estilo del título
        layout.addWidget(title_label)

        # Layout de formulario
        form_layout = QGridLayout()
        form_layout.setVerticalSpacing(15)
        form_layout.setHorizontalSpacing(10)

        # Crear fuente para las etiquetas y campos de entrada
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)

        input_font = QFont()
        input_font.setPointSize(12)

        button_font = QFont()  # Crear fuente para los botones
        button_font.setPointSize(10)
        button_font.setBold(True)

        # Campos de entrada
        self.cliente_input = QLineEdit()
        self.cedula_input = QLineEdit()
        
        if self.mode == "update":
            # Modo actualizar: deshabilitar comboboxes
            self.cedula_input.setEnabled(False)
        else:
            # Modo agregar: habilitar comboboxes
            self.cedula_input.setEnabled(True)
        
        
        self.correo_input = QLineEdit()
        self.telefono_input = QLineEdit()

        inputs = [
            self.cliente_input,
            self.cedula_input,
            self.correo_input,
            self.telefono_input
        ]

        for input_field in inputs:
            input_field.setMinimumHeight(40)
            input_field.setFont(input_font)
            input_field.setStyleSheet(
                "QLineEdit { padding: 8px; border: 1px solid #ccc; border-radius: 5px; }"
            )

        labels = [
            QLabel("Cliente:"),
            QLabel("Cédula/NIT:"),
            QLabel("Correo:"),
            QLabel("Teléfono:")
        ]

        for label in labels:
            label.setFont(label_font)
            label.setStyleSheet("color: #34495E;")

        # Añadir widgets al diseño en dos columnas
        form_layout.addWidget(labels[0], 0, 0)
        form_layout.addWidget(self.cliente_input, 0, 1)
        form_layout.addWidget(labels[1], 1, 0)
        form_layout.addWidget(self.cedula_input, 1, 1)
        form_layout.addWidget(labels[2], 2, 0)
        form_layout.addWidget(self.correo_input, 2, 1)
        form_layout.addWidget(labels[3], 3, 0)
        form_layout.addWidget(self.telefono_input, 3, 1)

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
        
         # Cambiar el texto de los botones
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

        # Layout horizontal para centrar los 4 botones
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Espacio flexible a la izquierda
        button_layout.addWidget(self.fill_button)
        
        button_layout.addWidget(self.buttons.button(QDialogButtonBox.Ok))  # Botón OK
        button_layout.addWidget(self.buttons.button(QDialogButtonBox.Cancel))  # Botón Cancel
        button_layout.addStretch()  # Espacio flexible a la derecha

        # Añadir layouts y botones al layout principal
        layout.addLayout(form_layout)
        layout.addStretch()
        layout.addLayout(button_layout)  # Añadir el layout de botones centrados

        layout.setContentsMargins(30, 20, 30, 20)  # Márgenes del layout principal

        # Conectar señales de los botones
        self.fill_button.clicked.connect(self.fill_fields)
       

    def fill_fields(self):
        # Llenar los espacios vacíos con "N/A" sin sobrescribir los llenos
        if not self.cliente_input.text():
            self.cliente_input.setText("N/A")
        if not self.cedula_input.text():
            self.cedula_input.setText("N/A")
        if not self.correo_input.text():
            self.correo_input.setText("N/A")
        if not self.telefono_input.text():
            self.telefono_input.setText("N/A")

    def clear_fields(self):
        # Borrar todos los campos
        self.cliente_input.clear()
        self.cedula_input.clear()
        self.correo_input.clear()
        self.telefono_input.clear()
        
    def accept(self):
            # Verificar si todos los campos están llenos
        if not all([
            self.cliente_input.text(),
            self.cedula_input.text(),
            self.correo_input.text(),
            self.telefono_input.text()
            
        ]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return  # No cerrar el diálogo si hay campos vacíos

        # Si todos los campos están llenos, cerrar el diálogo
        super().accept()
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= InputWindow()
    window.show()
    sys.exit(app.exec_())
