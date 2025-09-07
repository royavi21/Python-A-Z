from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout, QHBoxLayout
from PyQt6.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calc by Avi ✨")
        self.setFixedSize(400, 550)

        self.dark_mode = False  # Default = light mode

        # Main widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # ------------------------
        # Top bar (Theme toggle)
        # ------------------------
        top_bar = QHBoxLayout()
        top_bar.addStretch(1)

        self.theme_btn = QPushButton("🌙")
        self.theme_btn.setFixedSize(40, 40)
        self.theme_btn.setFont(QFont("Google", 14))
        self.theme_btn.clicked.connect(self.toggle_theme)
        self.theme_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #ffffff;
                border-radius: 20px;
                border: 1px solid #ddd;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            """
        )
        top_bar.addWidget(self.theme_btn)
        self.layout.addLayout(top_bar)

        # ------------------------
        # Display
        # ------------------------
        self.display = QLineEdit()
        self.display.setFont(QFont("moonospace", 24))
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            """
            background-color: #1f1f1f;
            color: #f5f5f5;
            border: none;
            border-radius: 12px;
            padding: 14px;
            """
        )
        self.layout.addWidget(self.display)

        # ------------------------
        # Buttons
        # ------------------------
        self.create_buttons()

        # Apply light mode at start
        self.apply_dark_mode()

    def create_buttons(self):
        button_layout = QGridLayout()
        button_layout.setSpacing(12)  # Prevent overlap
        self.layout.addLayout(button_layout)

        # Button definitions
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('C', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('/', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('.', 3, 0), ('0', 3, 1), ('-', 3, 2), ('+', 3, 3),
            ('(', 4, 0), (')', 4, 1), ('=', 4, 2), ('AC', 4, 3),
        ]

        self.buttons = {}
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 18))
            button.setFixedSize(80, 70)
            button.clicked.connect(lambda checked, t=text, b=button: self.on_button_click(t, b))
            button_layout.addWidget(button, row, col)
            self.buttons[text] = button

    def on_button_click(self, button_text, button):
        # Animate button press
        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(120)
        animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        rect = button.geometry()
        animation.setStartValue(rect)
        animation.setEndValue(rect.adjusted(2, 2, -2, -2))
        animation.start()

        if button_text == "=":
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(f"{result:.10g}")
            except Exception:
                self.display.setText("Error")
        elif button_text == "C":
            self.display.setText(self.display.text()[:-1])
        elif button_text == "AC":
            self.display.clear()
        else:
            self.display.setText(self.display.text() + button_text)

    # -------------------
    # Theme handling
    # -------------------
    def apply_light_mode(self):
        # Background gradient
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 550)
        gradient.setColorAt(0.0, QColor("#004e92"))
        gradient.setColorAt(1.0, QColor("#141E30"))
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Display
        self.display.setStyleSheet(
            """
            background-color: #ffffff;
            color: #333333;
            border-radius: 12px;
            padding: 14px;
            """
        )

        # Buttons
        for btn in self.buttons.values():
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #ffffff;
                    color: #333333;
                    border: 2px solid #ddd;
                    border-radius: 25px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
                QPushButton:pressed {
                    background-color: #d1e8ff;
                }
                """
            )

        # Theme toggle
        self.theme_btn.setText("🌙")
        self.theme_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #ffffff;
                color: #333333;
                border-radius: 20px;
                border: 1px solid #ddd;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            """
        )

    def apply_dark_mode(self):
        # Dark gradient
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 550)
        gradient.setColorAt(0.0, QColor("#232526"))
        gradient.setColorAt(1.0, QColor("#414345"))
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Display
        self.display.setStyleSheet(
            """
            background-color: #1f1f1f;
            color: #f5f5f5;
            border-radius: 12px;
            padding: 14px;
            """
        )

        # Buttons
        for btn in self.buttons.values():
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #333333;
                    color: #f5f5f5;
                    border: 2px solid #555;
                    border-radius: 25px;
                }
                QPushButton:hover {
                    background-color: #444444;
                }
                QPushButton:pressed {
                    background-color: #666666;
                }
                """
            )

        # Theme toggle
        self.theme_btn.setText("🌞")
        self.theme_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #333333;
                color: #f5f5f5;
                border-radius: 20px;
                border: 1px solid #555;
            }
            QPushButton:hover {
                background-color: #444444;
            }
            """
        )

    def toggle_theme(self):
        if self.dark_mode:
            self.apply_light_mode()
        else:
            self.apply_dark_mode()
        self.dark_mode = not self.dark_mode


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
