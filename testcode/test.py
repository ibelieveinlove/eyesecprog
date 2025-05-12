from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Dialog Example")

        layout = QVBoxLayout()

        self.label = QLabel("Файл не выбран")
        layout.addWidget(self.label)

        button = QPushButton("Выбрать файл")
        button.clicked.connect(self.open_file_dialog)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "",
            "Все файлы (*);;Текстовые файлы (*.txt)"
        )

        if file_path:
            self.label.setText(f"Выбран файл: {file_path}")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()