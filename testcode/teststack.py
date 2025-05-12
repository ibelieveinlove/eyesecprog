from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget,
                               QPushButton, QVBoxLayout, QWidget, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Многостраничное приложение")
        self.setGeometry(100, 100, 400, 300)

        # Создаем stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Создаем страницы
        self.create_page1()
        self.create_page2()

        # Добавляем страницы в stacked widget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

    def create_page1(self):
        self.page1 = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Это страница 1")
        btn = QPushButton("Перейти на страницу 2")
        btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        layout.addWidget(label)
        layout.addWidget(btn)
        self.page1.setLayout(layout)

    def create_page2(self):
        self.page2 = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Это страница 2")
        btn = QPushButton("Вернуться на страницу 1")
        btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        layout.addWidget(label)
        layout.addWidget(btn)
        self.page2.setLayout(layout)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()