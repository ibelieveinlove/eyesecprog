# -*- coding: utf-8 -*-

from PySide6.QtCore import (Qt, QMimeData, QPoint)
from PySide6.QtGui import (QDrag)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QPushButton, QLabel, QLineEdit,
                              QScrollArea, QFrame, QFileDialog, QMessageBox,
                              QInputDialog, QListWidget, QListWidgetItem)
from PySide6.QtGui import QCursor


class ColumnWidget(QFrame):
    def __init__(self, title, data, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.StyledPanel)
        self.setLineWidth(1)
        self.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                border-radius: 8px;
                padding: 15px;
            }
            QListWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 6px;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #dee2e6;
            }
            QListWidget::item:selected {
                background-color: #e9ecef;
                color: #495057;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Заголовок столбца
        self.title_edit = QLineEdit(title)
        self.title_edit.setObjectName(u"title_edit")
        self.title_edit.setAlignment(Qt.AlignCenter)
        self.title_edit.setStyleSheet(u"""
            QLineEdit {
                font-size: 16px;
                font-weight: bold;
                color: #2b303b;
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 6px;
                padding: 8px;
            }
        """)
        self.layout.addWidget(self.title_edit)

        # Область с данными
        self.list_widget = QListWidget()
        self.list_widget.setObjectName(u"list_widget")
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)

        # Добавляем данные
        for item in data:
            list_item = QListWidgetItem(item)
            self.list_widget.addItem(list_item)

        # Кнопки для управления элементами
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(10)
        self.button_layout.setContentsMargins(0, 0, 0, 0)

        self.add_button = QPushButton()
        self.add_button.setObjectName(u"add_button")
        self.add_button.clicked.connect(self.add_item)
        self.add_button.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.add_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.edit_button = QPushButton()
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.clicked.connect(self.edit_item)
        self.edit_button.setStyleSheet(u"""
            QPushButton {
                background-color: #A3BE8C;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #B5D99C;
            }
            QPushButton:pressed {
                background-color: #8FBCBB;
            }
        """)
        self.edit_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.remove_button = QPushButton()
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.clicked.connect(self.remove_items)
        self.remove_button.setStyleSheet(u"""
            QPushButton {
                background-color: #BF616A;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
            QPushButton:pressed {
                background-color: #A94444;
            }
        """)
        self.remove_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.remove_button)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.list_widget)
        self.add_button.setText("Добавить значение")
        self.edit_button.setText("Изменить значение")
        self.remove_button.setText("Удачить значение")

    def add_item(self):
        text, ok = QInputDialog.getText(self, "Добавить элемент", "Введите значение:")
        if ok and text:
            self.list_widget.addItem(text)
            self.parent.update_data()

    def edit_item(self):
        selected = self.list_widget.selectedItems()
        if len(selected) == 1:
            text, ok = QInputDialog.getText(self, "Изменить элемент",
                                          "Введите новое значение:",
                                          text=selected[0].text())
            if ok and text:
                selected[0].setText(text)
                self.parent.update_data()
        elif len(selected) > 1:
            text, ok = QInputDialog.getText(self, "Изменить элементы",
                                          "Введите общее значение для всех выделенных элементов:")
            if ok and text:
                for item in selected:
                    item.setText(text)
                self.parent.update_data()

    def remove_items(self):
        selected = self.list_widget.selectedItems()
        if selected:
            reply = QMessageBox.question(self, "Удаление",
                                       f"Удалить {len(selected)} элементов?",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                for item in selected:
                    self.list_widget.takeItem(self.list_widget.row(item))
                self.parent.update_data()

    def get_items(self):
        return [self.list_widget.item(i).text() for i in range(self.list_widget.count())]

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.position().toPoint() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mime_data = QMimeData()
        index = self.parent.columns_layout.indexOf(self)
        mime_data.setText(str(index))
        drag.setMimeData(mime_data)
        drag.exec(Qt.MoveAction)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Column Manager")
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet(u"""
            QMainWindow {
                background-color: #f5f7fa;
            }
        """)

        # Основные данные
        self.columns = []
        self.file_path = None

        # Главный виджет
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.setCentralWidget(self.centralwidget)

        # Основной layout
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Панель кнопок
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(10)
        self.button_layout.setContentsMargins(0, 0, 0, 0)

        self.open_button = QPushButton()
        self.open_button.setObjectName(u"open_button")
        self.open_button.clicked.connect(self.open_file)
        self.open_button.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.open_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.add_column_button = QPushButton()
        self.add_column_button.setObjectName(u"add_column_button")
        self.add_column_button.clicked.connect(self.add_column)
        self.add_column_button.setStyleSheet(u"""
            QPushButton {
                background-color: #A3BE8C;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #B5D99C;
            }
            QPushButton:pressed {
                background-color: #8FBCBB;
            }
        """)
        self.add_column_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.save_button = QPushButton()
        self.save_button.setObjectName(u"save_button")
        self.save_button.clicked.connect(self.save_data)
        self.save_button.setStyleSheet(u"""
            QPushButton {
                background-color: #D08770;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #EBCB8B;
            }
            QPushButton:pressed {
                background-color: #BF616A;
            }
        """)
        self.save_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.assign_button = QPushButton()
        self.assign_button.setObjectName(u"assign_button")
        self.assign_button.clicked.connect(self.assign_value)
        self.assign_button.setStyleSheet(u"""
            QPushButton {
                background-color: #B48EAD;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
            QPushButton:pressed {
                background-color: #A3BE8C;
            }
        """)
        self.assign_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.button_layout.addWidget(self.open_button)
        self.button_layout.addWidget(self.add_column_button)
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.assign_button)
        self.button_layout.addStretch()

        self.main_layout.addLayout(self.button_layout)

        # Область для столбцов
        self.columns_widget = QWidget()
        self.columns_widget.setObjectName(u"columns_widget")
        self.columns_layout = QHBoxLayout(self.columns_widget)
        self.columns_layout.setSpacing(15)
        self.columns_layout.setContentsMargins(0, 0, 0, 0)

        # Прокрутка для столбцов
        self.scroll = QScrollArea()
        self.scroll.setObjectName(u"scroll")
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.columns_widget)
        self.scroll.setStyleSheet(u"""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                width: 10px;
                background-color: #f1f3f5;
            }
            QScrollBar::handle:vertical {
                background-color: #ced4da;
                border-radius: 5px;
            }
        """)

        self.main_layout.addWidget(self.scroll)

        # Разрешаем drop
        self.setAcceptDrops(True)

        # Инициализация текста
        self.retranslateUi()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        source_index = int(event.mimeData().text())
        source_widget = self.columns_layout.itemAt(source_index).widget()

        # Находим позицию, куда бросаем
        pos = event.position().toPoint()
        target_index = -1

        for i in range(self.columns_layout.count()):
            item = self.columns_layout.itemAt(i)
            widget = item.widget()
            if widget.geometry().contains(pos):
                target_index = i
                break

        if target_index >= 0 and source_index != target_index:
            # Удаляем и вставляем на новое место
            self.columns_layout.removeWidget(source_widget)
            self.columns_layout.insertWidget(target_index, source_widget)

            # Обновляем данные в соответствии с новым порядком
            self.update_data()

            event.acceptProposedAction()

    def update_data(self):
        # Обновляем данные столбцов
        self.columns = []
        for i in range(self.columns_layout.count()):
            widget = self.columns_layout.itemAt(i).widget()
            self.columns.append((widget.title_edit.text(), widget.get_items()))

    def open_file(self):
        file_path = "threat.txt"
        if file_path:
            self.file_path = file_path
            self.load_file()

    def load_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Очищаем текущие столбцы
            while self.columns_layout.count():
                item = self.columns_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            self.columns = []

            # Анализируем количество столбцов
            max_columns = 0
            all_data = []

            for line in lines:
                parts = line.strip().split(' ')
                if len(parts) > max_columns:
                    max_columns = len(parts)
                all_data.append(parts)

            # Создаем список столбцов
            columns_data = [[] for _ in range(max_columns)]

            for parts in all_data:
                for i in range(max_columns):
                    if i < len(parts):
                        columns_data[i].append(parts[i])
                    else:
                        columns_data[i].append('')
            column_names = []
            try:
                with open('columns_names.txt', 'r', encoding='utf-8') as f:
                    column_names = [line.strip() for line in f.readlines()]
            except FileNotFoundError:
                pass
            # Добавляем столбцы
            for i, data in enumerate(columns_data):
                self.add_column_with_data(f"Столбец {i + 1}", data)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {str(e)}")

    def add_column(self):
        # Определяем номер нового столбца
        col_number = self.columns_layout.count() + 1
        self.add_column_with_data(f"Столбец {col_number}", [])

    def add_column_with_data(self, title, data):
        column = ColumnWidget(title, data, self)
        self.columns_layout.addWidget(column)
        self.columns.append((title, data))

    def save_data(self):
        if not self.file_path:
            self.file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt)")
            if not self.file_path:
                return

        try:
            self.update_data()

            # Собираем данные для сохранения
            max_rows = max(len(col[1]) for col in self.columns) if self.columns else 0

            lines = []
            for i in range(max_rows):
                row_data = []
                for col in self.columns:
                    if i < len(col[1]):
                        row_data.append(col[1][i])
                    else:
                        row_data.append('')
                lines.append(' '.join(row_data) + '\n')

            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)

            column_names = [col[0] for col in self.columns]
            with open('columns_names.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(column_names))

            QMessageBox.information(self, "Сохранено", "Файл успешно сохранен!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")

    def assign_value(self):
        # Собираем уникальные строки с выделением
        selected_rows = set()
        for i in range(self.columns_layout.count()):
            widget = self.columns_layout.itemAt(i).widget()
            for item in widget.list_widget.selectedItems():
                row = widget.list_widget.row(item)
                selected_rows.add(row)

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Не выбрано ни одного элемента")
            return

        col_count = self.columns_layout.count()
        target_col, ok = QInputDialog.getInt(
            self, "Выбор столбца",
            "Введите номер столбца для присвоения (начиная с 1):",
            1, 1, col_count
        )
        if not ok:
            return

        target_col -= 1  # в 0-based

        value, ok = QInputDialog.getText(self, "Значение", "Введите значение для присвоения:")
        if not ok:
            return

        # Получаем нужный столбец
        target_widget = self.columns_layout.itemAt(target_col).widget()

        # Добавляем строки до нужной длины
        for row in selected_rows:
            while target_widget.list_widget.count() <= row:
                target_widget.list_widget.addItem("")

        # Присваиваем значение только по выделенным строкам
        for row in selected_rows:
            target_widget.list_widget.item(row).setText(value)

        self.update_data()
    def retranslateUi(self):
        self.open_button.setText("Открыть файл")
        self.add_column_button.setText("Добавить столбец")
        self.save_button.setText("Сохранить")
        self.assign_button.setText("Присвоить значение")

