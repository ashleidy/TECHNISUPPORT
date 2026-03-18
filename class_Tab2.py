# Librerías estándar de Python

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
    QDialog
)
from PyQt5.QtCore import Qt, QDate
from class_InputHojaVida import InputWindowHojaVida
from class_DatabaseManager import DatabaseManager


class Tab2(QWidget):
    def __init__(self,connection_data):
        super().__init__()
        self.db = DatabaseManager(**connection_data)  
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Gestión de Información de Equipos")
        self.resize(800, 600)

        layout = QVBoxLayout(self)

        # Formulario de entrada de datos
        form_layout = QHBoxLayout()

   

        layout.addLayout(form_layout)

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Buscar...")
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_equipo)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(97)
        self.table.setHorizontalHeaderLabels([
                "ID", "Fecha de Ingreso", "Fecha de Entrega", "Tipo", "Marca", "Modelo", 
                "Número de Serie", "Main Board Marca", "Main Board Modelo", "Main Board Número de Serie",
                "WiFi Marca", "WiFi Modelo", "WiFi Número de Serie",
                "Teclado Marca", "Teclado Modelo", "Teclado Número de Serie",
                "CPU1 Marca", "CPU1 Modelo", "CPU1 Número de Serie",
                "CPU2 Marca", "CPU2 Modelo", "CPU2 Número de Serie",
                "PSU Marca", "PSU Modelo", "PSU Capacidad",
                "Pantalla Marca", "Pantalla Modelo", "Pantalla Capacidad", "Pantalla Número de Serie",
                "Batería Marca", "Batería Modelo", "Batería Número de Serie", "Batería Capacidad",
                "RAM1 Marca", "RAM1 Modelo", "RAM1 Capacidad", "RAM1 Número de Serie",
                "RAM2 Marca", "RAM2 Modelo", "RAM2 Capacidad", "RAM2 Número de Serie",
                "RAM3 Marca", "RAM3 Modelo", "RAM3 Capacidad", "RAM3 Número de Serie",
                "RAM4 Marca", "RAM4 Modelo", "RAM4 Capacidad", "RAM4 Número de Serie",
                "Unidad Almacenamiento 1 Marca", "Unidad Almacenamiento 1 Modelo", "Unidad Almacenamiento 1 Capacidad", "Unidad Almacenamiento 1 Número de Serie",
                "Unidad Almacenamiento 2 Marca", "Unidad Almacenamiento 2 Modelo", "Unidad Almacenamiento 2 Capacidad", "Unidad Almacenamiento 2 Número de Serie",
                "Unidad Almacenamiento 3 Marca", "Unidad Almacenamiento 3 Modelo", "Unidad Almacenamiento 3 Capacidad", "Unidad Almacenamiento 3 Número de Serie",
                "Unidad Almacenamiento 4 Marca", "Unidad Almacenamiento 4 Modelo", "Unidad Almacenamiento 4 Capacidad", "Unidad Almacenamiento 4 Número de Serie",
                "Unidad Almacenamiento 5 Marca", "Unidad Almacenamiento 5 Modelo", "Unidad Almacenamiento 5 Capacidad", "Unidad Almacenamiento 5 Número de Serie",
                "Unidad Almacenamiento 6 Marca", "Unidad Almacenamiento 6 Modelo", "Unidad Almacenamiento 6 Capacidad", "Unidad Almacenamiento 6 Número de Serie",
                "Unidad Almacenamiento 7 Marca", "Unidad Almacenamiento 7 Modelo", "Unidad Almacenamiento 7 Capacidad", "Unidad Almacenamiento 7 Número de Serie",
                "Unidad Almacenamiento 8 Marca", "Unidad Almacenamiento 8 Modelo", "Unidad Almacenamiento 8 Capacidad", "Unidad Almacenamiento 8 Número de Serie",
                "GPU1 Marca", "GPU1 Modelo", "GPU1 Capacidad", "GPU1 Número de Serie",
                "GPU2 Marca", "GPU2 Modelo", "GPU2 Capacidad", "GPU2 Número de Serie",
                "Unidad DVD1 Marca", "Unidad DVD1 Modelo", "Unidad DVD1 Capacidad", "Unidad DVD1 Número de Serie",
                "Unidad DVD2 Marca", "Unidad DVD2 Modelo", "Unidad DVD2 Capacidad", "Unidad DVD2 Número de Serie"
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
        self.add_button.clicked.connect(self.open_InputWindow_HojaVida)

        self.update_button = QPushButton("Actualizar")
        self.update_button.clicked.connect(self.update_equipo)

        
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
        records = self.db.fetch_all_equipos()
        for row_idx, row_data in enumerate(records):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def open_InputWindow_HojaVida(self):
        try:
            self.input_window_hoja_vida = InputWindowHojaVida(mode="add")
            result = self.input_window_hoja_vida.exec_()

            if result == QDialog.Accepted:
                
                fecha_ingreso = self.input_window_hoja_vida.fecha_ingreso_input.text()
                fecha_entrega = self.input_window_hoja_vida.fecha_entrega_input.text()
                tipo=self.input_window_hoja_vida.tipo_input.text()
                marca = self.input_window_hoja_vida.marca_input.text()
                modelo = self.input_window_hoja_vida.modelo_input.text()
                numero_de_serie=self.input_window_hoja_vida.numero_serie_input.text()
                main_board_marca=self.input_window_hoja_vida.main_board_marca_input.text()
                main_board_modelo=self.input_window_hoja_vida.main_board_modelo_input.text()
                main_board_numero_serie=self.input_window_hoja_vida.main_board_numero_serie_input.text()
                
                wifi_marca = self.input_window_hoja_vida.wifi_marca_input.text()
                wifi_modelo = self.input_window_hoja_vida.wifi_modelo_input.text()
                wifi_numero_serie = self.input_window_hoja_vida.wifi_numero_serie_input.text()
                teclado_marca = self.input_window_hoja_vida.teclado_marca_input.text()
                teclado_modelo = self.input_window_hoja_vida.teclado_modelo_input.text()
                teclado_numero_serie = self.input_window_hoja_vida.teclado_numero_serie_input.text()
                CPU1_marca = self.input_window_hoja_vida.CPU1_marca_input.text()
                CPU1_modelo = self.input_window_hoja_vida.CPU1_modelo_input.text()
                CPU1_numero_serie = self.input_window_hoja_vida.CPU1_numero_serie_input.text()
                CPU2_marca = self.input_window_hoja_vida.CPU2_marca_input.text()
                CPU2_modelo = self.input_window_hoja_vida.CPU2_modelo_input.text()
                CPU2_numero_serie = self.input_window_hoja_vida.CPU2_numero_serie_input.text()
                psu_marca = self.input_window_hoja_vida.psu_marca_input.text()
                psu_modelo = self.input_window_hoja_vida.psu_modelo_input.text()
                psu_capacidad = self.input_window_hoja_vida.psu_capacidad_input.text()
                pantalla_marca = self.input_window_hoja_vida.pantalla_marca_input.text()
                pantalla_modelo = self.input_window_hoja_vida.pantalla_modelo_input.text()
                pantalla_capacidad = self.input_window_hoja_vida.pantalla_capacidad_input.text()
                pantalla_numero_serie = self.input_window_hoja_vida.pantalla_numero_serie_input.text()
                bateria_marca = self.input_window_hoja_vida.bateria_marca_input.text()
                bateria_modelo = self.input_window_hoja_vida.bateria_modelo_input.text()
                bateria_numero_serie = self.input_window_hoja_vida.bateria_numero_serie_input.text()
                bateria_capacidad = self.input_window_hoja_vida.bateria_capacidad_input.text()
                ram1_marca = self.input_window_hoja_vida.ram1_marca_input.text()
                ram1_modelo = self.input_window_hoja_vida.ram1_modelo_input.text()
                ram1_capacidad = self.input_window_hoja_vida.ram1_capacidad_input.text()
                ram1_numero_serie = self.input_window_hoja_vida.ram1_numero_serie_input.text()
                ram2_marca = self.input_window_hoja_vida.ram2_marca_input.text()
                ram2_modelo = self.input_window_hoja_vida.ram2_modelo_input.text()
                ram2_capacidad = self.input_window_hoja_vida.ram2_capacidad_input.text()
                ram2_numero_serie = self.input_window_hoja_vida.ram2_numero_serie_input.text()
                ram3_marca = self.input_window_hoja_vida.ram3_marca_input.text()
                ram3_modelo = self.input_window_hoja_vida.ram3_modelo_input.text()
                ram3_capacidad = self.input_window_hoja_vida.ram3_capacidad_input.text()
                ram3_numero_serie = self.input_window_hoja_vida.ram3_numero_serie_input.text()
                ram4_marca = self.input_window_hoja_vida.ram4_marca_input.text()
                ram4_modelo = self.input_window_hoja_vida.ram4_modelo_input.text()
                ram4_capacidad = self.input_window_hoja_vida.ram4_capacidad_input.text()
                ram4_numero_serie = self.input_window_hoja_vida.ram4_numero_serie_input.text()
                Unidad_almacenamiento1_marca = self.input_window_hoja_vida.Unidad_almacenamiento1_marca_input.text()
                Unidad_almacenamiento1_modelo = self.input_window_hoja_vida.Unidad_almacenamiento1_modelo_input.text()
                Unidad_almacenamiento1_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento1_capacidad_input.text()
                Unidad_almacenamiento1_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento1_numero_serie_input.text()
                Unidad_almacenamiento2_marca = self.input_window_hoja_vida.Unidad_almacenamiento2_marca_input.text()
                Unidad_almacenamiento2_modelo = self.input_window_hoja_vida.Unidad_almacenamiento2_modelo_input.text()
                Unidad_almacenamiento2_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento2_capacidad_input.text()
                Unidad_almacenamiento2_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento2_numero_serie_input.text()
                Unidad_almacenamiento3_marca = self.input_window_hoja_vida.Unidad_almacenamiento3_marca_input.text()
                Unidad_almacenamiento3_modelo = self.input_window_hoja_vida.Unidad_almacenamiento3_modelo_input.text()
                Unidad_almacenamiento3_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento3_capacidad_input.text()
                Unidad_almacenamiento3_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento3_numero_serie_input.text()
                Unidad_almacenamiento4_marca = self.input_window_hoja_vida.Unidad_almacenamiento4_marca_input.text()
                Unidad_almacenamiento4_modelo = self.input_window_hoja_vida.Unidad_almacenamiento4_modelo_input.text()
                Unidad_almacenamiento4_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento4_capacidad_input.text()
                Unidad_almacenamiento4_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento4_numero_serie_input.text()
                Unidad_almacenamiento5_marca = self.input_window_hoja_vida.Unidad_almacenamiento5_marca_input.text()
                Unidad_almacenamiento5_modelo = self.input_window_hoja_vida.Unidad_almacenamiento5_modelo_input.text()
                Unidad_almacenamiento5_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento5_capacidad_input.text()
                Unidad_almacenamiento5_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento5_numero_serie_input.text()
                Unidad_almacenamiento6_marca = self.input_window_hoja_vida.Unidad_almacenamiento6_marca_input.text()
                Unidad_almacenamiento6_modelo = self.input_window_hoja_vida.Unidad_almacenamiento6_modelo_input.text()
                Unidad_almacenamiento6_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento6_capacidad_input.text()
                Unidad_almacenamiento6_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento6_numero_serie_input.text()
                Unidad_almacenamiento7_marca = self.input_window_hoja_vida.Unidad_almacenamiento7_marca_input.text()
                Unidad_almacenamiento7_modelo = self.input_window_hoja_vida.Unidad_almacenamiento7_modelo_input.text()
                Unidad_almacenamiento7_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento7_capacidad_input.text()
                Unidad_almacenamiento7_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento7_numero_serie_input.text()
                Unidad_almacenamiento8_marca = self.input_window_hoja_vida.Unidad_almacenamiento8_marca_input.text()
                Unidad_almacenamiento8_modelo = self.input_window_hoja_vida.Unidad_almacenamiento8_modelo_input.text()
                Unidad_almacenamiento8_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento8_capacidad_input.text()
                Unidad_almacenamiento8_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento8_numero_serie_input.text()
                GPU1_marca = self.input_window_hoja_vida.GPU1_marca_input.text()
                GPU1_modelo = self.input_window_hoja_vida.GPU1_modelo_input.text()
                GPU1_capacidad = self.input_window_hoja_vida.GPU1_capacidad_input.text()
                GPU1_numero_serie = self.input_window_hoja_vida.GPU1_numero_serie_input.text()
                GPU2_marca = self.input_window_hoja_vida.GPU2_marca_input.text()
                GPU2_modelo = self.input_window_hoja_vida.GPU2_modelo_input.text()
                GPU2_capacidad = self.input_window_hoja_vida.GPU2_capacidad_input.text()
                GPU2_numero_serie = self.input_window_hoja_vida.GPU2_numero_serie_input.text()
                Unidad_DVD1_marca = self.input_window_hoja_vida.Unidad_DVD1_marca_input.text()
                Unidad_DVD1_modelo = self.input_window_hoja_vida.Unidad_DVD1_modelo_input.text()
                Unidad_DVD1_capacidad = self.input_window_hoja_vida.Unidad_DVD1_capacidad_input.text()
                Unidad_DVD1_numero_serie = self.input_window_hoja_vida.Unidad_DVD1_numero_serie_input.text()
                Unidad_DVD2_marca = self.input_window_hoja_vida.Unidad_DVD2_marca_input.text()
                Unidad_DVD2_modelo = self.input_window_hoja_vida.Unidad_DVD2_modelo_input.text()
                Unidad_DVD2_capacidad = self.input_window_hoja_vida.Unidad_DVD2_capacidad_input.text()
                Unidad_DVD2_numero_serie = self.input_window_hoja_vida.Unidad_DVD2_numero_serie_input.text()

            

                try:
                    self.add_equipo(fecha_ingreso,fecha_entrega, tipo, marca, modelo,numero_de_serie,main_board_marca,main_board_modelo,main_board_numero_serie,
                                    wifi_marca, wifi_modelo, wifi_numero_serie, teclado_marca, teclado_modelo, teclado_numero_serie,
                                    CPU1_marca, CPU1_modelo, CPU1_numero_serie, CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                                    psu_marca, psu_modelo, psu_capacidad, pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                                    bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                                    ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie, ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                                    ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie, ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                                    Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo, Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                                    Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo, Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                                    Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo, Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                                    Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo, Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                                    Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo, Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                                    Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo, Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                                    Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo, Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                                    Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo, Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                                    GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie, GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                                    Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                                    Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie
                                    )
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error al agregar el registro: {str(e)}")
            else:
                return

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir la ventana: {str(e)}")

 
            
    def add_equipo(self,fecha_ingreso,fecha_entrega, tipo, marca, modelo,numero_de_serie,main_board_marca,main_board_modelo,main_board_numero_serie,
                wifi_marca, wifi_modelo, wifi_numero_serie, teclado_marca, teclado_modelo, teclado_numero_serie,
                CPU1_marca, CPU1_modelo, CPU1_numero_serie, CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                psu_marca, psu_modelo, psu_capacidad, pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie, ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie, ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo, Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo, Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo, Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo, Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo, Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo, Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo, Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo, Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie, GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie):
        try:
            result = self.db.add_equipo(fecha_ingreso,fecha_entrega, tipo, marca, modelo,numero_de_serie,main_board_marca,main_board_modelo,main_board_numero_serie,
                                        wifi_marca, wifi_modelo, wifi_numero_serie, teclado_marca, teclado_modelo, teclado_numero_serie,
                                        CPU1_marca, CPU1_modelo, CPU1_numero_serie, CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                                        psu_marca, psu_modelo, psu_capacidad, pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                                        bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                                        ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie, ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                                        ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie, ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                                        Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo, Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                                        Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo, Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                                        Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo, Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                                        Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo, Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                                        Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo, Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                                        Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo, Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                                        Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo, Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                                        Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo, Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                                        GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie, GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                                        Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                                        Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie)
            if result is True:
                self.load_data()
                QMessageBox.information(self, "Éxito", "Registro agregado correctamente.")
            elif isinstance(result, str):  # Si es un mensaje de error
                QMessageBox.warning(self, "Advertencia", result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al agregar el registro: {str(e)}")


    def update_equipo(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "Selecciona un registro para actualizar.")
            return

        try:
             
            
            id_Hoja_vida_equipo = self.table.item(selected_row, 0).text()
            fecha_ingreso = self.table.item(selected_row, 1).text()
            fecha_entrega = self.table.item(selected_row, 2).text()
            tipo = self.table.item(selected_row, 3).text()
            marca = self.table.item(selected_row, 4).text()
            modelo = self.table.item(selected_row, 5).text()
            numero_serie= self.table.item(selected_row, 6).text()
            main_board_marca= self.table.item(selected_row, 7).text()
            main_board_modelo= self.table.item(selected_row, 8).text()
            main_board_numero_serie=self.table.item(selected_row, 9).text()
            wifi_marca=self.table.item(selected_row, 10).text()
            wifi_modelo=self.table.item(selected_row, 11).text()
            wifi_numero_serie=self.table.item(selected_row, 12).text()
            teclado_marca=self.table.item(selected_row, 13).text()
            teclado_modelo=self.table.item(selected_row, 14).text()
            teclado_numero_serie =self.table.item(selected_row, 15).text()
            CPU1_marca=self.table.item(selected_row, 16).text()
            CPU1_modelo =self.table.item(selected_row, 17).text()
            CPU1_numero_serie =self.table.item(selected_row, 18).text()
            CPU2_marca =self.table.item(selected_row, 19).text()
            CPU2_modelo =self.table.item(selected_row, 20).text()
            CPU2_numero_serie =self.table.item(selected_row, 21).text()

            psu_marca =self.table.item(selected_row, 22).text()
            psu_modelo =self.table.item(selected_row, 23).text()
            psu_capacidad = self.table.item(selected_row, 24).text()
            # Corregido para obtener los valores correctos de la tabla
            pantalla_marca = self.table.item(selected_row, 25).text()
            pantalla_modelo = self.table.item(selected_row, 26).text()
            pantalla_capacidad = self.table.item(selected_row, 27).text()
            pantalla_numero_serie = self.table.item(selected_row, 28).text()

            bateria_marca = self.table.item(selected_row, 29).text()
            bateria_modelo = self.table.item(selected_row, 30).text()
            bateria_numero_serie = self.table.item(selected_row, 31).text()
            bateria_capacidad = self.table.item(selected_row, 32).text()

            ram1_marca = self.table.item(selected_row, 33).text()
            ram1_modelo = self.table.item(selected_row, 34).text()
            ram1_capacidad = self.table.item(selected_row, 35).text()
            ram1_numero_serie = self.table.item(selected_row, 36).text()

            ram2_marca = self.table.item(selected_row, 37).text()
            ram2_modelo = self.table.item(selected_row, 38).text()
            ram2_capacidad = self.table.item(selected_row, 39).text()
            ram2_numero_serie = self.table.item(selected_row, 40).text()

            ram3_marca = self.table.item(selected_row, 41).text()
            ram3_modelo = self.table.item(selected_row, 42).text()
            ram3_capacidad = self.table.item(selected_row, 43).text()
            ram3_numero_serie = self.table.item(selected_row, 44).text()

            ram4_marca = self.table.item(selected_row, 45).text()
            ram4_modelo = self.table.item(selected_row, 46).text()
            ram4_capacidad = self.table.item(selected_row, 47).text()
            ram4_numero_serie = self.table.item(selected_row, 48).text()

            Unidad_almacenamiento1_marca = self.table.item(selected_row, 49).text()
            Unidad_almacenamiento1_modelo = self.table.item(selected_row, 50).text()
            Unidad_almacenamiento1_capacidad = self.table.item(selected_row, 51).text()
            Unidad_almacenamiento1_numero_serie = self.table.item(selected_row, 52).text()

            Unidad_almacenamiento2_marca = self.table.item(selected_row, 53).text()
            Unidad_almacenamiento2_modelo = self.table.item(selected_row, 54).text()
            Unidad_almacenamiento2_capacidad = self.table.item(selected_row, 55).text()
            Unidad_almacenamiento2_numero_serie = self.table.item(selected_row, 56).text()

            Unidad_almacenamiento3_marca = self.table.item(selected_row, 57).text()
            Unidad_almacenamiento3_modelo = self.table.item(selected_row, 58).text()
            Unidad_almacenamiento3_capacidad = self.table.item(selected_row, 59).text()
            Unidad_almacenamiento3_numero_serie = self.table.item(selected_row, 60).text()

            Unidad_almacenamiento4_marca = self.table.item(selected_row, 61).text()
            Unidad_almacenamiento4_modelo = self.table.item(selected_row, 62).text()
            Unidad_almacenamiento4_capacidad = self.table.item(selected_row, 63).text()
            Unidad_almacenamiento4_numero_serie = self.table.item(selected_row, 64).text()

            Unidad_almacenamiento5_marca = self.table.item(selected_row, 65).text()
            Unidad_almacenamiento5_modelo = self.table.item(selected_row, 66).text()
            Unidad_almacenamiento5_capacidad = self.table.item(selected_row, 67).text()
            Unidad_almacenamiento5_numero_serie = self.table.item(selected_row, 68).text()

            Unidad_almacenamiento6_marca = self.table.item(selected_row, 69).text()
            Unidad_almacenamiento6_modelo = self.table.item(selected_row, 70).text()
            Unidad_almacenamiento6_capacidad = self.table.item(selected_row, 71).text()
            Unidad_almacenamiento6_numero_serie = self.table.item(selected_row, 72).text()

            Unidad_almacenamiento7_marca = self.table.item(selected_row, 73).text()
            Unidad_almacenamiento7_modelo = self.table.item(selected_row, 74).text()
            Unidad_almacenamiento7_capacidad = self.table.item(selected_row, 75).text()
            Unidad_almacenamiento7_numero_serie = self.table.item(selected_row, 76).text()

            Unidad_almacenamiento8_marca = self.table.item(selected_row, 77).text()
            Unidad_almacenamiento8_modelo = self.table.item(selected_row, 78).text()
            Unidad_almacenamiento8_capacidad = self.table.item(selected_row, 79).text()
            Unidad_almacenamiento8_numero_serie = self.table.item(selected_row, 80).text()

            GPU1_marca = self.table.item(selected_row, 81).text()
            GPU1_modelo = self.table.item(selected_row, 82).text()
            GPU1_capacidad = self.table.item(selected_row, 83).text()
            GPU1_numero_serie = self.table.item(selected_row, 84).text()

            GPU2_marca = self.table.item(selected_row, 85).text()
            GPU2_modelo = self.table.item(selected_row, 86).text()
            GPU2_capacidad = self.table.item(selected_row, 87).text()
            GPU2_numero_serie = self.table.item(selected_row, 88).text()

            Unidad_DVD1_marca = self.table.item(selected_row, 89).text()
            Unidad_DVD1_modelo = self.table.item(selected_row, 90).text()
            Unidad_DVD1_capacidad = self.table.item(selected_row, 91).text()
            Unidad_DVD1_numero_serie = self.table.item(selected_row, 92).text()

            Unidad_DVD2_marca = self.table.item(selected_row, 93).text()
            Unidad_DVD2_modelo = self.table.item(selected_row, 94).text()
            Unidad_DVD2_capacidad = self.table.item(selected_row, 95).text()
            Unidad_DVD2_numero_serie = self.table.item(selected_row, 96).text()
            
            # Convertir las fechas a objetos QDate
            fecha_ingreso_date = QDate.fromString(fecha_ingreso, "yyyy-MM-dd")  # Ajusta el formato según tu caso
            fecha_entrega_date = QDate.fromString(fecha_entrega, "yyyy-MM-dd")  # Ajusta el formato según tu caso
            

            self.input_window_hoja_vida = InputWindowHojaVida(mode="update")
            
            self.input_window_hoja_vida.fecha_ingreso_input.setDate(fecha_ingreso_date)
            self.input_window_hoja_vida.fecha_entrega_input.setDate(fecha_entrega_date)
            self.input_window_hoja_vida.tipo_input.setText(tipo)
            self.input_window_hoja_vida.marca_input.setText(marca)
            self.input_window_hoja_vida.modelo_input.setText(modelo)
            
            self.input_window_hoja_vida.numero_serie_input.setText(numero_serie)
            self.input_window_hoja_vida.main_board_marca_input.setText(main_board_marca)
            self.input_window_hoja_vida.main_board_modelo_input.setText(main_board_modelo)
            self.input_window_hoja_vida.main_board_numero_serie_input.setText(main_board_numero_serie)
            self.input_window_hoja_vida.wifi_marca_input.setText(wifi_marca)
            self.input_window_hoja_vida.wifi_modelo_input.setText(wifi_modelo)
            self.input_window_hoja_vida.wifi_numero_serie_input.setText(wifi_numero_serie)
            self.input_window_hoja_vida.teclado_marca_input.setText(teclado_marca)
            self.input_window_hoja_vida.teclado_modelo_input.setText(teclado_modelo)
            self.input_window_hoja_vida.teclado_numero_serie_input.setText(teclado_numero_serie)
            self.input_window_hoja_vida.CPU1_marca_input.setText(CPU1_marca)
            self.input_window_hoja_vida.CPU1_modelo_input.setText(CPU1_modelo)
            self.input_window_hoja_vida.CPU1_numero_serie_input.setText(CPU1_numero_serie)
            self.input_window_hoja_vida.CPU2_marca_input.setText(CPU2_marca)
            self.input_window_hoja_vida.CPU2_modelo_input.setText(CPU2_modelo)
            self.input_window_hoja_vida.CPU2_numero_serie_input.setText(CPU2_numero_serie)
            self.input_window_hoja_vida.psu_marca_input.setText(psu_marca)
            self.input_window_hoja_vida.psu_modelo_input.setText(psu_modelo)
            self.input_window_hoja_vida.psu_capacidad_input.setText(psu_capacidad)
            self.input_window_hoja_vida.pantalla_marca_input.setText(pantalla_marca)
            self.input_window_hoja_vida.pantalla_modelo_input.setText(pantalla_modelo)
            self.input_window_hoja_vida.pantalla_capacidad_input.setText(pantalla_capacidad)
            self.input_window_hoja_vida.pantalla_numero_serie_input.setText(pantalla_numero_serie)
            self.input_window_hoja_vida.bateria_marca_input.setText(bateria_marca)
            self.input_window_hoja_vida.bateria_modelo_input.setText(bateria_modelo)
            self.input_window_hoja_vida.bateria_numero_serie_input.setText(bateria_numero_serie)
            self.input_window_hoja_vida.bateria_capacidad_input.setText(bateria_capacidad)
            self.input_window_hoja_vida.ram1_marca_input.setText(ram1_marca)
            self.input_window_hoja_vida.ram1_modelo_input.setText(ram1_modelo)
            self.input_window_hoja_vida.ram1_capacidad_input.setText(ram1_capacidad)
            self.input_window_hoja_vida.ram1_numero_serie_input.setText(ram1_numero_serie)
            self.input_window_hoja_vida.ram2_marca_input.setText(ram2_marca)
            self.input_window_hoja_vida.ram2_modelo_input.setText(ram2_modelo)
            self.input_window_hoja_vida.ram2_capacidad_input.setText(ram2_capacidad)
            self.input_window_hoja_vida.ram2_numero_serie_input.setText(ram2_numero_serie)
            self.input_window_hoja_vida.ram3_marca_input.setText(ram3_marca)
            self.input_window_hoja_vida.ram3_modelo_input.setText(ram3_modelo)
            self.input_window_hoja_vida.ram3_capacidad_input.setText(ram3_capacidad)
            self.input_window_hoja_vida.ram3_numero_serie_input.setText(ram3_numero_serie)
            self.input_window_hoja_vida.ram4_marca_input.setText(ram4_marca)
            self.input_window_hoja_vida.ram4_modelo_input.setText(ram4_modelo)
            self.input_window_hoja_vida.ram4_capacidad_input.setText(ram4_capacidad)
            self.input_window_hoja_vida.ram4_numero_serie_input.setText(ram4_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento1_marca_input.setText(Unidad_almacenamiento1_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento1_modelo_input.setText(Unidad_almacenamiento1_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento1_capacidad_input.setText(Unidad_almacenamiento1_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento1_numero_serie_input.setText(Unidad_almacenamiento1_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento2_marca_input.setText(Unidad_almacenamiento2_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento2_modelo_input.setText(Unidad_almacenamiento2_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento2_capacidad_input.setText(Unidad_almacenamiento2_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento2_numero_serie_input.setText(Unidad_almacenamiento2_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento3_marca_input.setText(Unidad_almacenamiento3_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento3_modelo_input.setText(Unidad_almacenamiento3_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento3_capacidad_input.setText(Unidad_almacenamiento3_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento3_numero_serie_input.setText(Unidad_almacenamiento3_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento4_marca_input.setText(Unidad_almacenamiento4_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento4_modelo_input.setText(Unidad_almacenamiento4_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento4_capacidad_input.setText(Unidad_almacenamiento4_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento4_numero_serie_input.setText(Unidad_almacenamiento4_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento5_marca_input.setText(Unidad_almacenamiento5_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento5_modelo_input.setText(Unidad_almacenamiento5_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento5_capacidad_input.setText(Unidad_almacenamiento5_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento5_numero_serie_input.setText(Unidad_almacenamiento5_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento6_marca_input.setText(Unidad_almacenamiento6_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento6_modelo_input.setText(Unidad_almacenamiento6_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento6_capacidad_input.setText(Unidad_almacenamiento6_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento6_numero_serie_input.setText(Unidad_almacenamiento6_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento7_marca_input.setText(Unidad_almacenamiento7_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento7_modelo_input.setText(Unidad_almacenamiento7_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento7_capacidad_input.setText(Unidad_almacenamiento7_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento7_numero_serie_input.setText(Unidad_almacenamiento7_numero_serie)
            self.input_window_hoja_vida.Unidad_almacenamiento8_marca_input.setText(Unidad_almacenamiento8_marca)
            self.input_window_hoja_vida.Unidad_almacenamiento8_modelo_input.setText(Unidad_almacenamiento8_modelo)
            self.input_window_hoja_vida.Unidad_almacenamiento8_capacidad_input.setText(Unidad_almacenamiento8_capacidad)
            self.input_window_hoja_vida.Unidad_almacenamiento8_numero_serie_input.setText(Unidad_almacenamiento8_numero_serie)
            self.input_window_hoja_vida.GPU1_marca_input.setText(GPU1_marca)
            self.input_window_hoja_vida.GPU1_modelo_input.setText(GPU1_modelo)
            self.input_window_hoja_vida.GPU1_capacidad_input.setText(GPU1_capacidad)
            self.input_window_hoja_vida.GPU1_numero_serie_input.setText(GPU1_numero_serie)
            self.input_window_hoja_vida.GPU2_marca_input.setText(GPU2_marca)
            self.input_window_hoja_vida.GPU2_modelo_input.setText(GPU2_modelo)
            self.input_window_hoja_vida.GPU2_capacidad_input.setText(GPU2_capacidad)
            self.input_window_hoja_vida.GPU2_numero_serie_input.setText(GPU2_numero_serie)
            self.input_window_hoja_vida.Unidad_DVD1_marca_input.setText(Unidad_DVD1_marca)
            self.input_window_hoja_vida.Unidad_DVD1_modelo_input.setText(Unidad_DVD1_modelo)
            self.input_window_hoja_vida.Unidad_DVD1_capacidad_input.setText(Unidad_DVD1_capacidad)
            self.input_window_hoja_vida.Unidad_DVD1_numero_serie_input.setText(Unidad_DVD1_numero_serie)
            self.input_window_hoja_vida.Unidad_DVD2_marca_input.setText(Unidad_DVD2_marca)
            self.input_window_hoja_vida.Unidad_DVD2_modelo_input.setText(Unidad_DVD2_modelo)
            self.input_window_hoja_vida.Unidad_DVD2_capacidad_input.setText(Unidad_DVD2_capacidad)
            self.input_window_hoja_vida.Unidad_DVD2_numero_serie_input.setText(Unidad_DVD2_numero_serie)
          

            result = self.input_window_hoja_vida .exec_()

            if result == QDialog.Accepted:
                fecha_ingreso = self.input_window_hoja_vida.fecha_ingreso_input.date().toString("yyyy-MM-dd")
                fecha_entrega = self.input_window_hoja_vida.fecha_entrega_input.date().toString("yyyy-MM-dd")
                
                tipo=self.input_window_hoja_vida.tipo_input.text()
                marca=self.input_window_hoja_vida.marca_input.text()
                modelo=self.input_window_hoja_vida.modelo_input.text()
            
                numero_serie=self.input_window_hoja_vida.numero_serie_input.text()
                main_board_marca=self.input_window_hoja_vida.main_board_marca_input.text()
                main_board_modelo=self.input_window_hoja_vida.main_board_modelo_input.text()
                main_board_numero_serie=self.input_window_hoja_vida.main_board_numero_serie_input.text()
                
                wifi_marca = self.input_window_hoja_vida.wifi_marca_input.text()
                wifi_modelo = self.input_window_hoja_vida.wifi_modelo_input.text()
                wifi_numero_serie = self.input_window_hoja_vida.wifi_numero_serie_input.text()
                teclado_marca = self.input_window_hoja_vida.teclado_marca_input.text()
                teclado_modelo = self.input_window_hoja_vida.teclado_modelo_input.text()
                teclado_numero_serie = self.input_window_hoja_vida.teclado_numero_serie_input.text()
                CPU1_marca = self.input_window_hoja_vida.CPU1_marca_input.text()
                CPU1_modelo = self.input_window_hoja_vida.CPU1_modelo_input.text()
                CPU1_numero_serie = self.input_window_hoja_vida.CPU1_numero_serie_input.text()
                CPU2_marca = self.input_window_hoja_vida.CPU2_marca_input.text()
                CPU2_modelo = self.input_window_hoja_vida.CPU2_modelo_input.text()
                CPU2_numero_serie = self.input_window_hoja_vida.CPU2_numero_serie_input.text()
                psu_marca = self.input_window_hoja_vida.psu_marca_input.text()
                psu_modelo = self.input_window_hoja_vida.psu_modelo_input.text()
                psu_capacidad = self.input_window_hoja_vida.psu_capacidad_input.text()
                pantalla_marca = self.input_window_hoja_vida.pantalla_marca_input.text()
                pantalla_modelo = self.input_window_hoja_vida.pantalla_modelo_input.text()
                pantalla_capacidad = self.input_window_hoja_vida.pantalla_capacidad_input.text()
                pantalla_numero_serie = self.input_window_hoja_vida.pantalla_numero_serie_input.text()
                bateria_marca = self.input_window_hoja_vida.bateria_marca_input.text()
                bateria_modelo = self.input_window_hoja_vida.bateria_modelo_input.text()
                bateria_numero_serie = self.input_window_hoja_vida.bateria_numero_serie_input.text()
                bateria_capacidad = self.input_window_hoja_vida.bateria_capacidad_input.text()
                ram1_marca = self.input_window_hoja_vida.ram1_marca_input.text()
                ram1_modelo = self.input_window_hoja_vida.ram1_modelo_input.text()
                ram1_capacidad = self.input_window_hoja_vida.ram1_capacidad_input.text()
                ram1_numero_serie = self.input_window_hoja_vida.ram1_numero_serie_input.text()
                ram2_marca = self.input_window_hoja_vida.ram2_marca_input.text()
                ram2_modelo = self.input_window_hoja_vida.ram2_modelo_input.text()
                ram2_capacidad = self.input_window_hoja_vida.ram2_capacidad_input.text()
                ram2_numero_serie = self.input_window_hoja_vida.ram2_numero_serie_input.text()
                ram3_marca = self.input_window_hoja_vida.ram3_marca_input.text()
                ram3_modelo = self.input_window_hoja_vida.ram3_modelo_input.text()
                ram3_capacidad = self.input_window_hoja_vida.ram3_capacidad_input.text()
                ram3_numero_serie = self.input_window_hoja_vida.ram3_numero_serie_input.text()
                ram4_marca = self.input_window_hoja_vida.ram4_marca_input.text()
                ram4_modelo = self.input_window_hoja_vida.ram4_modelo_input.text()
                ram4_capacidad = self.input_window_hoja_vida.ram4_capacidad_input.text()
                ram4_numero_serie = self.input_window_hoja_vida.ram4_numero_serie_input.text()
                Unidad_almacenamiento1_marca = self.input_window_hoja_vida.Unidad_almacenamiento1_marca_input.text()
                Unidad_almacenamiento1_modelo = self.input_window_hoja_vida.Unidad_almacenamiento1_modelo_input.text()
                Unidad_almacenamiento1_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento1_capacidad_input.text()
                Unidad_almacenamiento1_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento1_numero_serie_input.text()
                Unidad_almacenamiento2_marca = self.input_window_hoja_vida.Unidad_almacenamiento2_marca_input.text()
                Unidad_almacenamiento2_modelo = self.input_window_hoja_vida.Unidad_almacenamiento2_modelo_input.text()
                Unidad_almacenamiento2_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento2_capacidad_input.text()
                Unidad_almacenamiento2_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento2_numero_serie_input.text()
                Unidad_almacenamiento3_marca = self.input_window_hoja_vida.Unidad_almacenamiento3_marca_input.text()
                Unidad_almacenamiento3_modelo = self.input_window_hoja_vida.Unidad_almacenamiento3_modelo_input.text()
                Unidad_almacenamiento3_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento3_capacidad_input.text()
                Unidad_almacenamiento3_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento3_numero_serie_input.text()
                Unidad_almacenamiento4_marca = self.input_window_hoja_vida.Unidad_almacenamiento4_marca_input.text()
                Unidad_almacenamiento4_modelo = self.input_window_hoja_vida.Unidad_almacenamiento4_modelo_input.text()
                Unidad_almacenamiento4_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento4_capacidad_input.text()
                Unidad_almacenamiento4_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento4_numero_serie_input.text()
                Unidad_almacenamiento5_marca = self.input_window_hoja_vida.Unidad_almacenamiento5_marca_input.text()
                Unidad_almacenamiento5_modelo = self.input_window_hoja_vida.Unidad_almacenamiento5_modelo_input.text()
                Unidad_almacenamiento5_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento5_capacidad_input.text()
                Unidad_almacenamiento5_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento5_numero_serie_input.text()
                Unidad_almacenamiento6_marca = self.input_window_hoja_vida.Unidad_almacenamiento6_marca_input.text()
                Unidad_almacenamiento6_modelo = self.input_window_hoja_vida.Unidad_almacenamiento6_modelo_input.text()
                Unidad_almacenamiento6_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento6_capacidad_input.text()
                Unidad_almacenamiento6_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento6_numero_serie_input.text()
                Unidad_almacenamiento7_marca = self.input_window_hoja_vida.Unidad_almacenamiento7_marca_input.text()
                Unidad_almacenamiento7_modelo = self.input_window_hoja_vida.Unidad_almacenamiento7_modelo_input.text()
                Unidad_almacenamiento7_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento7_capacidad_input.text()
                Unidad_almacenamiento7_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento7_numero_serie_input.text()
                Unidad_almacenamiento8_marca = self.input_window_hoja_vida.Unidad_almacenamiento8_marca_input.text()
                Unidad_almacenamiento8_modelo = self.input_window_hoja_vida.Unidad_almacenamiento8_modelo_input.text()
                Unidad_almacenamiento8_capacidad = self.input_window_hoja_vida.Unidad_almacenamiento8_capacidad_input.text()
                Unidad_almacenamiento8_numero_serie = self.input_window_hoja_vida.Unidad_almacenamiento8_numero_serie_input.text()
                GPU1_marca = self.input_window_hoja_vida.GPU1_marca_input.text()
                GPU1_modelo = self.input_window_hoja_vida.GPU1_modelo_input.text()
                GPU1_capacidad = self.input_window_hoja_vida.GPU1_capacidad_input.text()
                GPU1_numero_serie = self.input_window_hoja_vida.GPU1_numero_serie_input.text()
                GPU2_marca = self.input_window_hoja_vida.GPU2_marca_input.text()
                GPU2_modelo = self.input_window_hoja_vida.GPU2_modelo_input.text()
                GPU2_capacidad = self.input_window_hoja_vida.GPU2_capacidad_input.text()
                GPU2_numero_serie = self.input_window_hoja_vida.GPU2_numero_serie_input.text()
                Unidad_DVD1_marca = self.input_window_hoja_vida.Unidad_DVD1_marca_input.text()
                Unidad_DVD1_modelo = self.input_window_hoja_vida.Unidad_DVD1_modelo_input.text()
                Unidad_DVD1_capacidad = self.input_window_hoja_vida.Unidad_DVD1_capacidad_input.text()
                Unidad_DVD1_numero_serie = self.input_window_hoja_vida.Unidad_DVD1_numero_serie_input.text()
                Unidad_DVD2_marca = self.input_window_hoja_vida.Unidad_DVD2_marca_input.text()
                Unidad_DVD2_modelo = self.input_window_hoja_vida.Unidad_DVD2_modelo_input.text()
                Unidad_DVD2_capacidad = self.input_window_hoja_vida.Unidad_DVD2_capacidad_input.text()
                Unidad_DVD2_numero_serie = self.input_window_hoja_vida.Unidad_DVD2_numero_serie_input.text()
                
                

                if not all([fecha_ingreso , fecha_entrega, tipo, marca, modelo,  numero_serie,main_board_marca,main_board_modelo, main_board_numero_serie, 
                            wifi_marca, wifi_modelo, wifi_numero_serie, teclado_marca, teclado_modelo, teclado_numero_serie,
                            CPU1_marca, CPU1_modelo, CPU1_numero_serie, CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                            psu_marca, psu_modelo, psu_capacidad, pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                            bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                            ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie, ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                            ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie, ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                            Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo, Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                            Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo, Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                            Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo, Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                            Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo, Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                            Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo, Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                            Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo, Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                            Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo, Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                            Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo, Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                            GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie, GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                            Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                            Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie
                            
                            ]):
                    QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
                    return

                self.db.update_equipo(id_Hoja_vida_equipo ,fecha_ingreso , fecha_entrega, tipo, marca, modelo, numero_serie,main_board_marca,main_board_modelo, main_board_numero_serie,
                                            wifi_marca, wifi_modelo, wifi_numero_serie, teclado_marca, teclado_modelo, teclado_numero_serie,
                                            CPU1_marca, CPU1_modelo, CPU1_numero_serie, CPU2_marca, CPU2_modelo, CPU2_numero_serie,
                                            psu_marca, psu_modelo, psu_capacidad, pantalla_marca, pantalla_modelo, pantalla_capacidad, pantalla_numero_serie,
                                            bateria_marca, bateria_modelo, bateria_numero_serie, bateria_capacidad,
                                            ram1_marca, ram1_modelo, ram1_capacidad, ram1_numero_serie, ram2_marca, ram2_modelo, ram2_capacidad, ram2_numero_serie,
                                            ram3_marca, ram3_modelo, ram3_capacidad, ram3_numero_serie, ram4_marca, ram4_modelo, ram4_capacidad, ram4_numero_serie,
                                            Unidad_almacenamiento1_marca, Unidad_almacenamiento1_modelo, Unidad_almacenamiento1_capacidad, Unidad_almacenamiento1_numero_serie,
                                            Unidad_almacenamiento2_marca, Unidad_almacenamiento2_modelo, Unidad_almacenamiento2_capacidad, Unidad_almacenamiento2_numero_serie,
                                            Unidad_almacenamiento3_marca, Unidad_almacenamiento3_modelo, Unidad_almacenamiento3_capacidad, Unidad_almacenamiento3_numero_serie,
                                            Unidad_almacenamiento4_marca, Unidad_almacenamiento4_modelo, Unidad_almacenamiento4_capacidad, Unidad_almacenamiento4_numero_serie,
                                            Unidad_almacenamiento5_marca, Unidad_almacenamiento5_modelo, Unidad_almacenamiento5_capacidad, Unidad_almacenamiento5_numero_serie,
                                            Unidad_almacenamiento6_marca, Unidad_almacenamiento6_modelo, Unidad_almacenamiento6_capacidad, Unidad_almacenamiento6_numero_serie,
                                            Unidad_almacenamiento7_marca, Unidad_almacenamiento7_modelo, Unidad_almacenamiento7_capacidad, Unidad_almacenamiento7_numero_serie,
                                            Unidad_almacenamiento8_marca, Unidad_almacenamiento8_modelo, Unidad_almacenamiento8_capacidad, Unidad_almacenamiento8_numero_serie,
                                            GPU1_marca, GPU1_modelo, GPU1_capacidad, GPU1_numero_serie, GPU2_marca, GPU2_modelo, GPU2_capacidad, GPU2_numero_serie,
                                            Unidad_DVD1_marca, Unidad_DVD1_modelo, Unidad_DVD1_capacidad, Unidad_DVD1_numero_serie,
                                            Unidad_DVD2_marca, Unidad_DVD2_modelo, Unidad_DVD2_capacidad, Unidad_DVD2_numero_serie
                                      
                                      )
                self.load_data()
                QMessageBox.information(self, "Éxito", "Registro actualizado correctamente.")
            else:
                QMessageBox.information(self, "Cancelado", "Actualización cancelada.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al abrir la ventana o actualizar el registro: {e}")

   
        

            
    def eliminar(self):
        
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "Selecciona un registro para eliminar.")
            return

        id_Hoja_vida_equipo = self.table.item(selected_row, 0).text()

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
            resultado = self.db.delete_equipo(id_Hoja_vida_equipo)

            # Verificar si la eliminación fue exitosa
            if resultado["success"]:
                self.load_data()
                QMessageBox.information(self, "Éxito", resultado["message"])
            else:
                QMessageBox.warning(self, "Error", resultado["message"])

    def search_equipo(self):
        search_term = self.search_bar.text()
        results = self.db.search_equipo(search_term)
        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(results):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                
    def get_record_data(self):
        try:
            # Solicitar fecha de ingreso
            fecha_ingreso, ok = QInputDialog.getText(self, "Fecha Ingreso", "Fecha de ingreso (YYYY-MM-DD):")
            if not ok or not fecha_ingreso:
                return None

            # Solicitar fecha de entrega
            fecha_entrega, ok = QInputDialog.getText(self, "Fecha Entrega", "Fecha de entrega (YYYY-MM-DD):")
            if not ok or not fecha_entrega:
                return None

            # Solicitar tipo
            tipo, ok = QInputDialog.getText(self, "Tipo", "Tipo:")
            if not ok or not tipo:
                return None

            # Solicitar marca
            marca, ok = QInputDialog.getText(self, "Marca", "Marca:")
            if not ok or not marca:
                return None

            # Solicitar modelo
            modelo, ok = QInputDialog.getText(self, "Modelo", "Modelo:")
            if not ok or not modelo:
                return None

            # Solicitar número de serie
            numero_serie, ok = QInputDialog.getText(self, "Número de serie", "Número de Serie:")
            if not ok or not numero_serie:
                return None

            # Solicitar marca de la tarjeta principal
            main_board_marca, ok = QInputDialog.getText(self, "Main Board Marca:", "Main Board Marca:")
            if not ok or not main_board_marca:
                return None

            # Solicitar modelo de la tarjeta principal
            main_board_modelo, ok = QInputDialog.getText(self, "Main Board Modelo:", "Main Board Modelo:")
            if not ok or not main_board_modelo:
                return None

            # Solicitar número de serie de la tarjeta principal
            main_board_numero_serie, ok = QInputDialog.getText(self, "Main Board Número de Serie: ", "Main Board Número de Serie:")
            if not ok or not main_board_numero_serie:
                return None
            
            
        # Solicitar datos de WiFi
            wifi_marca, ok = QInputDialog.getText(self, "WiFi Marca", "WiFi Marca:")
            if not ok or not wifi_marca:
                return None

            wifi_modelo, ok = QInputDialog.getText(self, "WiFi Modelo", "WiFi Modelo:")
            if not ok or not wifi_modelo:
                return None

            wifi_numero_serie, ok = QInputDialog.getText(self, "WiFi Número de Serie", "WiFi Número de Serie:")
            if not ok or not wifi_numero_serie:
                return None

        # Solicitar datos de Teclado
            teclado_marca, ok = QInputDialog.getText(self, "Teclado Marca", "Teclado Marca:")
            if not ok or not teclado_marca:
                return None

            teclado_modelo, ok = QInputDialog.getText(self, "Teclado Modelo", "Teclado Modelo:")
            if not ok or not teclado_modelo:
                return None

            teclado_numero_serie, ok = QInputDialog.getText(self, "Teclado Número de Serie", "Teclado Número de Serie:")
            if not ok or not teclado_numero_serie:
                return None

        # Solicitar datos de CPU1
            CPU1_marca, ok = QInputDialog.getText(self, "CPU1 Marca", "CPU1 Marca:")
            if not ok or not CPU1_marca:
                return None

            CPU1_modelo, ok = QInputDialog.getText(self, "CPU1 Modelo", "CPU1 Modelo:")
            if not ok or not CPU1_modelo:
                return None

            CPU1_numero_serie, ok = QInputDialog.getText(self, "CPU1 Número de Serie", "CPU1 Número de Serie:")
            if not ok or not CPU1_numero_serie:
                return None

        # Solicitar datos de CPU2
            CPU2_marca, ok = QInputDialog.getText(self, "CPU2 Marca", "CPU2 Marca:")
            if not ok or not CPU2_marca:
                return None

            CPU2_modelo, ok = QInputDialog.getText(self, "CPU2 Modelo", "CPU2 Modelo:")
            if not ok or not CPU2_modelo:
                return None

            CPU2_numero_serie, ok = QInputDialog.getText(self, "CPU2 Número de Serie", "CPU2 Número de Serie:")
            if not ok or not CPU2_numero_serie:
                return None

        # Solicitar datos de PSU
            psu_marca, ok = QInputDialog.getText(self, "PSU Marca", "PSU Marca:")
            if not ok or not psu_marca:
                return None

            psu_modelo, ok = QInputDialog.getText(self, "PSU Modelo", "PSU Modelo:")
            if not ok or not psu_modelo:
                return None

            psu_capacidad, ok = QInputDialog.getText(self, "PSU Capacidad", "PSU Capacidad:")
            if not ok or not psu_capacidad:
                return None

        # Solicitar datos de Pantalla
            pantalla_marca, ok = QInputDialog.getText(self, "Pantalla Marca", "Pantalla Marca:")
            if not ok or not pantalla_marca:
                return None

            pantalla_modelo, ok = QInputDialog.getText(self, "Pantalla Modelo", "Pantalla Modelo:")
            if not ok or not pantalla_modelo:
                return None

            pantalla_capacidad, ok = QInputDialog.getText(self, "Pantalla Capacidad", "Pantalla Capacidad:")
            if not ok or not pantalla_capacidad:
                return None

            pantalla_numero_serie, ok = QInputDialog.getText(self, "Pantalla Número de Serie", "Pantalla Número de Serie:")
            if not ok or not pantalla_numero_serie:
                return None

        # Solicitar datos de Batería
            bateria_marca, ok = QInputDialog.getText(self, "Batería Marca", "Batería Marca:")
            if not ok or not bateria_marca:
                return None

            bateria_modelo, ok = QInputDialog.getText(self, "Batería Modelo", "Batería Modelo:")
            if not ok or not bateria_modelo:
                return None

            bateria_numero_serie, ok = QInputDialog.getText(self, "Batería Número de Serie", "Batería Número de Serie:")
            if not ok or not bateria_numero_serie:
                return None

            bateria_capacidad, ok = QInputDialog.getText(self, "Batería Capacidad", "Batería Capacidad:")
            if not ok or not bateria_capacidad:
                return None

        # Solicitar datos de RAM1
            ram1_marca, ok = QInputDialog.getText(self, "RAM1 Marca", "RAM1 Marca:")
            if not ok or not ram1_marca:
                return None

            ram1_modelo, ok = QInputDialog.getText(self, "RAM1 Modelo", "RAM1 Modelo:")
            if not ok or not ram1_modelo:
                return None

            ram1_capacidad, ok = QInputDialog.getText(self, "RAM1 Capacidad", "RAM1 Capacidad:")
            if not ok or not ram1_capacidad:
                return None

            ram1_numero_serie, ok = QInputDialog.getText(self, "RAM1 Número de Serie", "RAM1 Número de Serie:")
            if not ok or not ram1_numero_serie:
                return None

        # Solicitar datos de RAM2
            ram2_marca, ok = QInputDialog.getText(self, "RAM2 Marca", "RAM2 Marca:")
            if not ok or not ram2_marca:
                return None

            ram2_modelo, ok = QInputDialog.getText(self, "RAM2 Modelo", "RAM2 Modelo:")
            if not ok or not ram2_modelo:
                return None

            ram2_capacidad, ok = QInputDialog.getText(self, "RAM2 Capacidad", "RAM2 Capacidad:")
            if not ok or not ram2_capacidad:
                return None

            ram2_numero_serie, ok = QInputDialog.getText(self, "RAM2 Número de Serie", "RAM2 Número de Serie:")
            if not ok or not ram2_numero_serie:
                return None

        # Solicitar datos de RAM3
            ram3_marca, ok = QInputDialog.getText(self, "RAM3 Marca", "RAM3 Marca:")
            if not ok or not ram3_marca:
                return None

            ram3_modelo, ok = QInputDialog.getText(self, "RAM3 Modelo", "RAM3 Modelo:")
            if not ok or not ram3_modelo:
                return None

            ram3_capacidad, ok = QInputDialog.getText(self, "RAM3 Capacidad", "RAM3 Capacidad:")
            if not ok or not ram3_capacidad:
                return None

            ram3_numero_serie, ok = QInputDialog.getText(self, "RAM3 Número de Serie", "RAM3 Número de Serie:")
            if not ok or not ram3_numero_serie:
                return None

        # Solicitar datos de RAM4
            ram4_marca, ok = QInputDialog.getText(self, "RAM4 Marca", "RAM4 Marca:")
            if not ok or not ram4_marca:
                return None

            ram4_modelo, ok = QInputDialog.getText(self, "RAM4 Modelo", "RAM4 Modelo:")
            if not ok or not ram4_modelo:
                return None

            ram4_capacidad, ok = QInputDialog.getText(self, "RAM4 Capacidad", "RAM4 Capacidad:")
            if not ok or not ram4_capacidad:
                return None

            ram4_numero_serie, ok = QInputDialog.getText(self, "RAM4 Número de Serie", "RAM4 Número de Serie:")
            if not ok or not ram4_numero_serie:
                return None

            # Solicitar datos de Unidad de Almacenamiento 1
            Unidad_almacenamiento1_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 1 Marca", "Unidad Almacenamiento 1 Marca:")
            if not ok or not Unidad_almacenamiento1_marca:
                return None

            Unidad_almacenamiento1_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 1 Modelo", "Unidad Almacenamiento 1 Modelo:")
            if not ok or not Unidad_almacenamiento1_modelo:
                return None

            Unidad_almacenamiento1_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 1 Capacidad", "Unidad Almacenamiento 1 Capacidad:")
            if not ok or not Unidad_almacenamiento1_capacidad:
                return None

            Unidad_almacenamiento1_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 1 Número de Serie", "Unidad Almacenamiento 1 Número de Serie:")
            if not ok or not Unidad_almacenamiento1_numero_serie:
                return None

            # Solicitar datos de Unidad de Almacenamiento 2
            Unidad_almacenamiento2_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 2 Marca", "Unidad Almacenamiento 2 Marca:")
            if not ok or not Unidad_almacenamiento2_marca:
                return None

            Unidad_almacenamiento2_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 2 Modelo", "Unidad Almacenamiento 2 Modelo:")
            if not ok or not Unidad_almacenamiento2_modelo:
                return None

            Unidad_almacenamiento2_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 2 Capacidad", "Unidad Almacenamiento 2 Capacidad:")
            if not ok or not Unidad_almacenamiento2_capacidad:
                return None

            Unidad_almacenamiento2_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 2 Número de Serie", "Unidad Almacenamiento 2 Número de Serie:")
            if not ok or not Unidad_almacenamiento2_numero_serie:
                return None

            # Solicitar datos de Unidad de Almacenamiento 3
            Unidad_almacenamiento3_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 3 Marca", "Unidad Almacenamiento 3 Marca:")
            if not ok or not Unidad_almacenamiento3_marca:
                return None

            Unidad_almacenamiento3_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 3 Modelo", "Unidad Almacenamiento 3 Modelo:")
            if not ok or not Unidad_almacenamiento3_modelo:
                return None

            Unidad_almacenamiento3_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 3 Capacidad", "Unidad Almacenamiento 3 Capacidad:")
            if not ok or not Unidad_almacenamiento3_capacidad:
                return None

            Unidad_almacenamiento3_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 3 Número de Serie", "Unidad Almacenamiento 3 Número de Serie:")
            if not ok or not Unidad_almacenamiento3_numero_serie:
                return None

            # Solicitar datos de Unidad de Almacenamiento 4
            Unidad_almacenamiento4_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 4 Marca", "Unidad Almacenamiento 4 Marca:")
            if not ok or not Unidad_almacenamiento4_marca:
                return None

            Unidad_almacenamiento4_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 4 Modelo", "Unidad Almacenamiento 4 Modelo:")
            if not ok or not Unidad_almacenamiento4_modelo:
                return None

            Unidad_almacenamiento4_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 4 Capacidad", "Unidad Almacenamiento 4 Capacidad:")
            if not ok or not Unidad_almacenamiento4_capacidad:
                return None

            Unidad_almacenamiento4_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 4 Número de Serie", "Unidad Almacenamiento 4 Número de Serie:")
            if not ok or not Unidad_almacenamiento4_numero_serie:
                return None

            # Solicitar datos de Unidad de Almacenamiento 5
            Unidad_almacenamiento5_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 5 Marca", "Unidad Almacenamiento 5 Marca:")
            if not ok or not Unidad_almacenamiento5_marca:
                return None

            Unidad_almacenamiento5_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 5 Modelo", "Unidad Almacenamiento 5 Modelo:")
            if not ok or not Unidad_almacenamiento5_modelo:
                return None

            Unidad_almacenamiento5_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 5 Capacidad", "Unidad Almacenamiento 5 Capacidad:")
            if not ok or not Unidad_almacenamiento5_capacidad:
                return None

            Unidad_almacenamiento5_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 5 Número de Serie", "Unidad Almacenamiento 5 Número de Serie:")
            if not ok or not Unidad_almacenamiento5_numero_serie:
                return None

            # Solicitar datos de Unidad de Almacenamiento 6
            Unidad_almacenamiento6_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 6 Marca", "Unidad Almacenamiento 6 Marca:")
            if not ok or not Unidad_almacenamiento6_marca:
                return None

            Unidad_almacenamiento6_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 6 Modelo", "Unidad Almacenamiento 6 Modelo:")
            if not ok or not Unidad_almacenamiento6_modelo:
                return None

            Unidad_almacenamiento6_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 6 Capacidad", "Unidad Almacenamiento 6 Capacidad:")
            if not ok or not Unidad_almacenamiento6_capacidad:
                return None
            
            Unidad_almacenamiento6_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 6 Número de Serie", "Unidad Almacenamiento 6 Número de Serie:")
            if not ok or not Unidad_almacenamiento6_numero_serie:
                return None
            
            Unidad_almacenamiento7_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 7 marca", "Unidad Almacenamiento 7 marca:")
            if not ok or not Unidad_almacenamiento7_marca:
                return None
            
            Unidad_almacenamiento7_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 7 Modelo", "Unidad Almacenamiento 7 Modelo:")
            if not ok or not Unidad_almacenamiento7_modelo:
                return None
            
            
            Unidad_almacenamiento7_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 7 Capacidad", "Unidad Almacenamiento 7 Capacidad:")
            if not ok or not Unidad_almacenamiento7_capacidad:
                return None
            
            Unidad_almacenamiento7_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 7 Número de Serie", "Unidad Almacenamiento 7 Número de Serie:")
            if not ok or not Unidad_almacenamiento7_numero_serie:
                return None
            
            Unidad_almacenamiento8_marca, ok = QInputDialog.getText(self, "Unidad Almacenamiento 8 marca", "Unidad Almacenamiento 8 marca:")
            if not ok or not Unidad_almacenamiento8_marca:
                return None
            
            Unidad_almacenamiento8_modelo, ok = QInputDialog.getText(self, "Unidad Almacenamiento 8 Modelo", "Unidad Almacenamiento 8 Modelo:")
            if not ok or not Unidad_almacenamiento8_modelo:
                return None
            
            
            Unidad_almacenamiento8_capacidad, ok = QInputDialog.getText(self, "Unidad Almacenamiento 8 Capacidad", "Unidad Almacenamiento 8 Capacidad:")
            if not ok or not Unidad_almacenamiento8_capacidad:
                return None
            
            Unidad_almacenamiento8_numero_serie, ok = QInputDialog.getText(self, "Unidad Almacenamiento 8 Número de Serie", "Unidad Almacenamiento 8 Número de Serie:")
            if not ok or not Unidad_almacenamiento8_numero_serie:
                return None





            
            
                # Obtener información de la GPU 1
            GPU1_marca, ok = QInputDialog.getText(self, "GPU 1 Marca", "GPU 1 Marca:")
            if not ok or not GPU1_marca:
                return None

            GPU1_modelo, ok = QInputDialog.getText(self, "GPU 1 Modelo", "GPU 1 Modelo:")
            if not ok or not GPU1_modelo:
                return None

            GPU1_capacidad, ok = QInputDialog.getText(self, "GPU 1 Capacidad", "GPU 1 Capacidad:")
            if not ok or not GPU1_capacidad:
                return None

            GPU1_numero_serie, ok = QInputDialog.getText(self, "GPU 1 Número de Serie", "GPU 1 Número de Serie:")
            if not ok or not GPU1_numero_serie:
                return None

            # Obtener información de la GPU 2
            GPU2_marca, ok = QInputDialog.getText(self, "GPU 2 Marca", "GPU 2 Marca:")
            if not ok or not GPU2_marca:
                return None

            GPU2_modelo, ok = QInputDialog.getText(self, "GPU 2 Modelo", "GPU 2 Modelo:")
            if not ok or not GPU2_modelo:
                return None

            GPU2_capacidad, ok = QInputDialog.getText(self, "GPU 2 Capacidad", "GPU 2 Capacidad:")
            if not ok or not GPU2_capacidad:
                return None

            GPU2_numero_serie, ok = QInputDialog.getText(self, "GPU 2 Número de Serie", "GPU 2 Número de Serie:")
            if not ok or not GPU2_numero_serie:
                return None

            # Obtener información de la Unidad DVD 1
            Unidad_DVD1_marca, ok = QInputDialog.getText(self, "Unidad DVD 1 Marca", "Unidad DVD 1 Marca:")
            if not ok or not Unidad_DVD1_marca:
                return None

            Unidad_DVD1_modelo, ok = QInputDialog.getText(self, "Unidad DVD 1 Modelo", "Unidad DVD 1 Modelo:")
            if not ok or not Unidad_DVD1_modelo:
                return None

            Unidad_DVD1_capacidad, ok = QInputDialog.getText(self, "Unidad DVD 1 Capacidad", "Unidad DVD 1 Capacidad:")
            if not ok or not Unidad_DVD1_capacidad:
                return None

            Unidad_DVD1_numero_serie, ok = QInputDialog.getText(self, "Unidad DVD 1 Número de Serie", "Unidad DVD 1 Número de Serie:")
            if not ok or not Unidad_DVD1_numero_serie:
                return None

            # Obtener información de la Unidad DVD 2
            Unidad_DVD2_marca, ok = QInputDialog.getText(self, "Unidad DVD 2 Marca", "Unidad DVD 2 Marca:")
            if not ok or not Unidad_DVD2_marca:
                return None

            Unidad_DVD2_modelo, ok = QInputDialog.getText(self, "Unidad DVD 2 Modelo", "Unidad DVD 2 Modelo:")
            if not ok or not Unidad_DVD2_modelo:
                return None

            Unidad_DVD2_capacidad, ok = QInputDialog.getText(self, "Unidad DVD 2 Capacidad", "Unidad DVD 2 Capacidad:")
            if not ok or not Unidad_DVD2_capacidad:
                return None

            Unidad_DVD2_numero_serie, ok = QInputDialog.getText(self, "Unidad DVD 2 Número de Serie", "Unidad DVD 2 Número de Serie:")
            if not ok or not Unidad_DVD2_numero_serie:
                return None


            return (
               fecha_ingreso,
                fecha_entrega,
                tipo,
                marca,
                modelo,
                numero_serie,
                main_board_marca,
                main_board_modelo,
                main_board_numero_serie,
                wifi_marca,
                wifi_modelo,
                wifi_numero_serie,
                teclado_marca,
                teclado_modelo,
                teclado_numero_serie,
                CPU1_marca,
                CPU1_modelo,
                CPU1_numero_serie,
                CPU2_marca,
                CPU2_modelo,
                CPU2_numero_serie,
                psu_marca,
                psu_modelo,
                psu_capacidad,
                pantalla_marca,
                pantalla_modelo,
                pantalla_capacidad,
                pantalla_numero_serie,
                bateria_marca,
                bateria_modelo,
                bateria_numero_serie,
                bateria_capacidad,
                ram1_marca,
                ram1_modelo,
                ram1_capacidad,
                ram1_numero_serie,
                ram2_marca,
                ram2_modelo,
                ram2_capacidad,
                ram2_numero_serie,
                ram3_marca,
                ram3_modelo,
                ram3_capacidad,
                ram3_numero_serie,
                ram4_marca,
                ram4_modelo,
                ram4_capacidad,
                ram4_numero_serie,
                Unidad_almacenamiento1_marca,
                Unidad_almacenamiento1_modelo,
                Unidad_almacenamiento1_capacidad,
                Unidad_almacenamiento1_numero_serie,
                Unidad_almacenamiento2_marca,
                Unidad_almacenamiento2_modelo,
                Unidad_almacenamiento2_capacidad,
                Unidad_almacenamiento2_numero_serie,
                Unidad_almacenamiento3_marca,
                Unidad_almacenamiento3_modelo,
                Unidad_almacenamiento3_capacidad,
                Unidad_almacenamiento3_numero_serie,
                Unidad_almacenamiento4_marca,
                Unidad_almacenamiento4_modelo,
                Unidad_almacenamiento4_capacidad,
                Unidad_almacenamiento4_numero_serie,
                Unidad_almacenamiento5_marca,
                Unidad_almacenamiento5_modelo,
                Unidad_almacenamiento5_capacidad,
                Unidad_almacenamiento5_numero_serie,
                Unidad_almacenamiento6_marca,
                Unidad_almacenamiento6_modelo,
                Unidad_almacenamiento6_capacidad,
                Unidad_almacenamiento6_numero_serie,
                Unidad_almacenamiento7_marca,
                Unidad_almacenamiento7_modelo,
                Unidad_almacenamiento7_capacidad,
                Unidad_almacenamiento7_numero_serie,
                Unidad_almacenamiento8_marca,
                Unidad_almacenamiento8_modelo,
                Unidad_almacenamiento8_capacidad,
                Unidad_almacenamiento8_numero_serie,
                GPU1_marca,
                GPU1_modelo,
                GPU1_capacidad,
                GPU1_numero_serie,
                GPU2_marca,
                GPU2_modelo,
                GPU2_capacidad,
                GPU2_numero_serie,
                Unidad_DVD1_marca,
                Unidad_DVD1_modelo,
                Unidad_DVD1_capacidad,
                Unidad_DVD1_numero_serie,
                Unidad_DVD2_marca,
                Unidad_DVD2_modelo,
                Unidad_DVD2_capacidad,
                Unidad_DVD2_numero_serie
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al obtener los datos: {e}")
            return None
        
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= Tab2()
    window.show()
    sys.exit(app.exec_())
