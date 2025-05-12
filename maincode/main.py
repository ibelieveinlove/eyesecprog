import sys,urllib,pymysql
from pymysql import cursors
from config import core
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget,QWidget, QStackedWidget, QLabel, QFileDialog
import untitled, insert, Aunth, Flex,final,robberySystem
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QListWidgetItem,QTableWidgetItem,QListWidget
from database import DatabaseHandler
import MISPSend
from pymisp import MISPEvent, MISPObject, PyMISP, ExpandedPyMISP
import os



class mispSendWindow(MISPSend.MainWindow):
    def __init__(self,switch_page_callback=None):
        super().__init__()
        self.switch_page = switch_page_callback
class robberyWindow(robberySystem.MainWindow):
    def __init__(self,switch_page_callback=None):
        super().__init__()
        self.switch_page = switch_page_callback


class finalWindow(QMainWindow,final.Ui_MainWindow):
    def __init__(self,switch_page_callback=None):
        super().__init__()
        self.setupUi(self)
        self.switch_page = switch_page_callback


class FlexWindow(QMainWindow, Flex.Ui_MainWindow):
    def __init__(self,switch_page_callback=None):
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


from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QListWidget,
                               QMessageBox, QInputDialog)
from PySide6.QtCore import Qt


class ColumnWidget(QWidget):
    """Виджет для отображения одного столбца данных"""

    def __init__(self, title, data, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)

        # Заголовок столбца
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

        # Список данных
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
        """Обновляет данные в списке"""
        self.data_list.clear()
        for item in data:
            if item:  # Пропускаем пустые значения
                self.data_list.addItem(item)


from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QListWidget,
                               QMessageBox, QInputDialog)
from PySide6.QtCore import Qt


class ColumnWidget(QWidget):
    """Виджет для отображения одного столбца данных"""

    def __init__(self, title, data, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)

        # Заголовок столбца
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

        # Список данных
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
        """Обновляет данные в списке"""
        self.data_list.clear()
        for item in data:
            if item:  # Пропускаем пустые значения
                self.data_list.addItem(item)


class DataManager:
    """Класс для работы с данными с учетом формата файлов"""

    def __init__(self):
        self.column_names = []
        self.threat_data = []

    def load_data(self):
        """Загрузка данных из файлов с учетом их формата"""
        try:
            # Загрузка названий столбцов (каждая строка - отдельный столбец)
            with open("columns_names.txt", "r", encoding="utf-8") as f:
                self.column_names = [line.strip() for line in f if line.strip()]

            # Загрузка данных (столбцы разделены пробелами)
            with open("threat.txt", "r", encoding="utf-8") as f:
                self.threat_data = []
                for line in f:
                    line = line.strip()
                    if line:
                        # Разбиваем строку по пробелам, сохраняем все значения
                        row = line.split(' ')
                        self.threat_data.append(row)

            # Проверка данных
            if not self.column_names:
                raise Exception("Файл columns_names.txt пустой")
            if not self.threat_data:
                raise Exception("Файл threat.txt пустой")

            # Проверяем соответствие количества столбцов
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
        """Сохранение данных в файлы в исходном формате"""
        try:
            # Сохранение названий столбцов (каждый на новой строке)
            with open("columns_names.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(self.column_names))

            # Сохранение данных (столбцы разделены пробелами)
            with open("threat.txt", "w", encoding="utf-8") as f:
                for row in self.threat_data:
                    # Записываем значения через пробел
                    f.write(" ".join(row) + "\n")

            return True
        except Exception as e:
            raise Exception(f"Ошибка сохранения данных: {str(e)}")

    # Остальные методы остаются без изменений
    def sort_data(self, column_index, ascending=True):
        """Сортировка данных по указанному столбцу"""
        if not self.threat_data or column_index >= len(self.column_names):
            return False

        try:
            # Сортировка с учетом числовых значений
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

        # Подключение кнопок
        self.ui.load_data_btn.clicked.connect(self.load_and_display_data)
        self.ui.sort_by_column_btn.clicked.connect(self.show_sort_dialog)
        self.ui.save_btn.clicked.connect(self.save_data)

    def load_and_display_data(self):
        """Загрузка и отображение данных"""
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
        """Обновление отображения данных"""
        # Очищаем предыдущие виджеты
        for widget in self.column_widgets:
            widget.setParent(None)
        self.column_widgets.clear()

        # Создаем виджеты для каждого столбца
        for i, name in enumerate(self.data_manager.column_names):
            # Получаем данные для текущего столбца
            column_data = []
            for row in self.data_manager.threat_data:
                if i < len(row):
                    column_data.append(row[i])
                else:
                    column_data.append("")  # Пустое значение, если столбца нет в строке

            column_widget = ColumnWidget(name, column_data)
            self.column_widgets.append(column_widget)
            self.ui.columns_layout.addWidget(column_widget)

    def show_sort_dialog(self):
        """Показывает диалог сортировки с выбором столбца и направления"""
        if not self.data_manager.column_names:
            QMessageBox.warning(self.ui, "Ошибка", "Сначала загрузите данные")
            return

        # Выбор столбца
        column, ok = QInputDialog.getItem(
            self.ui,
            "Выбор столбца",
            "Выберите столбец для сортировки:",
            self.data_manager.column_names,
            0, False
        )

        if not ok or not column:
            return

        # Выбор направления сортировки
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
        """Сохранение данных в файлы в исходном формате"""
        try:
            if not self.data_manager.save_data():
                QMessageBox.warning(self.ui, "Ошибка", "Не удалось сохранить данные")
                return

            QMessageBox.information(self.ui, "Успех", "Данные успешно сохранены")
        except Exception as e:
            QMessageBox.critical(self.ui, "Ошибка", str(e))
class MainLogicUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Настройки окна
        screen_size = QApplication.primaryScreen().availableGeometry()
        self.setFixedSize(screen_size.width(), screen_size.height())

        # Инициализация stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.authwindow = AunthWindow()
        self.robberywindow = robberyWindow()
        self.mispsendwindow = mispSendWindow()
        # Создаем страницы с передачей callback функции
        self.main_window = MainWindow(self.switch_page)
        self.insert_window = InsertWindow(self.switch_page)
        self.flex_window = FlexWindow(self.switch_page)
        self.final_window = finalWindow(self.switch_page)
        self.db_handler = DatabaseHandler(self.create_config(), self.insert_window)
        self.db_handler.setup_connections()
        self.data_controller = DataController(self.flex_window)

        # Добавляем страницы в stacked widget
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.addWidget(self.insert_window)
        self.stacked_widget.addWidget(self.flex_window)
        self.stacked_widget.addWidget(self.final_window)

        # Подключаем кнопки
        self.connect_buttons()

        # Показываем главную страницу
        self.switch_page("Main")
    def switch_page(self, page_name):
        """Функция для переключения страниц"""
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
        """Подключение кнопок к функциям выплнения команд"""
        self.main_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.main_window.pushButton_6.clicked.connect(lambda: self.switch_page("Insert"))
        self.main_window.pushButton_4.clicked.connect(lambda: self.switch_page("Final"))
        self.main_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.main_window.pushButton_5.clicked.connect(lambda: self.switch_page("Flex"))
        # ---------------------------------------------------------------------------------
        self.insert_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.insert_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.insert_window.pushButton_5.clicked.connect(lambda: self.switch_page("Flex"))
        self.insert_window.pushButton_4.clicked.connect(lambda: self.switch_page("Final"))
        # ---------------------------------------------------------------------------------
        self.flex_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.flex_window.pushButton_6.clicked.connect(lambda: self.switch_page("Insert"))
        self.flex_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.flex_window.pushButton_4.clicked.connect(lambda: self.switch_page("Final"))
        self.flex_window.table_constructor_btn.clicked.connect(lambda:self.robberywindow.show())
        #---------------------------------------------------------------------------------
        self.final_window.pushButton_3.clicked.connect(lambda: self.switch_page("Main"))
        self.final_window.pushButton_6.clicked.connect(lambda: self.switch_page("Insert"))
        self.final_window.pushButton.clicked.connect(lambda: self.authwindow.show())
        self.final_window.pushButton_5.clicked.connect(lambda: self.switch_page("Flex"))
        self.final_window.pushButton_9.clicked.connect(lambda: self.mispsendwindow.show())
        #--------------------------------------------------------------------------------
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
            misp_key = self.authwindow.textEdit.text(),
            misp_url = "https://192.168.0.102",
            misp_verify_cert = False,
        )

    def get_column_data(self, column_name):
        """Возвращает список значений из указанного столбца"""
        list_widget = self.mispsendwindow.left_columns[column_name]  # Получаем QListWidget столбца
        return [list_widget.item(i).text() for i in range(list_widget.count())]

    def misp_convertion(self, config):
        # Получаем данные из колонок
        values = self.get_column_data("Value")  # Только значения, остальное не важно
        comments = self.get_column_data("Comment")
        category = self.get_column_data("Category")
        types = self.get_column_data("Type")

        # Проверяем, есть ли что отправлять
        if not values:
            print("Нет данных для отправки")
            return None

        # Создаём событие
        event = MISPEvent()
        event.info = "Данные из EyeSec"
        event.distribution = "0"  # Видимость: только моя организация
        event.add_tag('imported-from:eyesec')

        # Подключаемся к MISP
        try:
            misp = ExpandedPyMISP(
                config.get("misp_url"),
                config.get("misp_key"),
                config.get("misp_verify_cert")
            )
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            return None

        # Добавляем все значения как тип 'other'
        for i in range(len(values)):
            try:
                event.add_attribute(
                    category = str(category[i]),
                    type=str(types[i]),
                    value=str(values[i]),  # Значение как строка
                    comment=str(comments[i]) if i < len(comments) else "",  # Комментарий если есть
                    disable_correlation=True,  # Не создавать корреляции
                    to_ids=False  # Не использовать для автоматического обнаружения
                )
                print(f"Добавлено: {values[i]}")
            except Exception as e:
                print(f"Ошибка добавления {values[i]}: {e}")
                continue

        # Пытаемся отправить
        try:
            result = misp.add_event(event)
            print("Событие создано!")
            return result
        except Exception as e:
            print(f"Ошибка отправки: {e}")
            return None


if __name__ == "__main__":
    with open("threat.txt", "w")  as file:
        file.write(" ")
    with open("columns_names.txt","w") as file:
        file.write(" ")
    file.close()
    app = QApplication(sys.argv)

    # Настройки масштабирования

    window = MainLogicUI()
    window.show()
    sys.exit(app.exec())