# A simple calculator GUI based App
from idlelib.run import MyHandler
from tkinter.font import names

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calc by Avi")
        self.setFixedSize(400, 500)

        # Main widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Display
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 24))
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            """
            background-color: #333;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            """
        )
        self.layout.addWidget(self.display)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        button_layout = QGridLayout()
        self.layout.addLayout(button_layout)

        # Button definitions
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('C', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('/', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('.', 3, 0), ('0', 3, 1), ('-', 3, 2), ('+', 3, 3),
            ('(', 4, 0), (')', 4, 1), ('=', 4, 2), ('AC', 4, 3),
        ]

        # Create buttons dynamically
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 18))
            button.setFixedSize(80, 80)
            button.setStyleSheet(
                """
                QPushButton {
                    background-color: #444;
                    color: white;
                    border: none;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #555;
                }
                QPushButton:pressed {
                    background-color: #666;
                }
                """
            )
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            button_layout.addWidget(button, row, col)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                expression = self.display.text()
                result = eval(expression)  # Evaluate the expression
                self.display.setText(f"{result:.10g}")  # Format result to show exponential when needed
            except Exception:
                self.display.setText("Error")
        elif button_text == "C":
            self.display.setText(self.display.text()[:-1])  # Remove the last character
        elif button_text == "AC":
            self.display.clear()  # Clear the display
        else:
            self.display.setText(self.display.text() + button_text)  # Append button text to display


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

