from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QLabel


import sys


class DraggableLabel(QLabel):
    """Кастомный QLabel, который можно перетаскивать"""
    def __init__(self, text):
        super().__init__(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: white; font-size: 18px; border: 1px solid gray; padding: 5px;")

    def mousePressEvent(self, event):
        """Начало drag & drop"""
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(self.text())
            drag.setMimeData(mime_data)
            drag.exec(Qt.MoveAction)


class DropWidget(QWidget):
    """Кастомный QWidget, в который можно перетаскивать элементы"""
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setStyleSheet("background-color: #44475a; border: 2px dashed white;")

    def dragEnterEvent(self, event):
        """Разрешаем перетаскивание, если MIME-данные содержат текст"""
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """Обрабатываем дроп и обновляем содержимое"""
        text = event.mimeData().text()
        label = DraggableLabel(text)
        layout = self.layout()
        if layout:
            layout.addWidget(label)
        event.acceptProposedAction()


class Construct(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1204, 899)
        self.setWindowTitle("Drag & Drop Example")

        # Основной виджет и его layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # QStackedWidget с drag & drop
        self.stacked_widget_1 = QStackedWidget()
        self.stacked_widget_2 = QStackedWidget()

        self.stacked_widget_1.setStyleSheet("background-color: #2b303b; border: none;")
        self.stacked_widget_2.setStyleSheet("background-color: #0000; border: none;")

        # Создание страниц
        page1 = DropWidget()
        page1.setLayout(QVBoxLayout())
        label1 = DraggableLabel("Перетащи меня!")
        page1.layout().addWidget(label1)

        page2 = DropWidget()
        page2.setLayout(QVBoxLayout())

        self.stacked_widget_1.addWidget(page1)
        self.stacked_widget_2.addWidget(page2)

        # Добавляем QStackedWidget в основной layout
        layout.addWidget(self.stacked_widget_1)
        layout.addWidget(self.stacked_widget_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Construct()
    window.show()
    sys.exit(app.exec())
