
import sys

# PyQt5 para la interfaz gráfica
from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QDialogButtonBox,
    QDateEdit,
    QDialog,
    QGridLayout,
    QScrollArea
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDate


class InputWindowHojaVida(QDialog):
    def __init__(self,mode):
        super().__init__()
        self.setWindowTitle("Registro de Hoja de Vida del Equipo")  # Cambiar el título de la ventana
        self.mode = mode  # Modo: "add" o "update"
        # Configurar banderas para evitar el signo de interrogación
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Configurar tamaño mínimo y tamaño inicial
        self.setMinimumSize(800, 600)
        self.resize(1000, 800)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setSpacing(20)  # Espaciado entre elementos

        # Título de la ventana
        title_label = QLabel("Registro de Hoja de Vida del Equipo")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2E86C1; padding: 10px;")  # Estilo del título
        layout.addWidget(title_label)

        # Crear un área de desplazamiento
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  # Hacer que el área de desplazamiento sea redimensionable
        scroll_area.setStyleSheet("QScrollArea { border: none; }")  # Eliminar el borde del QScrollArea

        # Widget que contendrá el formulario
        form_widget = QWidget()
        form_layout = QGridLayout(form_widget)
        form_layout.setVerticalSpacing(15)
        form_layout.setHorizontalSpacing(10)

        # Crear fuentes para las etiquetas y campos de entrada
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)

        input_font = QFont()
        input_font.setPointSize(12)

        button_font = QFont()
        button_font.setPointSize(10)
        button_font.setBold(True)

        # Campos de entrada
        self.fecha_ingreso_input = QDateEdit(self)
        self.fecha_ingreso_input.setDisplayFormat("yyyy-MM-dd")
        self.fecha_ingreso_input.setDate(QDate.currentDate())
        self.fecha_ingreso_input.setCalendarPopup(True)

        self.fecha_entrega_input = QDateEdit(self)
        self.fecha_entrega_input.setDisplayFormat("yyyy-MM-dd")
        self.fecha_entrega_input.setDate(QDate.currentDate())
        self.fecha_entrega_input.setCalendarPopup(True)

        self.tipo_input = QLineEdit()
        self.marca_input = QLineEdit()
        self.modelo_input = QLineEdit()
        self.numero_serie_input = QLineEdit()
        if self.mode == "update":
            # Modo actualizar: deshabilitar comboboxes
            self.numero_serie_input.setEnabled(False)
        else:
            # Modo agregar: habilitar comboboxes
            self.numero_serie_input.setEnabled(True)
        
        
        
        self.main_board_marca_input = QLineEdit()
        self.main_board_modelo_input = QLineEdit()
        self.main_board_numero_serie_input = QLineEdit()
        self.wifi_marca_input = QLineEdit()
        self.wifi_modelo_input = QLineEdit()
        self.wifi_numero_serie_input = QLineEdit()
        self.teclado_marca_input = QLineEdit()
        self.teclado_modelo_input = QLineEdit()
        self.teclado_numero_serie_input = QLineEdit()
        self.CPU1_marca_input = QLineEdit()
        self.CPU1_modelo_input = QLineEdit()
        self.CPU1_numero_serie_input = QLineEdit()
        self.CPU2_marca_input = QLineEdit()
        self.CPU2_modelo_input = QLineEdit()
        self.CPU2_numero_serie_input = QLineEdit()
        self.psu_marca_input = QLineEdit()
        self.psu_modelo_input = QLineEdit()
        self.psu_capacidad_input = QLineEdit()
        self.pantalla_marca_input = QLineEdit()
        self.pantalla_modelo_input = QLineEdit()
        self.pantalla_capacidad_input = QLineEdit()
        self.pantalla_numero_serie_input = QLineEdit()
        self.bateria_marca_input = QLineEdit()
        self.bateria_modelo_input = QLineEdit()
        self.bateria_numero_serie_input = QLineEdit()
        self.bateria_capacidad_input = QLineEdit()
        self.ram1_marca_input = QLineEdit()
        self.ram1_modelo_input = QLineEdit()
        self.ram1_capacidad_input = QLineEdit()
        self.ram1_numero_serie_input = QLineEdit()
        self.ram2_marca_input = QLineEdit()
        self.ram2_modelo_input = QLineEdit()
        self.ram2_capacidad_input = QLineEdit()
        self.ram2_numero_serie_input = QLineEdit()
        self.ram3_marca_input = QLineEdit()
        self.ram3_modelo_input = QLineEdit()
        self.ram3_capacidad_input = QLineEdit()
        self.ram3_numero_serie_input = QLineEdit()
        self.ram4_marca_input = QLineEdit()
        self.ram4_modelo_input = QLineEdit()
        self.ram4_capacidad_input = QLineEdit()
        self.ram4_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento1_marca_input = QLineEdit()
        self.Unidad_almacenamiento1_modelo_input = QLineEdit()
        self.Unidad_almacenamiento1_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento1_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento2_marca_input = QLineEdit()
        self.Unidad_almacenamiento2_modelo_input = QLineEdit()
        self.Unidad_almacenamiento2_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento2_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento3_marca_input = QLineEdit()
        self.Unidad_almacenamiento3_modelo_input = QLineEdit()
        self.Unidad_almacenamiento3_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento3_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento4_marca_input = QLineEdit()
        self.Unidad_almacenamiento4_modelo_input = QLineEdit()
        self.Unidad_almacenamiento4_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento4_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento5_marca_input = QLineEdit()
        self.Unidad_almacenamiento5_modelo_input = QLineEdit()
        self.Unidad_almacenamiento5_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento5_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento6_marca_input = QLineEdit()
        self.Unidad_almacenamiento6_modelo_input = QLineEdit()
        self.Unidad_almacenamiento6_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento6_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento7_marca_input = QLineEdit()
        self.Unidad_almacenamiento7_modelo_input = QLineEdit()
        self.Unidad_almacenamiento7_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento7_numero_serie_input = QLineEdit()
        self.Unidad_almacenamiento8_marca_input = QLineEdit()
        self.Unidad_almacenamiento8_modelo_input = QLineEdit()
        self.Unidad_almacenamiento8_capacidad_input = QLineEdit()
        self.Unidad_almacenamiento8_numero_serie_input = QLineEdit()
        self.GPU1_marca_input = QLineEdit()
        self.GPU1_modelo_input = QLineEdit()
        self.GPU1_capacidad_input = QLineEdit()
        self.GPU1_numero_serie_input = QLineEdit()
        self.GPU2_marca_input = QLineEdit()
        self.GPU2_modelo_input = QLineEdit()
        self.GPU2_capacidad_input = QLineEdit()
        self.GPU2_numero_serie_input = QLineEdit()
        self.Unidad_DVD1_marca_input = QLineEdit()
        self.Unidad_DVD1_modelo_input = QLineEdit()
        self.Unidad_DVD1_capacidad_input = QLineEdit()
        self.Unidad_DVD1_numero_serie_input = QLineEdit()
        self.Unidad_DVD2_marca_input = QLineEdit()
        self.Unidad_DVD2_modelo_input = QLineEdit()
        self.Unidad_DVD2_capacidad_input = QLineEdit()
        self.Unidad_DVD2_numero_serie_input = QLineEdit()

        inputs = [
            self.fecha_ingreso_input, self.fecha_entrega_input, self.tipo_input, self.marca_input, self.modelo_input,
            self.numero_serie_input, self.main_board_marca_input, self.main_board_modelo_input, self.main_board_numero_serie_input,
            self.wifi_marca_input, self.wifi_modelo_input, self.wifi_numero_serie_input, self.teclado_marca_input, self.teclado_modelo_input,
            self.teclado_numero_serie_input, self.CPU1_marca_input, self.CPU1_modelo_input, self.CPU1_numero_serie_input, self.CPU2_marca_input,
            self.CPU2_modelo_input, self.CPU2_numero_serie_input, self.psu_marca_input, self.psu_modelo_input, self.psu_capacidad_input,
            self.pantalla_marca_input, self.pantalla_modelo_input, self.pantalla_capacidad_input, self.pantalla_numero_serie_input,
            self.bateria_marca_input, self.bateria_modelo_input, self.bateria_numero_serie_input, self.bateria_capacidad_input,
            self.ram1_marca_input, self.ram1_modelo_input, self.ram1_capacidad_input, self.ram1_numero_serie_input, self.ram2_marca_input,
            self.ram2_modelo_input, self.ram2_capacidad_input, self.ram2_numero_serie_input, self.ram3_marca_input, self.ram3_modelo_input,
            self.ram3_capacidad_input, self.ram3_numero_serie_input, self.ram4_marca_input, self.ram4_modelo_input, self.ram4_capacidad_input,
            self.ram4_numero_serie_input, self.Unidad_almacenamiento1_marca_input, self.Unidad_almacenamiento1_modelo_input,
            self.Unidad_almacenamiento1_capacidad_input, self.Unidad_almacenamiento1_numero_serie_input, self.Unidad_almacenamiento2_marca_input,
            self.Unidad_almacenamiento2_modelo_input, self.Unidad_almacenamiento2_capacidad_input, self.Unidad_almacenamiento2_numero_serie_input,
            self.Unidad_almacenamiento3_marca_input, self.Unidad_almacenamiento3_modelo_input, self.Unidad_almacenamiento3_capacidad_input,
            self.Unidad_almacenamiento3_numero_serie_input, self.Unidad_almacenamiento4_marca_input, self.Unidad_almacenamiento4_modelo_input,
            self.Unidad_almacenamiento4_capacidad_input, self.Unidad_almacenamiento4_numero_serie_input, self.Unidad_almacenamiento5_marca_input,
            self.Unidad_almacenamiento5_modelo_input, self.Unidad_almacenamiento5_capacidad_input, self.Unidad_almacenamiento5_numero_serie_input,
            self.Unidad_almacenamiento6_marca_input, self.Unidad_almacenamiento6_modelo_input, self.Unidad_almacenamiento6_capacidad_input,
            self.Unidad_almacenamiento6_numero_serie_input, self.Unidad_almacenamiento7_marca_input, self.Unidad_almacenamiento7_modelo_input,
            self.Unidad_almacenamiento7_capacidad_input, self.Unidad_almacenamiento7_numero_serie_input, self.Unidad_almacenamiento8_marca_input,
            self.Unidad_almacenamiento8_modelo_input, self.Unidad_almacenamiento8_capacidad_input, self.Unidad_almacenamiento8_numero_serie_input,
            self.GPU1_marca_input, self.GPU1_modelo_input, self.GPU1_capacidad_input, self.GPU1_numero_serie_input, self.GPU2_marca_input,
            self.GPU2_modelo_input, self.GPU2_capacidad_input, self.GPU2_numero_serie_input, self.Unidad_DVD1_marca_input, self.Unidad_DVD1_modelo_input,
            self.Unidad_DVD1_capacidad_input, self.Unidad_DVD1_numero_serie_input, self.Unidad_DVD2_marca_input, self.Unidad_DVD2_modelo_input,
            self.Unidad_DVD2_capacidad_input, self.Unidad_DVD2_numero_serie_input
        ]

        for input_field in inputs:
            input_field.setMinimumHeight(50)
            input_field.setFont(input_font)
            input_field.setStyleSheet(
                "QLineEdit, QDateEdit { padding: 8px; border: 1px solid #ccc; border-radius: 5px; }"
            )

        labels = [
            QLabel("Fecha de Ingreso:"), QLabel("Fecha de Entrega:"), QLabel("Tipo:"), QLabel("Marca:"), QLabel("Modelo:"),
            QLabel("Número de Serie:"), QLabel("Main Board Marca:"), QLabel("Main Board Modelo:"), QLabel("Main Board Número de Serie:"),
            QLabel("WiFi Marca:"), QLabel("WiFi Modelo:"), QLabel("WiFi Número de Serie:"), QLabel("Teclado Marca:"), QLabel("Teclado Modelo:"),
            QLabel("Teclado Número de Serie:"), QLabel("CPU1 Marca:"), QLabel("CPU1 Modelo:"), QLabel("CPU1 Número de Serie:"), QLabel("CPU2 Marca:"),
            QLabel("CPU2 Modelo:"), QLabel("CPU2 Número de Serie:"), QLabel("PSU Marca:"), QLabel("PSU Modelo:"), QLabel("PSU Capacidad:"),
            QLabel("Pantalla Marca:"), QLabel("Pantalla Modelo:"), QLabel("Pantalla Capacidad:"), QLabel("Pantalla Número de Serie:"),
            QLabel("Batería Marca:"), QLabel("Batería Modelo:"), QLabel("Batería Número de Serie:"), QLabel("Batería Capacidad:"),
            QLabel("RAM1 Marca:"), QLabel("RAM1 Modelo:"), QLabel("RAM1 Capacidad:"), QLabel("RAM1 Número de Serie:"), QLabel("RAM2 Marca:"),
            QLabel("RAM2 Modelo:"), QLabel("RAM2 Capacidad:"), QLabel("RAM2 Número de Serie:"), QLabel("RAM3 Marca:"), QLabel("RAM3 Modelo:"),
            QLabel("RAM3 Capacidad:"), QLabel("RAM3 Número de Serie:"), QLabel("RAM4 Marca:"), QLabel("RAM4 Modelo:"), QLabel("RAM4 Capacidad:"),
            QLabel("RAM4 Número de Serie:"), QLabel("Unidad Almacenamiento1 Marca:"), QLabel("Unidad Almacenamiento1 Modelo:"),
            QLabel("Unidad Almacenamiento1 Capacidad:"), QLabel("Unidad Almacenamiento1 Número de Serie:"), QLabel("Unidad Almacenamiento2 Marca:"),
            QLabel("Unidad Almacenamiento2 Modelo:"), QLabel("Unidad Almacenamiento2 Capacidad:"), QLabel("Unidad Almacenamiento2 Número de Serie:"),
            QLabel("Unidad Almacenamiento3 Marca:"), QLabel("Unidad Almacenamiento3 Modelo:"), QLabel("Unidad Almacenamiento3 Capacidad:"),
            QLabel("Unidad Almacenamiento3 Número de Serie:"), QLabel("Unidad Almacenamiento4 Marca:"), QLabel("Unidad Almacenamiento4 Modelo:"),
            QLabel("Unidad Almacenamiento4 Capacidad:"), QLabel("Unidad Almacenamiento4 Número de Serie:"), QLabel("Unidad Almacenamiento5 Marca:"),
            QLabel("Unidad Almacenamiento5 Modelo:"), QLabel("Unidad Almacenamiento5 Capacidad:"), QLabel("Unidad Almacenamiento5 Número de Serie:"),
            QLabel("Unidad Almacenamiento6 Marca:"), QLabel("Unidad Almacenamiento6 Modelo:"), QLabel("Unidad Almacenamiento6 Capacidad:"),
            QLabel("Unidad Almacenamiento6 Número de Serie:"), QLabel("Unidad Almacenamiento7 Marca:"), QLabel("Unidad Almacenamiento7 Modelo:"),
            QLabel("Unidad Almacenamiento7 Capacidad:"), QLabel("Unidad Almacenamiento7 Número de Serie:"), QLabel("Unidad Almacenamiento8 Marca:"),
            QLabel("Unidad Almacenamiento8 Modelo:"), QLabel("Unidad Almacenamiento8 Capacidad:"), QLabel("Unidad Almacenamiento8 Número de Serie:"),
            QLabel("GPU1 Marca:"), QLabel("GPU1 Modelo:"), QLabel("GPU1 Capacidad:"), QLabel("GPU1 Número de Serie:"), QLabel("GPU2 Marca:"),
            QLabel("GPU2 Modelo:"), QLabel("GPU2 Capacidad:"), QLabel("GPU2 Número de Serie:"), QLabel("Unidad DVD1 Marca:"), QLabel("Unidad DVD1 Modelo:"),
            QLabel("Unidad DVD1 Capacidad:"), QLabel("Unidad DVD1 Número de Serie:"), QLabel("Unidad DVD2 Marca:"), QLabel("Unidad DVD2 Modelo:"),
            QLabel("Unidad DVD2 Capacidad:"), QLabel("Unidad DVD2 Número de Serie:")
        ]

        for label in labels:
            label.setFont(label_font)
            label.setStyleSheet("color: #34495E;")

        # Añadir widgets al diseño en dos columnas
        for i, (label, input_field) in enumerate(zip(labels, inputs)):
            form_layout.addWidget(label, i, 0)
            form_layout.addWidget(input_field, i, 1)

        # Configurar el widget del formulario para que se expanda
        form_widget.setLayout(form_layout)
        scroll_area.setWidget(form_widget)

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

        # Layout horizontal para centrar los 4 botones
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Espacio flexible a la izquierda
        button_layout.addWidget(self.fill_button)
    
        button_layout.addWidget(self.buttons.button(QDialogButtonBox.Ok))  # Botón OK
        button_layout.addWidget(self.buttons.button(QDialogButtonBox.Cancel))  # Botón Cancel
        button_layout.addStretch()  # Espacio flexible a la derecha

        # Añadir layouts y botones al layout principal
        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)  # Añadir el layout de botones centrados

        layout.setContentsMargins(30, 20, 30, 20)  # Márgenes del layout principal

        # Conectar señales de los botones
        self.fill_button.clicked.connect(self.fill_fields)
      

    def fill_fields(self):
        # Llenar los espacios vacíos con "N/A" sin sobrescribir los llenos
        for input_field in [
            self.tipo_input, self.marca_input, self.modelo_input, self.numero_serie_input,
            self.main_board_marca_input, self.main_board_modelo_input, self.main_board_numero_serie_input,
            self.wifi_marca_input, self.wifi_modelo_input, self.wifi_numero_serie_input,
            self.teclado_marca_input, self.teclado_modelo_input, self.teclado_numero_serie_input,
            self.CPU1_marca_input, self.CPU1_modelo_input, self.CPU1_numero_serie_input,
            self.CPU2_marca_input, self.CPU2_modelo_input, self.CPU2_numero_serie_input,
            self.psu_marca_input, self.psu_modelo_input, self.psu_capacidad_input,
            self.pantalla_marca_input, self.pantalla_modelo_input, self.pantalla_capacidad_input,
            self.pantalla_numero_serie_input, self.bateria_marca_input, self.bateria_modelo_input,
            self.bateria_numero_serie_input, self.bateria_capacidad_input, self.ram1_marca_input,
            self.ram1_modelo_input, self.ram1_capacidad_input, self.ram1_numero_serie_input,
            self.ram2_marca_input, self.ram2_modelo_input, self.ram2_capacidad_input,
            self.ram2_numero_serie_input, self.ram3_marca_input, self.ram3_modelo_input,
            self.ram3_capacidad_input, self.ram3_numero_serie_input, self.ram4_marca_input,
            self.ram4_modelo_input, self.ram4_capacidad_input, self.ram4_numero_serie_input,
            self.Unidad_almacenamiento1_marca_input, self.Unidad_almacenamiento1_modelo_input,
            self.Unidad_almacenamiento1_capacidad_input, self.Unidad_almacenamiento1_numero_serie_input,
            self.Unidad_almacenamiento2_marca_input, self.Unidad_almacenamiento2_modelo_input,
            self.Unidad_almacenamiento2_capacidad_input, self.Unidad_almacenamiento2_numero_serie_input,
            self.Unidad_almacenamiento3_marca_input, self.Unidad_almacenamiento3_modelo_input,
            self.Unidad_almacenamiento3_capacidad_input, self.Unidad_almacenamiento3_numero_serie_input,
            self.Unidad_almacenamiento4_marca_input, self.Unidad_almacenamiento4_modelo_input,
            self.Unidad_almacenamiento4_capacidad_input, self.Unidad_almacenamiento4_numero_serie_input,
            self.Unidad_almacenamiento5_marca_input, self.Unidad_almacenamiento5_modelo_input,
            self.Unidad_almacenamiento5_capacidad_input, self.Unidad_almacenamiento5_numero_serie_input,
            self.Unidad_almacenamiento6_marca_input, self.Unidad_almacenamiento6_modelo_input,
            self.Unidad_almacenamiento6_capacidad_input, self.Unidad_almacenamiento6_numero_serie_input,
            self.Unidad_almacenamiento7_marca_input, self.Unidad_almacenamiento7_modelo_input,
            self.Unidad_almacenamiento7_capacidad_input, self.Unidad_almacenamiento7_numero_serie_input,
            self.Unidad_almacenamiento8_marca_input, self.Unidad_almacenamiento8_modelo_input,
            self.Unidad_almacenamiento8_capacidad_input, self.Unidad_almacenamiento8_numero_serie_input,
            self.GPU1_marca_input, self.GPU1_modelo_input, self.GPU1_capacidad_input, self.GPU1_numero_serie_input,
            self.GPU2_marca_input, self.GPU2_modelo_input, self.GPU2_capacidad_input, self.GPU2_numero_serie_input,
            self.Unidad_DVD1_marca_input, self.Unidad_DVD1_modelo_input, self.Unidad_DVD1_capacidad_input,
            self.Unidad_DVD1_numero_serie_input, self.Unidad_DVD2_marca_input, self.Unidad_DVD2_modelo_input,
            self.Unidad_DVD2_capacidad_input, self.Unidad_DVD2_numero_serie_input
        ]:
            if not input_field.text():
                input_field.setText("N/A")
    
    def accept(self):
        # Verificar si todos los campos están llenos
        if not all([
            self.fecha_ingreso_input.text(),
            self.fecha_entrega_input.text(),
            self.tipo_input.text(),
            self.marca_input.text(),
            self.modelo_input.text(),
            self.numero_serie_input.text(),
            self.main_board_marca_input.text(),
            self.main_board_modelo_input.text(),
            self.main_board_numero_serie_input.text(),
            self.wifi_marca_input.text(),
            self.wifi_modelo_input.text(),
            self.wifi_numero_serie_input.text(),
            self.teclado_marca_input.text(),
            self.teclado_modelo_input.text(),
            self.teclado_numero_serie_input.text(),
            self.CPU1_marca_input.text(),
            self.CPU1_modelo_input.text(),
            self.CPU1_numero_serie_input.text(),
            self.CPU2_marca_input.text(),
            self.CPU2_modelo_input.text(),
            self.CPU2_numero_serie_input.text(),
            self.psu_marca_input.text(),
            self.psu_modelo_input.text(),
            self.psu_capacidad_input.text(),
            self.pantalla_marca_input.text(),
            self.pantalla_modelo_input.text(),
            self.pantalla_capacidad_input.text(),
            self.pantalla_numero_serie_input.text(),
            self.bateria_marca_input.text(),
            self.bateria_modelo_input.text(),
            self.bateria_numero_serie_input.text(),
            self.bateria_capacidad_input.text(),
            self.ram1_marca_input.text(),
            self.ram1_modelo_input.text(),
            self.ram1_capacidad_input.text(),
            self.ram1_numero_serie_input.text(),
            self.ram2_marca_input.text(),
            self.ram2_modelo_input.text(),
            self.ram2_capacidad_input.text(),
            self.ram2_numero_serie_input.text(),
            self.ram3_marca_input.text(),
            self.ram3_modelo_input.text(),
            self.ram3_capacidad_input.text(),
            self.ram3_numero_serie_input.text(),
            self.ram4_marca_input.text(),
            self.ram4_modelo_input.text(),
            self.ram4_capacidad_input.text(),
            self.ram4_numero_serie_input.text(),
            self.Unidad_almacenamiento1_marca_input.text(),
            self.Unidad_almacenamiento1_modelo_input.text(),
            self.Unidad_almacenamiento1_capacidad_input.text(),
            self.Unidad_almacenamiento1_numero_serie_input.text(),
            self.Unidad_almacenamiento2_marca_input.text(),
            self.Unidad_almacenamiento2_modelo_input.text(),
            self.Unidad_almacenamiento2_capacidad_input.text(),
            self.Unidad_almacenamiento2_numero_serie_input.text(),
            self.Unidad_almacenamiento3_marca_input.text(),
            self.Unidad_almacenamiento3_modelo_input.text(),
            self.Unidad_almacenamiento3_capacidad_input.text(),
            self.Unidad_almacenamiento3_numero_serie_input.text(),
            self.Unidad_almacenamiento4_marca_input.text(),
            self.Unidad_almacenamiento4_modelo_input.text(),
            self.Unidad_almacenamiento4_capacidad_input.text(),
            self.Unidad_almacenamiento4_numero_serie_input.text(),
            self.Unidad_almacenamiento5_marca_input.text(),
            self.Unidad_almacenamiento5_modelo_input.text(),
            self.Unidad_almacenamiento5_capacidad_input.text(),
            self.Unidad_almacenamiento5_numero_serie_input.text(),
            self.Unidad_almacenamiento6_marca_input.text(),
            self.Unidad_almacenamiento6_modelo_input.text(),
            self.Unidad_almacenamiento6_capacidad_input.text(),
            self.Unidad_almacenamiento6_numero_serie_input.text(),
            self.Unidad_almacenamiento7_marca_input.text(),
            self.Unidad_almacenamiento7_modelo_input.text(),
            self.Unidad_almacenamiento7_capacidad_input.text(),
            self.Unidad_almacenamiento7_numero_serie_input.text(),
            self.Unidad_almacenamiento8_marca_input.text(),
            self.Unidad_almacenamiento8_modelo_input.text(),
            self.Unidad_almacenamiento8_capacidad_input.text(),
            self.Unidad_almacenamiento8_numero_serie_input.text(),
            self.GPU1_marca_input.text(),
            self.GPU1_modelo_input.text(),
            self.GPU1_capacidad_input.text(),
            self.GPU1_numero_serie_input.text(),
            self.GPU2_marca_input.text(),
            self.GPU2_modelo_input.text(),
            self.GPU2_capacidad_input.text(),
            self.GPU2_numero_serie_input.text(),
            self.Unidad_DVD1_marca_input.text(),
            self.Unidad_DVD1_modelo_input.text(),
            self.Unidad_DVD1_capacidad_input.text(),
            self.Unidad_DVD1_numero_serie_input.text(),
            self.Unidad_DVD2_marca_input.text(),
            self.Unidad_DVD2_modelo_input.text(),
            self.Unidad_DVD2_capacidad_input.text(),
            self.Unidad_DVD2_numero_serie_input.text()
    ]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return  # No cerrar el diálogo si hay campos vacíos

    # Si todos los campos están llenos, cerrar el diálogo
        super().accept()
        

   
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= InputWindowHojaVida()
    window.show()
    sys.exit(app.exec_())
