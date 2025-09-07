
# 🧮 Calculator App (PyQt6)

A modern, stylish calculator built with **PyQt6** that supports **dark/light theme toggle**, animated button presses, and a smooth user interface.  

---

## ✨ Features
- ✅ **Basic Arithmetic** → Addition, subtraction, multiplication, division  
- ✅ **Extra Functions** → Clear (C), All Clear (AC), Parentheses `()` and decimal point  
- ✅ **Dark/Light Mode** → Switch themes with a 🌙/🌞 toggle button  
- ✅ **Animated Buttons** → Each button press bounces for a smooth user experience  
- ✅ **Gradient Backgrounds** → Clean, modern light & dark gradient themes  
- ✅ **Fixed Layout** → Prevents overlapping with neat grid spacing  

---

## 📂 Project Structure
```

calculator.py   # Main program file

````

---

## 🛠️ Requirements
- Python **3.9+**  
- PyQt6  

Install PyQt6:
```bash
pip install PyQt6
````

---

## ▶️ How to Run

Run the calculator with:

```bash
python calculator.py
```

---

## 🎨 UI Overview

### 🔹 **Light Mode**

* Background: Blue-to-dark gradient
* Buttons: White with gray borders
* Display: White background, dark text

### 🔹 **Dark Mode**

* Background: Gray-to-black gradient
* Buttons: Dark gray with light text
* Display: Black background, white text

---

## 🧩 Code Explanation

### 1. **Imports**

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout, QHBoxLayout
from PyQt6.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
import sys
```

* **PyQt6 Widgets** → UI components (buttons, layouts, display)
* **QFont, QPalette, QLinearGradient, QColor, QBrush** → Styling text and backgrounds
* **Qt, QPropertyAnimation, QEasingCurve** → Alignment and button animations
* **sys** → Required for running PyQt apps

---

### 2. **Main Window**

```python
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calc by Avi ✨")
        self.setFixedSize(400, 550)
        self.dark_mode = False
```

* Creates a **400x550 fixed window** titled *Calc by Avi ✨*
* Default = **light mode**

---

### 3. **Theme Toggle Button**

```python
self.theme_btn = QPushButton("🌙")
self.theme_btn.setFixedSize(40, 40)
self.theme_btn.clicked.connect(self.toggle_theme)
```

* Small **circle button** in the top-right corner
* Switches between **light 🌙 / dark 🌞 mode**

---

### 4. **Display**

```python
self.display = QLineEdit()
self.display.setFont(QFont("monospace", 24))
self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
self.display.setReadOnly(True)
```

* Large **read-only field** for inputs/results
* Right-aligned like a real calculator

---

### 5. **Buttons**

```python
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('C', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('/', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
    ('.', 3, 0), ('0', 3, 1), ('-', 3, 2), ('+', 3, 3),
    ('(', 4, 0), (')', 4, 1), ('=', 4, 2), ('AC', 4, 3),
]
```

* Buttons arranged in a **5x4 grid**
* Includes numbers, operators, clear, all-clear, parentheses, equals

---

### 6. **Button Animation**

```python
animation = QPropertyAnimation(button, b"geometry")
animation.setDuration(120)
animation.setEasingCurve(QEasingCurve.Type.OutBounce)
```

* When pressed, the button **shrinks slightly and bounces back**
* Smooth & interactive feel

---

### 7. **Themes**

* **Light Mode**

```python
gradient.setColorAt(0.0, QColor("#004e92"))
gradient.setColorAt(1.0, QColor("#141E30"))
```

* **Dark Mode**

```python
gradient.setColorAt(0.0, QColor("#232526"))
gradient.setColorAt(1.0, QColor("#414345"))
```

Each theme updates:

* Background gradient
* Button style
* Display colors
* Theme toggle icon 🌙/🌞

---

## 📸 Preview

💡 *Light Mode Example*
🌙 *Dark Mode Example*

---

## 🚀 Future Improvements

* Add **scientific functions** → sin, cos, log, power
* Enable **keyboard input support**
* Add a **fade transition effect** for theme switching

---

## 👨‍💻 Author

**Avijit Roy**
✨ Built with PyQt6 and love 💙

```

---


