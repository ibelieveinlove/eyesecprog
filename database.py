import pymysql
from urllib.request import urlopen
from PySide6.QtWidgets import QFileDialog, QMessageBox
import logging
import urllib.request
import os
class DatabaseHandler():
    def __init__(self, config, window):
        self.config = config
        self.window = window
        self.file_path = ''
        self.links_url = ''
        self.strings_read = ''

    def get_connection(self):
        """Устанавливает соединение с базой данных"""
        try:
            return pymysql.connect(
                host=self.config.get["Host"],
                port=self.config.get("Port", 3306),
                user=self.config.get["User"],
                password=self.config.get["password"],
                database=self.config.get["database"],
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            self.logger.error(f"Ошибка подключения к БД: {e}")
            self.show_message("Ошибка", f"Не удалось подключиться к базе данных: {e}")
            return None

    def setup_connections(self):
        """Подключаем сигналы кнопок к слотам"""
        # Подключаем кнопки файлового ввода
        self.window.pushButton_11.clicked.connect(self.browse_files)
        self.window.pushButton_7.clicked.connect(lambda: self.read_files())
        self.window.pushButton_8.clicked.connect(lambda: self.window.textEdit.clear())

        # Подключаем кнопки ручного ввода
        self.window.pushButton_9.clicked.connect(lambda: self.read_links())
        self.window.pushButton_10.clicked.connect(lambda: self.window.textBrowser.clear())

        # Подключаем кнопки ввода по ссылке
        self.window.pushButton_12.clicked.connect(lambda: self.read_string())
        self.window.pushButton_13.clicked.connect(lambda: self.window.linkBrowser.clear())

    def browse_files(self):
        """Открывает диалог выбора файла"""
        self.file_path, _ = QFileDialog.getOpenFileName(
            self.window,  # Указываем родительское окно
            "Выберите файл с данными",
            "",
            "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if self.file_path:
            self.window.textEdit.setText(self.file_path)

    def read_links(self):
        try:
            url = self.window.textBrowser.toPlainText()
            if not url:
                self.show_message("Ошибка", "Поле ввода ссылок пустое")
                return

            # Указываем полный путь к файлу для надёжности
            file_path = os.path.join(os.getcwd(), 'threat.txt')

            with urllib.request.urlopen(url) as blist:
                # Открываем файл в режиме добавления ('a') с явным указанием кодировки
                with open(file_path, 'a', encoding='utf-8') as output_file:
                    for line in blist:
                        ip_str = line.decode("utf-8").strip()
                        if not ip_str:
                            continue

                        try:
                            output_file.write(ip_str + '\n')
                            output_file.flush()  # Принудительно записываем изменения
                            print(f"Успешно записано: {ip_str}")  # Для отладки
                        except Exception as e:
                            print(f"Ошибка при записи {ip_str} в файл: {e}")

            print(f"Данные сохранены в файл: {file_path}")  # Показываем где искать файл
        except urllib.error.URLError as e:
            self.show_message("Ошибка", f"Не удалось открыть URL: {e}")
        except PermissionError:
            self.show_message("Ошибка", f"Нет прав на запись в файл: {file_path}")
        except Exception as e:
            self.show_message("Ошибка", f"Непредвиденная ошибка: {e}")

    def read_files(self):
        try:
            with open(self.file_path) as blist:
                with open("threat.txt", 'a', encoding='utf-8') as output_file:
                    for line in blist:
                        ip_str = line.strip()
                        if not ip_str:
                            continue

                        try:
                            output_file.write(ip_str + '\n')
                            output_file.flush()  # Принудительно записываем изменения
                            print(f"Успешно записано: {ip_str}")  # Для отладки
                        except Exception as e:
                            print(f"Ошибка при записи {ip_str} в файл: {e}")

            print(f"Данные сохранены в файл: {output_file}")  # Показываем где искать файл
        except urllib.error.URLError as e:
            self.show_message("Ошибка", f"Не удалось открыть URL: {e}")
        except PermissionError:
            self.show_message("Ошибка", f"Нет прав на запись в файл: {output_file}")
        except Exception as e:
            self.show_message("Ошибка", f"Непредвиденная ошибка: {e}")
    def read_string(self):
        try:
            with open(self.file_path) as blist:
                with open("threat.txt", 'a', encoding='utf-8') as output_file:
                    for line in blist:
                        ip_str = line.strip()
                        if not ip_str:
                            continue

                        try:
                            output_file.write(ip_str + '\n')
                            output_file.flush()  # Принудительно записываем изменения
                            print(f"Успешно записано: {ip_str}")  # Для отладки
                        except Exception as e:
                            print(f"Ошибка при записи {ip_str} в файл: {e}")

            print(f"Данные сохранены в файл: {output_file}")  # Показываем где искать файл
        except urllib.error.URLError as e:
            self.show_message("Ошибка", f"Не удалось открыть URL: {e}")
        except PermissionError:
            self.show_message("Ошибка", f"Нет прав на запись в файл: {output_file}")
        except Exception as e:
            self.show_message("Ошибка", f"Непредвиденная ошибка: {e}")

    def read_string(self):
        try:
            # Получаем весь текст из linkBrowser
            text = self.window.linkBrowser.toPlainText()

            # Разделяем текст на строки (учитываем разные варианты переноса строк)
            lines = text.splitlines() if text else []

            # Указываем путь к файлу
            file_path = "threat.txt"

            with open(file_path, 'a', encoding='utf-8') as output_file:
                for line in lines:
                    line = line.strip()  # Удаляем лишние пробелы и переносы
                    if not line:  # Пропускаем пустые строки
                        continue

                    try:
                        output_file.write(line + '\n')  # Записываем строку с переносом
                        output_file.flush()  # Принудительно записываем изменения
                        print(f"Успешно записано: {line}")  # Для отладки
                    except Exception as e:
                        print(f"Ошибка при записи строки '{line}' в файл: {e}")

            print(f"Данные сохранены в файл: {file_path}")  # Показываем путь к файлу

        except PermissionError:
            self.show_message("Ошибка", "Нет прав на запись в файл!")
        except Exception as e:
            self.show_message("Ошибка", f"Непредвиденная ошибка: {str(e)}")

    def show_message(self, title, message):
        """Показывает всплывающее сообщение"""
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()