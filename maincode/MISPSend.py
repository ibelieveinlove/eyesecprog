import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QListWidget, QListWidgetItem, QMessageBox,
                               QMenu)
from PySide6.QtCore import Qt, QMimeData, QPoint, QRect, Signal
from PySide6.QtGui import QDrag, QPixmap, QPainter, QAction
from PySide6.QtWidgets import QStyleOptionViewItem, QStyle

MISP_CATEGORIES = [
    "Antivirus detection", "Artifacts dropped", "Attribution", "External analysis",
    "Financial fraud", "Internal reference", "Network activity", "Other",
    "Payload delivery", "Payload installation", "Payload type", "Persistence mechanism",
    "Person", "Social engineering", "Support Tool", "Targeting data"
]

MISP_TYPES = [
    "md5", "sha1", "sha256", "filename", "ip-src", "ip-dst",
    "domain", "email-src", "email-dst", "url", "user-agent",
    "regkey", "AS", "vulnerability", "comment", "text",
    "target-user", "target-email", "target-machine", "target-org"
]


class EditableListWidgetItem(QListWidgetItem):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setFlags(self.flags() | Qt.ItemIsEditable)


class DraggableListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(False)
        self.setSelectionMode(QListWidget.SingleSelection)
        self.setDragDropMode(QListWidget.DragOnly)
        self.setDefaultDropAction(Qt.CopyAction)
        self.setStyleSheet("""
            QListWidget {
                background-color: #ffffff;
                border: 1px solid #D8DEE9;
                border-radius: 8px;
                padding: 5px;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #ECEFF4;
            }
            QListWidget::item:hover {
                background-color: #ECEFF4;
            }
            QListWidget::item:selected {
                background-color: #5E81AC;
                color: white;
            }
        """)

    def startDrag(self, dropActions):
        drag = QDrag(self)
        mimedata = QMimeData()

        selected_item = self.currentItem()
        if selected_item:
            mimedata.setText(selected_item.text())
            mimedata.setData("application/column-index",
                             str(selected_item.data(Qt.UserRole)).encode())
            drag.setMimeData(mimedata)

            rect = self.visualItemRect(selected_item)
            pixmap = QPixmap(rect.size())
            pixmap.fill(Qt.transparent)

            painter = QPainter(pixmap)
            option = QStyleOptionViewItem()
            option.rect = QRect(QPoint(0, 0), rect.size())
            option.state = QStyle.State_Selected | QStyle.State_Enabled
            option.text = selected_item.text()

            self.style().drawControl(QStyle.CE_ItemViewItem, option, painter)
            painter.end()

            drag.setPixmap(pixmap)
            drag.setHotSpot(QPoint(15, 15))
            drag.exec(Qt.CopyAction)


class DroppableListWidget(QListWidget):
    itemDoubleClicked = Signal(QListWidgetItem)

    def __init__(self, main_window=None, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setAcceptDrops(True)
        self.setDragDropMode(QListWidget.DropOnly)
        self.setDefaultDropAction(Qt.CopyAction)
        self.setStyleSheet("""
            QListWidget {
                background-color: #ffffff;
                border: 2px dashed #D8DEE9;
                border-radius: 8px;
                min-height: 100px;
                min-width: 150px;
                font-size: 14px;
                padding: 5px;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #ECEFF4;
            }
        """)
        self.itemDoubleClicked.connect(self.on_item_double_clicked)

    def on_item_double_clicked(self, item):
        if self.objectName() in ["Type", "Category"]:
            self.show_edit_menu(item)

    def show_edit_menu(self, item):
        menu = QMenu(self)

        if self.objectName() == "Type":
            for type_name in MISP_TYPES:
                action = QAction(type_name, menu)
                action.triggered.connect(lambda checked, t=type_name, i=item: i.setText(t))
                menu.addAction(action)
        elif self.objectName() == "Category":
            for category_name in MISP_CATEGORIES:
                action = QAction(category_name, menu)
                action.triggered.connect(lambda checked, c=category_name, i=item: i.setText(c))
                menu.addAction(action)

        menu.exec_(self.mapToGlobal(self.visualItemRect(item).bottomLeft()))

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/column-index"):
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/column-index"):
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/column-index") and self.main_window:
            event.setDropAction(Qt.CopyAction)
            event.accept()

            column_index = int(event.mimeData().data("application/column-index").data().decode())
            self.clear()

            for row in self.main_window.threat_data_rows:
                if column_index < len(row):
                    item_text = row[column_index]
                    if item_text:
                        item = QListWidgetItem(item_text)
                        self.addItem(item)
        else:
            event.ignore()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Threat Data Mapper")
        self.setMinimumSize(1000, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f7fa;
            }
        """)

        # Central widget
        self.centralwidget = QWidget()
        self.centralwidget.setStyleSheet("background-color: transparent;")
        self.setCentralWidget(self.centralwidget)

        # Main layout
        self.main_layout = QHBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Content area
        self.content_area = QWidget()
        self.content_area.setStyleSheet("background-color: #f8f9fa;")

        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(30, 30, 30, 30)
        self.content_layout.setSpacing(20)

        # Title
        self.title_label = QLabel("Threat Data Mapper")
        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
                padding: 10px;
            }
        """)
        self.content_layout.addWidget(self.title_label)

        # Main content
        self.main_content = QWidget()
        self.main_content.setStyleSheet("background-color: transparent;")

        self.main_content_layout = QHBoxLayout(self.main_content)
        self.main_content_layout.setContentsMargins(0, 0, 0, 0)
        self.main_content_layout.setSpacing(20)

        # Left panel (3/4 width)
        self.left_panel = QWidget()
        self.left_panel.setStyleSheet("background-color: transparent;")

        self.left_layout = QHBoxLayout(self.left_panel)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setSpacing(15)

        # Left side columns
        self.left_columns = {}
        for column in ["Category", "Type", "Value", "Comment"]:
            column_widget = QWidget()
            column_widget.setStyleSheet("""
                QWidget {
                    background-color: #ffffff;
                    border-radius: 12px;
                    padding: 15px;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
                }
            """)

            column_layout = QVBoxLayout(column_widget)
            column_layout.setContentsMargins(0, 0, 0, 0)
            column_layout.setSpacing(10)

            label = QLabel(column)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("""
                QLabel {
                    font-weight: bold; 
                    font-size: 16px;
                    color: #2E3440;
                    padding: 5px;
                }
            """)

            list_widget = DroppableListWidget(main_window=self)
            list_widget.setObjectName(column)

            column_layout.addWidget(label)
            column_layout.addWidget(list_widget)
            self.left_layout.addWidget(column_widget)

            self.left_columns[column] = list_widget

        self.main_content_layout.addWidget(self.left_panel, 3)

        # Right panel (1/4 width)
        self.right_panel = QWidget()
        self.right_panel.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            }
        """)

        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        self.right_layout.setSpacing(15)

        # Buttons
        button_style = """
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """

        self.load_button = QPushButton("Загрузить данные")
        self.load_button.setStyleSheet(button_style)
        self.load_button.clicked.connect(self.load_data)
        self.right_layout.addWidget(self.load_button)

        self.send_button = QPushButton("Отправить в MISP")
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5FB864;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            QPushButton:pressed {
                background-color: #3D8B40;
            }
        """)
        self.send_button.clicked.connect(lambda: print("Отправка в MISP"))
        self.right_layout.addWidget(self.send_button)

        # Columns label
        columns_label = QLabel("Доступные столбцы:")
        columns_label.setStyleSheet("""
            QLabel {
                font-weight: bold; 
                font-size: 16px;
                color: #2E3440;
                padding-top: 15px;
            }
        """)
        self.right_layout.addWidget(columns_label)

        # Columns list
        self.columns_list = DraggableListWidget()
        self.right_layout.addWidget(self.columns_list)

        self.right_layout.addStretch(1)
        self.main_content_layout.addWidget(self.right_panel, 1)

        self.content_layout.addWidget(self.main_content, 1)
        self.main_layout.addWidget(self.content_area, 1)

        self.threat_data_rows = []
        self.column_indices = {}

    def load_data(self):
        self.columns_list.clear()
        for column in self.left_columns.values():
            column.clear()
        self.threat_data_rows = []
        self.column_indices = {}

        try:
            # 1. Чтение columns_names.txt
            try:
                with open("columns_names.txt", "r", encoding="utf-8") as f:
                    column_names = [line.strip() for line in f if line.strip()]

                if not column_names:
                    QMessageBox.warning(self, "Ошибка", "Файл columns_names.txt пустой")
                    return

            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось прочитать columns_names.txt:\n{str(e)}")
                return

            # 2. Чтение threat.txt
            try:
                with open("threat.txt", "r", encoding="utf-8") as f:
                    lines = [line.strip() for line in f if line.strip()]

                if not lines:
                    QMessageBox.warning(self, "Ошибка", "Файл threat.txt пустой")
                    return

                self.threat_data_rows = [line.split() for line in lines]

                max_columns = max(len(row) for row in self.threat_data_rows) if self.threat_data_rows else 0
                if len(column_names) > max_columns:
                    QMessageBox.warning(self, "Ошибка",
                                        f"В threat.txt только {max_columns} столбцов, а в columns_names.txt - {len(column_names)}")
                    return

                self.column_indices = {name: i for i, name in enumerate(column_names)}

            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось прочитать threat.txt:\n{str(e)}")
                return

            # 3. Заполняем список доступных столбцов
            self.columns_list.clear()
            for name, pos in self.column_indices.items():
                item = QListWidgetItem(f"{name} (столбец {pos + 1})")
                item.setData(Qt.UserRole, pos)
                self.columns_list.addItem(item)

            # 4. Заполняем столбцы Type и Category пустыми редактируемыми элементами
            for _ in range(len(self.threat_data_rows)):
                # Для столбца Type
                type_item = EditableListWidgetItem("")
                self.left_columns["Type"].addItem(type_item)

                # Для столбца Category
                category_item = EditableListWidgetItem("")
                self.left_columns["Category"].addItem(category_item)

            QMessageBox.information(self, "Успех",
                                    f"Загружено {len(self.threat_data_rows)} строк\n"
                                    f"Доступно столбцов: {len(self.column_indices)}")

        except Exception as e:
            QMessageBox.critical(self, "Критическая ошибка", f"Непредвиденная ошибка:\n{str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())