import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 250, 250)

        self.resultado = QLineEdit()
        self.resultado.setReadOnly(True)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.resultado)

        layout_botones = QGridLayout()
        botones = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0)
        ]

        for texto, fila, columna in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(self.boton_presionado)
            layout_botones.addWidget(boton, fila, columna)

        layout_principal.addLayout(layout_botones)
        self.setLayout(layout_principal)

    def boton_presionado(self):
        texto = self.sender().text()
        if texto == "C":
            self.resultado.clear() 
        elif texto == "=":
            try:
                self.resultado.setText(str(eval(self.resultado.text())))
            except:
                self.resultado.setText("Error")
        else:
            self.resultado.setText(self.resultado.text() + texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())


