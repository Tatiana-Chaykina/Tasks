from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import random
import string
from kiwisolver import strength
from CRUD import *
from sqlalchemy.orm import sessionmaker
from gui_def import PasswordStrengthChecker,Generator

class PasswordApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проверка и генерация паролей")
        self.setGeometry(100, 100, 300, 500)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        layout.addWidget(self.password_input)

        self.check_button = QPushButton("Проверка пароля")
        self.check_button.clicked.connect(self.check_password)
        layout.addWidget(self.check_button)

        self.strength_label = QLabel("Здесь будет отображаться надежность пароля.")
        self.strength_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.strength_label)

        self.generate_button = QPushButton("Сгенерировать пароль")
        self.generate_button.clicked.connect(self.open_generator_window)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def check_password(self):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Input Error", "Пожалуйста введите пароль для проверки")
            return
        strength = PasswordStrengthChecker.check_strength(password)
        add_password(password, strength)
        if strength == 0:
            strength = 'Слабый'
        elif strength == 1:
            strength = 'Средний'
        else:
            strength = "Сильный"
        self.strength_label.setText(f"Надежность пароля: {strength}")
    def open_generator_window(self):
        self.generator_window = PasswordGenerator()
        self.generator_window.show()


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генерация пароля")
        self.setGeometry(100, 100, 300, 500)
        self.init_ui()
    def init_ui(self):
        layout = QVBoxLayout()
        self.generated_password_label = QLabel("Нажмите на кнопку для генерации пароля")
        self.generated_password_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.generated_password_label)
        self.generate_button = QPushButton("Сгенерировать пароль")
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)
        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("Длина пароля")
        layout.addWidget(self.length_input)
        self.copy_button = QPushButton("Скопировать пароль")
        self.copy_button.clicked.connect(self.copy_password)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Введите число для длины пароля.")
            return

        if length < 6 or length > 300:
            QMessageBox.warning(self, "Input Error", "Длина пароля должна быть от 6 до 300 символов.")
            return

        password = Generator.generator(length)
        self.generated_password_label.setText(f"Сгенерированный пароль: {password}")
        self.generated_password = password

    def copy_password(self):
        if hasattr(self, 'generated_password'):
            QApplication.clipboard().setText(self.generated_password)
            QMessageBox.information(self, "Успешно скопировано", "Пароль был скопирован в буфер обмена")
        else:
            QMessageBox.warning(self, "Ошибка", "Пароль для копирования отсутствует")


app = QApplication([])
main_window = PasswordApp()
main_window.show()
app.exec_()
