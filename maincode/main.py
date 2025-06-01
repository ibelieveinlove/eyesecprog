import sys, urllib, pymysql, os, random,openpyxl
from pymysql import cursors
from config import core
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,
                               QStackedWidget, QLabel, QFileDialog, QVBoxLayout,
                               QHBoxLayout, QListWidget, QMessageBox, QInputDialog)
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag, QPixmap
import untitled, insert, Aunth, Flex, final, robberySystem, MISPSend
from database import DatabaseHandler
from pymisp import MISPEvent, MISPObject, PyMISP, ExpandedPyMISP
import pandas as pd


class mispSendWindow(MISPSend.MainWindow):
    def __init__(self, switch_page_callback=None):
        super().__init__()
        self.switch_page = switch_page_callback


class robberyWindow(robberySystem.MainWindow):
    def __init__(self, switch_page_callback=None):
        super().__init__()
        self.switch_page = switch_page_callback


class finalWindow(QMainWindow, final.Ui_MainWindow):
    def __init__(self, switch_page_callback=None):
        super().__init__()
        self.setupUi(self)
        self.switch_page = switch_page_callback


class FlexWindow(QMainWindow, Flex.Ui_MainWindow):
    def __init__(self, switch_page_callback=None):
        super().__init__()
        self.setupUi(self)
        self.switch_page = switch_page_callback


class AunthWindow(QMainWindow, Aunth.Ui_MainWindow):
    def __init__(self, switch_page_callback=None):
        super().__init__()
        self.setupUi(self)
        self.switch_page = switch_page_callback


class InsertWindow(QMainWindow, insert.Ui_MainWindow):
    def __init__(self, switch_page_callback=None):
        super().__init__()
        self.setupUi(self)
        self.switch_page = switch_page_callback


class MainWindow(QMainWindow, untitled.Ui_MainWindow):
    def __init__(self, switch_page_callback=None):
        super().__init__()
        self.setupUi(self)
        self.switch_page = switch_page_callback


class ColumnWidget(QWidget):
    """Виджет для отображения одного столбца данных"""

    def __init__(self, title, data, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)

        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
                background-color: #5E81AC;
                color: white;
                border-radius: 5px;
                text-align: center;
            }
        """)

        self.data_list = QListWidget()
        self.data_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #D8DEE9;
                border-radius: 5px;
                background-color: white;
                min-width: 150px;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #f0f0f0;
            }
        """)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.data_list)
        self.update_data(data)

    def update_data(self, data):
        self.data_list.clear()
        for item in data:
            if item:
                self.data_list.addItem(item)


class DataManager:
    """Класс для работы с данными с учетом формата файлов"""

    def __init__(self):
        self.column_names = []
        self.threat_data = []

    def load_data(self):
        try:
            with open("columns_names.txt", "r", encoding="utf-8") as f:
                self.column_names = [line.strip() for line in f if line.strip()]

            with open("threat.txt", "r", encoding="utf-8") as f:
                self.threat_data = []
                for line in f:
                    line = line.strip()
                    if line:
                        row = line.split(' ')
                        self.threat_data.append(row)

            if not self.column_names:
                raise Exception("Файл columns_names.txt пустой")
            if not self.threat_data:
                raise Exception("Файл threat.txt пустой")

            max_columns = max(len(row) for row in self.threat_data) if self.threat_data else 0
            if len(self.column_names) > max_columns:
                raise Exception(
                    f"В threat.txt найдено {max_columns} столбцов, "
                    f"а в columns_names.txt - {len(self.column_names)}. "
                    "Количество не совпадает."
                )

            return True
        except Exception as e:
            raise Exception(f"Ошибка загрузки данных: {str(e)}")

    def save_data(self):
        try:
            with open("columns_names.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(self.column_names))

            with open("threat.txt", "w", encoding="utf-8") as f:
                for row in self.threat_data:
                    f.write(" ".join(row) + "\n")

            return True
        except Exception as e:
            raise Exception(f"Ошибка сохранения данных: {str(e)}")

    def sort_data(self, column_index, ascending=True):
        if not self.threat_data or column_index >= len(self.column_names):
            return False

        try:
            self.threat_data = sorted(
                self.threat_data,
                key=lambda x: float(x[column_index])
                if column_index < len(x) and x[column_index].replace('.', '', 1).isdigit()
                else x[column_index] if column_index < len(x) else "",
                reverse=not ascending
            )
            return True
        except Exception as e:
            raise Exception(f"Ошибка сортировки: {str(e)}")


class DataController:
    """Контроллер для управления данными и интерфейсом"""

    def __init__(self, ui):
        self.ui = ui
        self.data_manager = DataManager()
        self.column_widgets = []

        self.ui.load_data_btn.clicked.connect(self.load_and_display_data)
        self.ui.sort_by_column_btn.clicked.connect(self.show_sort_dialog)
        self.ui.save_btn.clicked.connect(self.save_data)

    def load_and_display_data(self):
        try:
            if not self.data_manager.load_data():
                QMessageBox.warning(self.ui, "Ошибка", "Не удалось загрузить данные")
                return

            self.update_display()
            QMessageBox.information(self.ui, "Успех",
                                    f"Загружено {len(self.data_manager.threat_data)} строк\n"
                                    f"Столбцов: {len(self.data_manager.column_names)}")
        except Exception as e:
            QMessageBox.critical(self.ui, "Ошибка", str(e))

    def update_display(self):
        for widget in self.column_widgets:
            widget.setParent(None)
        self.column_widgets.clear()

        for i, name in enumerate(self.data_manager.column_names):
            column_data = []
            for row in self.data_manager.threat_data:
                if i < len(row):
                    column_data.append(row[i])
                else:
                    column_data.append("")

            column_widget = ColumnWidget(name, column_data)
            self.column_widgets.append(column_widget)
            self.ui.columns_layout.addWidget(column_widget)

    def show_sort_dialog(self):
        if not self.data_manager.column_names:
            QMessageBox.warning(self.ui, "Ошибка", "Сначала загрузите данные")
            return

        column, ok = QInputDialog.getItem(
            self.ui,
            "Выбор столбца",
            "Выберите столбец для сортировки:",
            self.data_manager.column_names,
            0, False
        )

        if not ok or not column:
            return

        sort_order, ok = QInputDialog.getItem(
            self.ui,
            "Направление сортировки",
            "Выберите направление сортировки:",
            ["По возрастанию", "По убыванию"],
            0, False
        )

        if not ok:
            return

        try:
            column_index = self.data_manager.column_names.index(column)
            ascending = sort_order == "По возрастанию"

            if self.data_manager.sort_data(column_index, ascending):
                self.update_display()
                QMessageBox.information(self.ui, "Успех",
                                        f"Данные отсортированы по столбцу '{column}'")
            else:
                QMessageBox.warning(self.ui, "Ошибка", "Не удалось отсортировать данные")
        except Exception as e:
            QMessageBox.critical(self.ui, "Ошибка", str(e))

    def save_data(self):
        try:
            if not self.data_manager.save_data():
                QMessageBox.warning(self.ui, "Ошибка", "Не удалось сохранить данные")
                return

            QMessageBox.information(self.ui, "Успех", "Данные успешно сохранены")
        except Exception as e:
            QMessageBox.critical(self.ui, "Ошибка", str(e))


class TagWidget(QWidget):
    """Виджет для отображения одного тега с поддержкой drag-and-drop"""

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.setFixedSize(120, 40)
        self.name = name
        self.color = self.generate_random_hex_color()

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {self.color};
                color: white;
                border-radius: 6px;
                padding: 5px;
                font-weight: 500;
                font-size: 12px;
                qproperty-alignment: 'AlignCenter';
            }}
        """)

        self.label = QLabel(name, self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setAcceptDrops(True)

    def generate_random_hex_color(self):
        r = random.randint(100, 200)
        g = random.randint(100, 200)
        b = random.randint(100, 200)
        return f"#{r:02X}{g:02X}{b:02X}"

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(f"{self.name}|{self.color}")
            drag.setMimeData(mime_data)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())

            drag.exec_(Qt.MoveAction)


class DropTagsWidget(QWidget):
    """Виджет для приема перетаскиваемых тегов"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(60)
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border-radius: 8px;
                padding: 10px;
                margin-top: 10px;
                box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
                border: 2px dashed #D8DEE9;
            }
            QWidget:hover {
                border-color: #5E81AC;
            }
        """)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 5, 10, 5)
        self.layout.setSpacing(10)

        self.label = QLabel("Перетащите теги сюда")
        self.label.setStyleSheet("""
            QLabel {
                color: #4C566A;
                font-size: 14px;
                font-style: italic;
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.label)
        self.layout.addStretch()

        self.setAcceptDrops(True)
        self.tags = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        mime_data = event.mimeData()
        if mime_data.hasText():
            text = mime_data.text()
            if "|" in text:
                name, color = text.split("|")

                tag = QLabel(name)
                tag.setStyleSheet(f"""
                    QLabel {{
                        background-color: {color};
                        color: white;
                        border-radius: 6px;
                        padding: 5px;
                        font-weight: 500;
                        font-size: 12px;
                        margin: 2px;
                    }}
                """)
                tag.setAlignment(Qt.AlignCenter)
                tag.setFixedSize(120, 40)

                self.layout.insertWidget(self.layout.count() - 1, tag)
                self.tags.append(name)

                source_widget = event.source()
                if source_widget and source_widget.parent():
                    source_widget.setParent(None)
                    source_widget.deleteLater()

                if len(self.tags) == 1:
                    self.label.setVisible(False)


class TagController:
    def __init__(self, ui):
        self.default_tags = ['EyeSec:Network', 'EyeSec:System', 'EyeSec:Virus']
        self.ui = ui
        self.load_saved_tags()

        # Создаем и добавляем виджет для перетаскивания тегов
        self.drop_tags_widget = DropTagsWidget()
        self.ui.info_vertical_layout.addWidget(self.drop_tags_widget)

        self.ui.add_tag_btn.clicked.connect(self.add_new_tag)
        self.ui.delete_tag_btn.clicked.connect(self.delete_tag)

        self.load_data_tags()

    def load_saved_tags(self):
        try:
            if os.path.exists("add_new_tag.txt"):
                with open("add_new_tag.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        tag = line.strip()
                        if tag and tag not in self.default_tags:
                            self.default_tags.append(tag)
        except Exception as e:
            print(f"Ошибка загрузки тегов: {e}")

    def load_data_tags(self):
        for i in reversed(range(self.ui.tags_layout.count())):
            item = self.ui.tags_layout.itemAt(i)
            if item.widget() is not None:
                item.widget().deleteLater()

        for tag_name in self.default_tags:
            tag = TagWidget(str(tag_name))
            self.ui.tags_layout.insertWidget(self.ui.tags_layout.count() - 1, tag)

    def add_new_tag(self):
        name_tag, ok = QInputDialog.getText(
            self.ui,
            "Добавление нового тега",
            "Введите название нового тега:"
        )

        if not ok or not name_tag:
            return

        full_tag_name = f'EyeSec:{name_tag}' if not name_tag.startswith('EyeSec:') else name_tag

        if full_tag_name in self.default_tags:
            QMessageBox.warning(self.ui, "Ошибка", "Такой тег уже есть в списке")
            return

        self.default_tags.append(full_tag_name)
        self.load_data_tags()

        try:
            with open("add_new_tag.txt", "w", encoding="utf-8") as f:
                for tag in self.default_tags:
                    if tag not in ['EyeSec:Network', 'EyeSec:System', 'EyeSec:Virus']:
                        f.write(f"{tag}\n")
        except Exception as e:
            QMessageBox.warning(self.ui, "Ошибка", f"Не удалось сохранить теги: {str(e)}")

    def delete_tag(self):
        name_tag, ok = QInputDialog.getText(
            self.ui,
            "Удаление тэга",
            "Введите название тэга:"
        )

        if not ok or not name_tag:
            return

        full_tag_name = f'EyeSec:{name_tag}' if not name_tag.startswith('EyeSec:') else name_tag

        if full_tag_name in self.default_tags:
            self.default_tags.remove(full_tag_name)
            self.load_data_tags()
        else:
            QMessageBox.warning(self.ui, "Ошибка", f"Не удалось найти тэг: {full_tag_name}")


class MainLogicUI(QMainWindow):
    def __init__(self):
        super().__init__()
        screen_size = QApplication.primaryScreen().availableGeometry()
        self.setFixedSize(screen_size.width(), screen_size.height())

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.authwindow = AunthWindow()
        self.robberywindow = robberyWindow()
        self.mispsendwindow = mispSendWindow()

        self.main_window = MainWindow(self.switch_page)
        self.insert_window = InsertWindow(self.switch_page)
        self.flex_window = FlexWindow(self.switch_page)
        self.final_window = finalWindow(self.switch_page)

        self.db_handler = DatabaseHandler(self.create_config(), self.insert_window)
        self.db_handler.setup_connections()
        self.data_controller = DataController(self.flex_window)
        self.tags_controller = TagController(self.flex_window)
        self.tags_controller.load_data_tags()
        self.dropmemory = DropTagsWidget()

        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.addWidget(self.insert_window)
        self.stacked_widget.addWidget(self.flex_window)
        self.stacked_widget.addWidget(self.final_window)

        self.connect_buttons()
        self.switch_page("Main")

    def switch_page(self, page_name):
        if page_name == "Main":
            self.stacked_widget.setCurrentWidget(self.main_window)
            self.setWindowTitle("EyeSec - Главная страница")
        elif page_name == "Insert":
            self.stacked_widget.setCurrentWidget(self.insert_window)
            self.setWindowTitle("EyeSec - Загрузка данных")
        elif page_name == "Flex":
            self.stacked_widget.setCurrentWidget(self.flex_window)
            self.setWindowTitle("EyeSec - Сортировка данных")
        elif page_name == "Final":
            self.stacked_widget.setCurrentWidget(self.final_window)
            self.setWindowTitle("EyeSec - Выгрузка данных")
        else:
            print(f"Страница {page_name} не найдена")

    def connect_buttons(self):
        self.main_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.main_window.pushButton_6.clicked.connect(lambda: self.switch_page("Insert"))
        self.main_window.pushButton_4.clicked.connect(lambda: self.switch_page("Final"))
        self.main_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.main_window.pushButton_5.clicked.connect(lambda: self.switch_page("Flex"))

        self.insert_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.insert_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.insert_window.pushButton_5.clicked.connect(lambda: self.switch_page("Flex"))
        self.insert_window.pushButton_4.clicked.connect(lambda: self.switch_page("Final"))

        self.flex_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.flex_window.pushButton_6.clicked.connect(lambda: self.switch_page("Insert"))
        self.flex_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.flex_window.pushButton_4.clicked.connect(lambda: self.switch_page("Final"))
        self.flex_window.table_constructor_btn.clicked.connect(lambda: self.robberywindow.show())
        self.flex_window.add_tag_btn.clicked.connect(lambda: self.tags_controller.add_new_tag())
        self.flex_window.delete_tag_btn.clicked.connect(lambda: self.tags_controller.delete_tag())

        self.final_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.final_window.pushButton_6.clicked.connect(lambda: self.switch_page("Insert"))
        self.final_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.final_window.pushButton_5.clicked.connect(lambda: self.switch_page("Flex"))
        self.final_window.pushButton_9.clicked.connect(lambda: self.mispsendwindow.show())
        self.final_window.pushButton_8.clicked.connect(lambda: self.import_to_exel())

        self.mispsendwindow.send_button.clicked.connect(lambda: self.misp_convertion(self.send_aunth_to_misp()))

    def create_config(self):
        return {
            "Host": self.authwindow.textEdit_ip.text(),
            "Port": 3306,
            "User": self.authwindow.textEdit_login.text(),
            "password": self.authwindow.textEdit_passwd.text(),
            "database": self.authwindow.textEdit_table.text(),
        }

    def send_aunth_to_misp(self):
        return dict(
            misp_key=self.authwindow.textEdit.text(),
            misp_url="https://192.168.0.102",
            misp_verify_cert=False,
        )

    def get_column_data(self, column_name):
        list_widget = self.mispsendwindow.left_columns[column_name]
        return [list_widget.item(i).text() for i in range(list_widget.count())]

    def misp_convertion(self, config):
        values = self.get_column_data("Value")
        comments = self.get_column_data("Comment")
        category = self.get_column_data("Category")
        types = self.get_column_data("Type")

        if not values:
            print("Нет данных для отправки")
            return None

        event = MISPEvent()
        event.info = "Данные из EyeSec"
        event.distribution = "0"
        event.add_tag('imported-from:eyesec')
        for tag_name in self.tags_controller.drop_tags_widget.tags:
            event.add_tag(tag_name)

        try:
            misp = ExpandedPyMISP(
                config.get("misp_url"),
                config.get("misp_key"),
                config.get("misp_verify_cert")
            )
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            return None

        for i in range(len(values)):
            try:
                event.add_attribute(
                    type=str(types[i]),
                    value=str(values[i]),
                    comment=str(comments[i]) if i < len(comments) else "",
                    disable_correlation=True,
                    to_ids=True
                )
                print(f"Добавлено: {values[i]}")
            except Exception as e:
                print(f"Ошибка добавления {values[i]}: {e}")
                continue

        try:
            result = misp.add_event(event)
            print("Событие создано!")
            return result
        except Exception as e:
            print(f"Ошибка отправки: {e}")
            return None
    def import_to_exel(self):
        columns_names = []
        with open('columns_names.txt', 'r', encoding='utf-8') as file:
            for i in file:
                columns_names.append(i.strip())
        dataframe = pd.read_csv('threat.txt', header=None, sep=' ')
        dataframe.columns = columns_names
        dataframe.to_excel('EyeSec exel file.xlsx')


if __name__ == "__main__":
    with open("threat.txt", "w") as file:
        file.write(" ")
    with open("columns_names.txt", "w") as file:
        file.write(" ")

    app = QApplication(sys.argv)
    window = MainLogicUI()
    window.show()
    sys.exit(app.exec())