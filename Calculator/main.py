#calculator
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.initUI(width, height)

    def initUI(self, width, height):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, width, height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.result_field = QLineEdit()
        self.result_field.setFixedHeight(50)
        self.layout.addWidget(self.result_field, 0, 0, 1, 4)




        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Кнопки цикл
        row, col = 1, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedSize(60,60)
            btn.clicked.connect(self.on_button_click)
            self.layout.addWidget(btn, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        self.show()

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.result_field.clear()
        elif text == '=':
            try:
                result = eval(self.result_field.text())
                self.result_field.setText(str(result))
            except Exception as e:
                self.result_field.setText('Error')
        else:
            current_text = self.result_field.text()
            new_text = current_text + text
            self.result_field.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)


    width = int(input("Window width: "))
    height = int(input("Windiw height: "))

    calculator = Calculator(width, height)
    sys.exit(app.exec_())
