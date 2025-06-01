from Flex import Ui_MainWindow
import sys,urllib,pymysql
from pymysql import cursors
from config import core
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget,QWidget, QStackedWidget, QLabel, QFileDialog,QInputDialog,QMessageBox
import untitled, insert, Aunth, Flex,final,robberySystem
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QListWidgetItem,QTableWidgetItem,QListWidget
import random


class TagWidget(QWidget):
    """Виджет для отображения одного столбца данных"""

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)


        random_color = self.generate_random_hex_color()
        # Заголовок столбца
        self.tag_name_label = QLabel(name)
        self.tag_name_label.setStyleSheet(f"""
            QLabel {{
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
                background-color: {random_color};
                color: white;
                border-radius: 5px;
                text-align: center;
            }}
        """)
        self.layout.addWidget(self.tag_name_label)


    def generate_random_hex_color(self):
        """Генерирует случайный цвет в формате HEX (#RRGGBB)"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02X}{g:02X}{b:02X}"


class TagController:
    def __init__(self,ui):
        self.default_tags = ['EyeSec:Network', 'EyeSec:System', 'EyeSec:Virus']
        self.ui = ui
    def load_data_tags(self):
        self.ui.info_vertical_layout_threat.setParent(None)
        for i in self.default_tags:
            tag = TagWidget(str(i))
            self.ui.info_vertical_layout_threat.addWidget(tag)

    def add_new_tag(self):
        name_tag,ok = QInputDialog.getItem(
        self.ui,
        "Добавление нового тэга",
        "Введите название нового тэга:",
        0, False)
        if not ok:
            return
        if name_tag in self.default_tags:
            QMessageBox.warning(self.ui, "Ошибка", "Такой тэг ужесть в списке")
        else:
            self.default_tags.append('EyeSec:' + str(name_tag))
            self.load_data_tags()
            with open("add_new_tag.txt", 'w') as file:
                file.write(str(name_tag))


