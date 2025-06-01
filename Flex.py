# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QPushButton, QScrollBar, QSizePolicy, QVBoxLayout,
                               QWidget, QHBoxLayout, QListWidget, QListWidgetItem,
                               QMessageBox, QInputDialog, QScrollArea)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1457, 895)
        MainWindow.setMinimumSize(QSize(1000, 700))
        MainWindow.setStyleSheet(u"""
            QMainWindow {
                background-color: #f5f7fa;
            }
        """)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: transparent;")

        # Главный горизонтальный макет
        self.main_horizontal_layout = QHBoxLayout(self.centralwidget)
        self.main_horizontal_layout.setSpacing(0)
        self.main_horizontal_layout.setContentsMargins(0, 0, 0, 0)

        # Боковая панель (меню) - ВОССТАНОВЛЕН ИСХОДНЫЙ ВИД
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

        self.side_menu_layout = QVBoxLayout(self.side_menu)
        self.side_menu_layout.setSpacing(20)
        self.side_menu_layout.setContentsMargins(20, 40, 20, 40)

        # Заголовок меню
        self.menu_header = QFrame()
        self.menu_header.setObjectName(u"menu_header")
        self.menu_header.setStyleSheet(u"background-color: transparent;")
        self.menu_header.setFrameShape(QFrame.NoFrame)

        self.menu_header_layout = QHBoxLayout(self.menu_header)
        self.menu_header_layout.setContentsMargins(0, 0, 0, 0)

        self.label_4 = QLabel()
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"""
            QLabel {
                color: #ffffff;
                font-size: 22px;
                font-weight: bold;
                background-color: transparent;
            }
        """)

        self.pushButton = QPushButton()
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 40))
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

        self.menu_header_layout.addWidget(self.label_4)
        self.menu_header_layout.addWidget(self.pushButton)
        self.menu_header_layout.setStretch(0, 1)

        self.side_menu_layout.addWidget(self.menu_header)

        # Кнопки меню
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

        self.pushButton_3 = QPushButton()
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(button_style)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_6 = QPushButton()
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(button_style)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_5 = QPushButton()
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(button_style)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_4 = QPushButton()
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(button_style)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_2 = QPushButton()
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.side_menu_layout.addWidget(self.pushButton_3)
        self.side_menu_layout.addWidget(self.pushButton_6)
        self.side_menu_layout.addWidget(self.pushButton_5)
        self.side_menu_layout.addWidget(self.pushButton_4)
        self.side_menu_layout.addWidget(self.pushButton_2)

        # Spacer
        self.side_menu_layout.addStretch(1)

        self.main_horizontal_layout.addWidget(self.side_menu)

        # Основная область контента (вертикальная компоновка)
        self.content_area = QWidget(self.centralwidget)
        self.content_area.setObjectName(u"content_area")
        self.content_area.setStyleSheet(u"background-color: #f8f9fa;")

        self.content_vertical_layout = QVBoxLayout(self.content_area)
        self.content_vertical_layout.setContentsMargins(20, 20, 20, 20)
        self.content_vertical_layout.setSpacing(20)

        # Заголовок
        self.label = QLabel()
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"""
            QLabel {
                font-size: 36px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
                padding: 10px;
            }
        """)
        self.content_vertical_layout.addWidget(self.label)

        # Основной контент (горизонтальная компоновка)
        self.main_content_widget = QWidget()
        self.main_content_widget.setObjectName(u"main_content_widget")
        self.main_content_widget.setStyleSheet(u"background-color: transparent;")

        self.main_content_layout = QHBoxLayout(self.main_content_widget)
        self.main_content_layout.setContentsMargins(0, 0, 0, 0)
        self.main_content_layout.setSpacing(20)

        # Блок информации (вертикальный) - ЛЕВАЯ ЧАСТЬ
        self.info_widget = QWidget()
        self.info_widget.setObjectName(u"widget")
        self.info_widget.setStyleSheet(u"""
            QWidget {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            }
        """)

        self.info_vertical_layout = QVBoxLayout(self.info_widget)
        self.info_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.info_vertical_layout.setSpacing(15)

        # Область с прокруткой для столбцов
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; }")

        # Контейнер для столбцов
        self.columns_area = QWidget()
        self.columns_layout = QHBoxLayout(self.columns_area)
        self.columns_layout.setContentsMargins(5, 5, 5, 5)
        self.columns_layout.setSpacing(10)

        self.scroll_area.setWidget(self.columns_area)
        self.info_vertical_layout.addWidget(self.scroll_area)

        # Кнопка загрузки данных
        self.load_data_btn = QPushButton()
        self.load_data_btn.setObjectName(u"load_data_btn")
        self.load_data_btn.setStyleSheet(u"""
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
        """)
        self.load_data_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.info_vertical_layout.addWidget(self.load_data_btn)

        # Кнопка сохранения данных
        self.save_btn = QPushButton()
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setStyleSheet(u"""
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
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.info_vertical_layout.addWidget(self.save_btn)



        # Блок тегов (правая часть) - оригинальные названия
        self.info_widget_threat = QWidget()
        self.info_widget_threat.setObjectName(u"info_widget_threat")
        self.info_widget_threat.setStyleSheet(u"""
            QWidget {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 0px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            }
        """)
        self.info_widget_threat.setFixedHeight(400)

        self.info_vertical_layout_threat = QVBoxLayout(self.info_widget_threat)
        self.info_vertical_layout_threat.setContentsMargins(0, 0, 0, 0)
        self.info_vertical_layout_threat.setSpacing(0)

        # Компактный виджет заголовка (50px высотой)
        self.tags_header = QWidget()
        self.tags_header.setObjectName(u"tags_header")
        self.tags_header.setFixedHeight(50)
        self.tags_header.setStyleSheet(u"""
            QWidget {
                background-color: #f8f9fa;
                border-top-left-radius: 12px;
                border-top-right-radius: 12px;
                padding: 10px 15px;
            }
        """)

        self.tags_header_layout = QHBoxLayout(self.tags_header)
        self.tags_header_layout.setContentsMargins(0, 0, 0, 0)

        # Заголовок "Теги"
        self.label_5 = QLabel()
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
            }
        """)

        # Кнопка "Добавить тег" (компактная)
        self.add_tag_btn = QPushButton()
        self.add_tag_btn.setObjectName(u"add_tag_btn")
        self.add_tag_btn.setFixedSize(100, 30)
        self.add_tag_btn.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 4px 8px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.add_tag_btn.setCursor(QCursor(Qt.PointingHandCursor))

        # Кнопка "удалить тег" (компактная)
        self.delete_tag_btn = QPushButton()
        self.delete_tag_btn.setObjectName(u"delete_tag_btn")
        self.delete_tag_btn.setFixedSize(100, 30)
        self.delete_tag_btn.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 4px 8px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.delete_tag_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.tags_header_layout.addWidget(self.label_5)
        self.tags_header_layout.addStretch(1)
        self.tags_header_layout.addWidget(self.add_tag_btn)
        self.tags_header_layout.addWidget(self.delete_tag_btn)

        self.info_vertical_layout_threat.addWidget(self.tags_header)

        # Основная область тегов с фиксированным скроллбаром
        self.tags_scroll_area = QScrollArea()
        self.tags_scroll_area.setObjectName(u"tags_scroll_area")
        self.tags_scroll_area.setWidgetResizable(True)
        self.tags_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tags_scroll_area.setStyleSheet(u"""
            QScrollArea {
                border: none;
                border-bottom-left-radius: 12px;
                border-bottom-right-radius: 12px;
            }
            QScrollBar:vertical {
                width: 10px;
                background: #f1f1f1;
            }
            QScrollBar::handle:vertical {
                background: #c1c1c1;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        self.tags_container = QWidget()
        self.tags_container.setObjectName(u"tags_container")
        self.tags_container.setStyleSheet(u"background-color: transparent;")
        self.tags_layout = QVBoxLayout(self.tags_container)
        self.tags_layout.setContentsMargins(15, 10, 15, 15)
        self.tags_layout.setSpacing(8)
        self.tags_layout.addStretch()

        self.tags_scroll_area.setWidget(self.tags_container)
        self.info_vertical_layout_threat.addWidget(self.tags_scroll_area)

        # Блок управления (вертикальный) - ПРАВАЯ ЧАСТЬ
        self.control_widget = QWidget()
        self.control_widget.setObjectName(u"frame_2")
        self.control_widget.setStyleSheet(u"""
            QWidget {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            }
        """)

        self.control_vertical_layout = QVBoxLayout(self.control_widget)
        self.control_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.control_vertical_layout.setSpacing(12)

        self.label_3 = QLabel()
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
                margin-bottom: 10px;
            }
        """)
        self.control_vertical_layout.addWidget(self.label_3)

        # Кнопки сортировки
        sort_button_style = u"""
            QPushButton {
                background-color: #ECEFF4;
                color: #4C566A;
                border: 1px solid #D8DEE9;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                min-width: 160px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #E5E9F0;
                border-color: #C0C8D2;
            }
            QPushButton:pressed {
                background-color: #D8DEE9;
            }
            QPushButton:checked {
                background-color: #5E81AC;
                color: white;
                border-color: #5E81AC;
            }
        """

        self.sort_by_column_btn = QPushButton()
        self.sort_by_column_btn.setObjectName(u"sort_by_column_btn")
        self.sort_by_column_btn.setStyleSheet(sort_button_style)
        self.sort_by_column_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.control_vertical_layout.addWidget(self.sort_by_column_btn)

        # Разделитель
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setStyleSheet("color: #D8DEE9;")
        self.control_vertical_layout.addWidget(self.separator)

        # Основные кнопки управления
        action_button_style = u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
                min-width: 160px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """

        self.apply_filters_btn = QPushButton()
        self.apply_filters_btn.setObjectName(u"apply_filters_btn")
        self.apply_filters_btn.setStyleSheet(action_button_style)
        self.apply_filters_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.control_vertical_layout.addWidget(self.apply_filters_btn)

        self.reset_filters_btn = QPushButton()
        self.reset_filters_btn.setObjectName(u"reset_filters_btn")
        self.reset_filters_btn.setStyleSheet(action_button_style)
        self.reset_filters_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.control_vertical_layout.addWidget(self.reset_filters_btn)

        self.table_constructor_btn = QPushButton()
        self.table_constructor_btn.setObjectName(u"table_constructor_btn")
        self.table_constructor_btn.setStyleSheet(action_button_style)
        self.table_constructor_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.control_vertical_layout.addWidget(self.table_constructor_btn)

        self.control_vertical_layout.addStretch(1)

        # Вертикальный макет для правой части
        self.right_side_layout = QVBoxLayout()
        self.right_side_layout.setContentsMargins(0, 0, 0, 0)
        self.right_side_layout.setSpacing(20)

        # Добавляем блок тегов
        self.right_side_layout.addWidget(self.info_widget_threat)

        # Добавляем блок управления
        self.right_side_layout.addWidget(self.control_widget)

        # Контейнер для правой части
        self.right_side_container = QWidget()
        self.right_side_container.setLayout(self.right_side_layout)

        # Добавляем основные виджеты в главный layout
        self.main_content_layout.addWidget(self.info_widget, 2)
        self.main_content_layout.addWidget(self.right_side_container, 1)

        self.content_vertical_layout.addWidget(self.main_content_widget, 1)

        self.main_horizontal_layout.addWidget(self.content_area, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Threat Data Manager", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Меню", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Авторизация", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Главная страница", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Загрузка данных", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Фильтрация", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Выгрузка", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Настройки", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Управление данными", None))
        self.load_data_btn.setText(QCoreApplication.translate("MainWindow", u"Загрузить данные", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Управление", None))
        self.sort_by_column_btn.setText(QCoreApplication.translate("MainWindow", u"Сортировать по столбцу", None))
        self.table_constructor_btn.setText(QCoreApplication.translate("MainWindow", u"Конструктор таблиц", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Сохранить", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Теги", None))
        self.add_tag_btn.setText(QCoreApplication.translate("MainWindow", u"Добавить тег", None))
        self.delete_tag_btn.setText(QCoreApplication.translate("MainWindow", u"Удалить тэг", None))
