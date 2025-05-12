# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QTextBrowser, QTextEdit, QVBoxLayout, QWidget,
                               QHBoxLayout, QLineEdit, QSpacerItem)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1000, 700))

        # Основные стили
        MainWindow.setStyleSheet(u"""
            QMainWindow {
                background-color: #f5f7fa;
            }
            QFrame {
                border-radius: 8px;
            }
        """)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: transparent;")

        # Главный макет
        self.main_layout = QHBoxLayout(self.centralwidget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Боковая панель (меню) - изменено под стиль из файла 2
        self.side_menu = QWidget(self.centralwidget)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumWidth(250)
        self.side_menu.setMaximumWidth(300)
        self.side_menu.setStyleSheet(u"""
            QWidget {
                background-color: #2b303b;
                border: none;
                border-radius: 0;
            }
        """)

        self.menu_layout = QVBoxLayout(self.side_menu)
        self.menu_layout.setSpacing(20)  # Изменено с 0 на 20
        self.menu_layout.setContentsMargins(20, 40, 20, 40)  # Изменено отступы

        # Заголовок меню - изменено под стиль из файла 2
        self.menu_header = QFrame(self.side_menu)
        self.menu_header.setObjectName(u"menu_header")
        self.menu_header.setStyleSheet(u"background-color: transparent;")
        self.menu_header.setFrameShape(QFrame.NoFrame)

        self.header_layout = QHBoxLayout(self.menu_header)
        self.header_layout.setContentsMargins(0, 0, 0, 0)

        self.label_4 = QLabel(self.menu_header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"""
            QLabel {
                color: #ffffff;
                font-size: 22px;
                font-weight: bold;
                background-color: transparent;
            }
        """)

        self.pushButton = QPushButton(self.menu_header)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 40))  # Добавлено минимальный размер
        self.pushButton.setStyleSheet(u"""
            QPushButton {
                background-color: #3a3f4b;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #434956;
            }
            QPushButton:pressed {
                background-color: #3a3f4b;
            }
        """)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.header_layout.addWidget(self.label_4)
        self.header_layout.addWidget(self.pushButton)
        self.header_layout.setStretch(0, 1)  # Добавлено растяжение

        self.menu_layout.addWidget(self.menu_header)

        # Кнопки меню - изменено под стиль из файла 2
        button_style = u"""
            QPushButton {
                text-align: left;
                padding: 12px 15px;
                color: #d8dee9;
                background-color: transparent;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: normal;
            }
            QPushButton:hover {
                background-color: #3a3f4b;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #434956;
            }
        """

        self.pushButton_3 = QPushButton(self.side_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(button_style)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_6 = QPushButton(self.side_menu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(button_style)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_5 = QPushButton(self.side_menu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(button_style)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_4 = QPushButton(self.side_menu)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(button_style)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_2 = QPushButton(self.side_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.menu_layout.addWidget(self.pushButton_3)
        self.menu_layout.addWidget(self.pushButton_6)
        self.menu_layout.addWidget(self.pushButton_5)
        self.menu_layout.addWidget(self.pushButton_4)
        self.menu_layout.addWidget(self.pushButton_2)

        # Растягивающийся спейсер
        self.menu_layout.addStretch(1)  # Изменено на addStretch вместо QSpacerItem

        self.main_layout.addWidget(self.side_menu)

        # Остальной код остается без изменений
        # Основная область контента
        self.content_area = QWidget(self.centralwidget)
        self.content_area.setObjectName(u"content_area")
        self.content_area.setStyleSheet(u"background-color: #f8f9fa;")

        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(30, 30, 30, 30)
        self.content_layout.setSpacing(30)

        # Заголовок страницы
        self.page_header = QFrame(self.content_area)
        self.page_header.setObjectName(u"page_header")
        self.page_header.setStyleSheet(u"background-color: transparent;")
        self.page_header.setFixedHeight(80)

        self.header_layout = QHBoxLayout(self.page_header)
        self.header_layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.page_header)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
            }
        """)

        self.label_5 = QLabel(self.page_header)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u"istockphoto-845329690-612x612.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setFixedSize(50, 50)
        self.label_5.setStyleSheet(u"""
            QLabel {
                background-color: #ECEFF4;
                border-radius: 25px;
                padding: 5px;
            }
        """)

        self.header_layout.addWidget(self.label)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.label_5)
        self.content_layout.addWidget(self.page_header)

        # Основной контент
        self.main_content = QFrame(self.content_area)
        self.main_content.setObjectName(u"main_content")
        self.main_content.setStyleSheet(u"background-color: transparent;")

        self.content_grid = QHBoxLayout(self.main_content)
        self.content_grid.setContentsMargins(0, 0, 0, 0)
        self.content_grid.setSpacing(30)

        # Левая колонка (форма ввода)
        self.left_column = QFrame(self.main_content)
        self.left_column.setObjectName(u"left_column")
        self.left_column.setStyleSheet(u"background-color: transparent;")

        self.left_layout = QVBoxLayout(self.left_column)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setSpacing(20)

        # Форма ввода файлов
        self.file_frame = QFrame(self.left_column)
        self.file_frame.setObjectName(u"file_frame")
        self.file_frame.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                padding: 25px;
            }
        """)

        self.file_layout = QVBoxLayout(self.file_frame)
        self.file_layout.setContentsMargins(0, 0, 0, 0)
        self.file_layout.setSpacing(20)

        self.label_2 = QLabel(self.file_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
            }
        """)

        self.file_input_layout = QHBoxLayout()
        self.file_input_layout.setSpacing(15)

        self.textEdit = QLineEdit(self.file_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"""
            QLineEdit {
                background-color: #ECEFF4;
                border: 1px solid #D8DEE9;
                border-radius: 6px;
                padding: 10px 15px;
                font-size: 14px;
                min-height: 40px;
            }
        """)

        self.pushButton_11 = QPushButton(self.file_frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.file_input_layout.addWidget(self.textEdit)
        self.file_input_layout.addWidget(self.pushButton_11)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(15)

        self.pushButton_7 = QPushButton(self.file_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_8 = QPushButton(self.file_frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"""
            QPushButton {
                background-color: #BF616A;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
            QPushButton:pressed {
                background-color: #A94444;
            }
        """)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.buttons_layout.addWidget(self.pushButton_7)
        self.buttons_layout.addWidget(self.pushButton_8)
        self.buttons_layout.addStretch()

        self.file_layout.addWidget(self.label_2)
        self.file_layout.addLayout(self.file_input_layout)
        self.file_layout.addLayout(self.buttons_layout)

        # Разделитель
        self.line = QFrame(self.left_column)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet(u"color: #D8DEE9; margin: 15px 0;")

        # Форма ручного ввода
        self.manual_frame = QFrame(self.left_column)
        self.manual_frame.setObjectName(u"manual_frame")
        self.manual_frame.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                padding: 25px;
            }
        """)

        self.manual_layout = QVBoxLayout(self.manual_frame)
        self.manual_layout.setContentsMargins(0, 0, 0, 0)
        self.manual_layout.setSpacing(20)

        self.label_3 = QLabel(self.manual_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
            }
        """)

        self.textBrowser = QTextEdit(self.manual_frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"""
            QTextEdit {
                background-color: #ECEFF4;
                border: 1px solid #D8DEE9;
                border-radius: 6px;
                padding: 15px;
                font-size: 14px;
                min-height: 150px;
            }
        """)

        self.manual_buttons_layout = QHBoxLayout()
        self.manual_buttons_layout.setSpacing(15)

        self.pushButton_9 = QPushButton(self.manual_frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_10 = QPushButton(self.manual_frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"""
            QPushButton {
                background-color: #BF616A;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
            QPushButton:pressed {
                background-color: #A94444;
            }
        """)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.manual_buttons_layout.addWidget(self.pushButton_9)
        self.manual_buttons_layout.addWidget(self.pushButton_10)
        self.manual_buttons_layout.addStretch()

        self.manual_layout.addWidget(self.label_3)
        self.manual_layout.addWidget(self.textBrowser)
        self.manual_layout.addLayout(self.manual_buttons_layout)

        self.left_layout.addWidget(self.file_frame)
        self.left_layout.addWidget(self.line)
        self.left_layout.addWidget(self.manual_frame)

        # Правая колонка (ссылки)
        self.right_column = QFrame(self.main_content)
        self.right_column.setObjectName(u"right_column")
        self.right_column.setStyleSheet(u"background-color: transparent;")

        self.right_layout = QVBoxLayout(self.right_column)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        self.right_layout.setSpacing(20)

        # Форма ввода ссылок
        self.links_frame = QFrame(self.right_column)
        self.links_frame.setObjectName(u"links_frame")
        self.links_frame.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                padding: 25px;
            }
        """)

        self.links_layout = QVBoxLayout(self.links_frame)
        self.links_layout.setContentsMargins(0, 0, 0, 0)
        self.links_layout.setSpacing(20)

        self.label_6 = QLabel(self.links_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
            }
        """)

        self.linkBrowser = QTextEdit(self.links_frame)
        self.linkBrowser.setObjectName(u"linkBrowser")
        self.linkBrowser.setStyleSheet(u"""
            QTextEdit {
                background-color: #ECEFF4;
                border: 1px solid #D8DEE9;
                border-radius: 6px;
                padding: 15px;
                font-size: 14px;
                min-height: 200px;
            }
        """)

        self.link_buttons_layout = QHBoxLayout()
        self.link_buttons_layout.setSpacing(15)

        self.pushButton_12 = QPushButton(self.links_frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_13 = QPushButton(self.links_frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"""
            QPushButton {
                background-color: #BF616A;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
            QPushButton:pressed {
                background-color: #A94444;
            }
        """)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.link_buttons_layout.addWidget(self.pushButton_12)
        self.link_buttons_layout.addWidget(self.pushButton_13)
        self.link_buttons_layout.addStretch()

        self.links_layout.addWidget(self.label_6)
        self.links_layout.addWidget(self.linkBrowser)
        self.links_layout.addLayout(self.link_buttons_layout)

        self.right_layout.addWidget(self.links_frame)

        self.content_grid.addWidget(self.left_column, 2)  # 2/3 ширины
        self.content_grid.addWidget(self.right_column, 1)  # 1/3 ширины

        self.content_layout.addWidget(self.main_content)
        self.main_layout.addWidget(self.content_area)

        MainWindow.setCentralWidget(self.centralwidget)

        # Меню и статусбар
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EyeSec - Загрузка данных", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Меню", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Авторизация", None))  # Изменено с "Выйти" на "Авторизация"
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Главная страница", None))  # Изменено
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Загрузка данных", None))  # Изменено
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Фильтрация", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Выгрузка", None))  # Изменено с "Экспорт" на "Выгрузка"
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Настройки", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Загрузка данных", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Обзор...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ввод файлов", None))  # Изменено
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Ввод", None))  # Изменено
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Удалить", None))  # Изменено
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ввод ссылок", None))  # Изменено
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Ввод", None))  # Изменено
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Удалить", None))  # Изменено
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Введение данных вручную", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Ввод", None))  # Изменено
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Удалить", None))  # Изменено
        self.label_5.setText("")