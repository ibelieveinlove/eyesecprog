# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
                               QWidget, QHBoxLayout)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1204, 901)
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

        # Боковая панель (меню) - точное соответствие файлу 2
        self.side_menu = QWidget(self.centralwidget)
        self.side_menu.setObjectName(u"frame")  # Сохраняем оригинальное имя
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

        # Заголовок меню (как в файле 2)
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

        # Кнопки меню (точное соответствие файлу 2)
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

        # Spacer (как в файле 2)
        self.side_menu_layout.addStretch(1)

        self.main_horizontal_layout.addWidget(self.side_menu)

        # Основная область контента
        self.content_area = QWidget(self.centralwidget)
        self.content_area.setObjectName(u"content_area")
        self.content_area.setStyleSheet(u"background-color: #f8f9fa;")

        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(20)

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
        self.content_layout.addWidget(self.label)

        # Блок статистики (frame_2)
        self.frame_2 = QFrame()
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: transparent;")

        self.widget_layout = QVBoxLayout(self.widget)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setSpacing(15)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
                margin-bottom: 10px;
            }
        """)
        self.widget_layout.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"""
            QTextEdit {
                background-color: #ECEFF4;
                border: 1px solid #D8DEE9;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                min-height: 200px;
            }
        """)
        self.widget_layout.addWidget(self.textEdit)

        self.frame_2_layout = QVBoxLayout(self.frame_2)
        self.frame_2_layout.addWidget(self.widget)
        self.content_layout.addWidget(self.frame_2)

        # Блок визуализаций (frame_3) и гистограмм
        self.viz_hist_layout = QHBoxLayout()
        self.viz_hist_layout.setSpacing(20)

        # Блок способов визуализаций (frame_3)
        self.frame_3 = QFrame()
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.label_3 = QLabel(self.frame_3)
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

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.frame_3_layout = QVBoxLayout(self.frame_3)
        self.frame_3_layout.addWidget(self.label_3)
        self.frame_3_layout.addWidget(self.pushButton_7)
        self.frame_3_layout.addWidget(self.pushButton_8)
        self.frame_3_layout.addWidget(self.pushButton_9)
        self.frame_3_layout.addStretch(1)

        # Блок для гистограмм (новый)
        self.histogram_frame = QFrame()
        self.histogram_frame.setObjectName(u"histogram_frame")
        self.histogram_frame.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        self.histogram_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.histogram_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.histogram_label = QLabel(self.histogram_frame)
        self.histogram_label.setObjectName(u"histogram_label")
        self.histogram_label.setText("Гистограммы")
        self.histogram_label.setStyleSheet(u"""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
                margin-bottom: 10px;
            }
        """)

        # Пустое место для будущих гистограмм
        self.histogram_placeholder = QLabel(self.histogram_frame)
        self.histogram_placeholder.setObjectName(u"histogram_placeholder")
        self.histogram_placeholder.setStyleSheet(u"""
            QLabel {
                background-color: #ECEFF4;
                border: 2px dashed #D8DEE9;
                border-radius: 8px;
                min-height: 300px;
            }
        """)
        self.histogram_placeholder.setText("Место для гистограмм")
        self.histogram_placeholder.setAlignment(Qt.AlignCenter)

        self.histogram_layout = QVBoxLayout(self.histogram_frame)
        self.histogram_layout.addWidget(self.histogram_label)
        self.histogram_layout.addWidget(self.histogram_placeholder)

        self.viz_hist_layout.addWidget(self.frame_3, 1)
        self.viz_hist_layout.addWidget(self.histogram_frame, 2)  # Больше места для гистограмм

        self.content_layout.addLayout(self.viz_hist_layout)
        self.main_horizontal_layout.addWidget(self.content_area, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EyeSec - Выгрузка", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430",
                                                             None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445",
                                                             None))
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f",
                                       None))
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f",
                                                           None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"Выгрузка",
                                       None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430",
                                       None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0421\u043f\u043e\u0441\u043e\u0431 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0439",
                                                        None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 SQL",
                                                             None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Exel", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"MISP", None))
    # retranslateUi