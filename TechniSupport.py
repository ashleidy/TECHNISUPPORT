import os
import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTabWidget, QDesktopWidget
)
from PyQt5.QtGui import QIcon

from class_Tab1 import Tab1
from class_Tab2 import Tab2
from class_Tab3 import Tab3
from class_Tab4 import Tab4


class DatabaseTabs(QMainWindow):
    def __init__(self, connection_data):
        super().__init__()
        self.connection_data = connection_data

        self.setWindowTitle("BASES DE DATOS")
        self.resize(1000, 800)

        # Ruta absoluta al icono
        icon_path = "C:/Users/Ashleidy/Desktop/TechniSupport/Registro.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"El archivo de ícono no existe en: {icon_path}")

        # Crear el widget de pestañas
        self.tabs = QTabWidget()

        # Agregar pestañas
        self.tabs.addTab(Tab1(connection_data), "FORMULARIO USUARIO")
        self.tabs.addTab(Tab2(connection_data), "FORMULARIO CUV")
        self.tabs.addTab(Tab3(connection_data), " FORMULARIO DIAGNOSTICO")
        self.tabs.addTab(Tab4(connection_data), " GENERACIÓN DE DOCUMENTOS")

        self.setCentralWidget(self.tabs)

        # Centrar la ventana al final, cuando ya tiene tamaño definido
        self._center_window()

    def _center_window(self):
        """Centra la ventana en la pantalla disponible."""
        screen = QDesktopWidget().availableGeometry()
        size = self.frameGeometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )


def main():
    # Soporte de alta DPI (debe ir ANTES de crear QApplication)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    # Ruta absoluta al icono
    icon_path = "C:/Users/Ashleidy/Desktop/TechniSupport/Registro.ico"
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    else:
        print(f"El archivo de ícono no existe en: {icon_path}")

    # Base de datos SQLite local
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "technisupport.db")
    connection_data = {
        "host": "",
        "user": "",
        "password": "",
        "database": db_path
    }

    try:
        conn = sqlite3.connect(db_path)
        conn.close()

        mainWindow = DatabaseTabs(connection_data)
        mainWindow.show()

        # Forzar repintado correcto antes del mensaje
        app.processEvents()

        QMessageBox.information(
            mainWindow,
            "Conexión exitosa",
            f"Base de datos SQLite local lista:\n{db_path}"
        )
        sys.exit(app.exec_())

    except sqlite3.Error as err:
        QMessageBox.critical(
            None,
            "Error de base de datos",
            f"No se pudo abrir/crear la base de datos: {err}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()