## -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget, QHBoxLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QSize(1000, 700))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #f8f9fa;")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: transparent;")

        # Main layout
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Sidebar (widget)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumWidth(250)
        self.widget.setMaximumWidth(300)
        self.widget.setStyleSheet(u"""
            QWidget {
                background-color: #2b303b;
                border: none;
                border-radius: 0;
            }
        """)

        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(20, 40, 20, 40)

        # Sidebar header (frame)
        self.frame = QFrame()
        self.frame.setStyleSheet(u"background-color: transparent;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

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

        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_2.addWidget(self.frame)

        # Sidebar buttons
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

        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.pushButton_2)

        # Spacer to push buttons to top
        self.verticalLayout_2.addStretch(1)

        self.horizontalLayout.addWidget(self.widget)

        # Main content area
        self.content = QWidget()
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: #f8f9fa;")

        self.verticalLayout = QVBoxLayout(self.content)
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout.setSpacing(30)

        # Main title (label)
        self.label = QLabel()
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"""
            QLabel {
                color: #2e3440;
                font-size: 72px;
                font-weight: bold;
                background-color: transparent;
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        # Image (label_2)
        self.label_2 = QLabel()
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setPixmap(QPixmap(u"istockphoto-845329690-612x612.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setMaximumSize(600, 400)
        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignCenter)

        # Subtitle (label_3)
        self.label_3 = QLabel()
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"""
            QLabel {
                color: #4c566a;
                font-size: 26px;
                font-weight: bold;
                background-color: transparent;
            }
        """)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_3)

        # Info box (textBrowser)
        self.textBrowser = QTextBrowser()
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"""
            QTextBrowser {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 12px;
                padding: 20px;
                color: #2e3440;
                font-size: 14px;
                font-weight: normal;
            }
        """)
        self.textBrowser.setMaximumHeight(150)
        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout.addWidget(self.content, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EyeSec - Главная страница", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EyeSec", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Меню", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Авторизация", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Главная страница", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Загрузка данных", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Фильтрация", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Выгрузка", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Настройки", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Выпускная квалификационная работа", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow",
            u"""<!DOCTYPE HTML>
            <html>
            <body>
            <p style="font-size:16px; font-weight:bold; margin-bottom:10px;">
            Система обработки киберугроз.
            </p>
            <p style="margin-bottom:5px;">Разработал: Подлипчук Е.В.</p>
            <p>Руководитель: Фрид А.И.</p>
            </body>
            </html>""", None))