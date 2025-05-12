# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
                               QLineEdit, QWidget, QVBoxLayout, QPushButton, QFrame)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        screen_size = QApplication.primaryScreen().availableGeometry()
        self.setFixedSize(screen_size.width(), screen_size.height())

        # Основной стиль окна
        MainWindow.setStyleSheet(u"""
            QMainWindow {
                background-color: #f5f7fa;
            }
        """)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: transparent;")

        # Главный макет
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)

        # Заголовок (label)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #2E3440;
                background-color: transparent;
                padding: 10px;
                text-align: center;
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        # Контейнер для формы
        self.form_frame = QFrame(self.centralwidget)
        self.form_frame.setObjectName(u"form_frame")
        self.form_frame.setStyleSheet(u"""
            QFrame {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
            }
        """)

        self.form_layout = QVBoxLayout(self.form_frame)
        self.form_layout.setContentsMargins(20, 20, 20, 20)
        self.form_layout.setSpacing(15)

        # Метка для поля ввода (label_2)
        self.label_2 = QLabel(self.form_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #4C566A;
                background-color: transparent;
            }
        """)
        self.form_layout.addWidget(self.label_2)

        # Поле ввода (заменил QTextEdit на QLineEdit)
        self.textEdit = QLineEdit(self.form_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"""
            QLineEdit {
                background-color: #ECEFF4;
                border: 1px solid #D8DEE9;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
                min-height: 30px;
            }
            QLineEdit:focus {
                border: 1px solid #5E81AC;
            }
        """)
        self.form_layout.addWidget(self.textEdit)

        self.label_3 = QLabel(self.form_frame)
        self.label_3.setObjectName(u"label_2")
        self.label_3.setStyleSheet(u"""
                   QLabel {
                       font-size: 14px;
                       font-weight: bold;
                       color: #4C566A;
                       background-color: transparent;
                   }
               """)
        self.form_layout.addWidget(self.label_3)

        self.textEdit_ip = QLineEdit(self.form_frame)
        self.textEdit_ip.setObjectName(u"textEdit")
        self.textEdit_ip.setStyleSheet(u"""
                    QLineEdit {
                        background-color: #ECEFF4;
                        border: 1px solid #D8DEE9;
                        border-radius: 6px;
                        padding: 8px;
                        font-size: 14px;
                        min-height: 30px;
                    }
                    QLineEdit:focus {
                        border: 1px solid #5E81AC;
                    }
                """)
        self.form_layout.addWidget(self.textEdit_ip)

        self.label_4 = QLabel(self.form_frame)
        self.label_4.setObjectName(u"label_2")
        self.label_4.setStyleSheet(u"""
                   QLabel {
                       font-size: 14px;
                       font-weight: bold;
                       color: #4C566A;
                       background-color: transparent;
                   }
               """)
        self.form_layout.addWidget(self.label_4)

        self.textEdit_login = QLineEdit(self.form_frame)
        self.textEdit_login.setObjectName(u"textEdit")
        self.textEdit_login.setStyleSheet(u"""
                            QLineEdit {
                                background-color: #ECEFF4;
                                border: 1px solid #D8DEE9;
                                border-radius: 6px;
                                padding: 8px;
                                font-size: 14px;
                                min-height: 30px;
                            }
                            QLineEdit:focus {
                                border: 1px solid #5E81AC;
                            }
                        """)
        self.form_layout.addWidget(self.textEdit_login)

        self.label_5 = QLabel(self.form_frame)
        self.label_5.setObjectName(u"label_2")
        self.label_5.setStyleSheet(u"""
                   QLabel {
                       font-size: 14px;
                       font-weight: bold;
                       color: #4C566A;
                       background-color: transparent;
                   }
               """)
        self.form_layout.addWidget(self.label_5)

        self.textEdit_passwd = QLineEdit(self.form_frame)
        self.textEdit_passwd.setObjectName(u"textEdit")
        self.textEdit_passwd.setStyleSheet(u"""
                            QLineEdit {
                                background-color: #ECEFF4;
                                border: 1px solid #D8DEE9;
                                border-radius: 6px;
                                padding: 8px;
                                font-size: 14px;
                                min-height: 30px;
                            }
                            QLineEdit:focus {
                                border: 1px solid #5E81AC;
                            }
                        """)
        self.form_layout.addWidget(self.textEdit_passwd)

        self.label_6 = QLabel(self.form_frame)
        self.label_6.setObjectName(u"label_2")
        self.label_6.setStyleSheet(u"""
                           QLabel {
                               font-size: 14px;
                               font-weight: bold;
                               color: #4C566A;
                               background-color: transparent;
                           }
                       """)
        self.form_layout.addWidget(self.label_6)

        self.textEdit_table = QLineEdit(self.form_frame)
        self.textEdit_table.setObjectName(u"textEdit")
        self.textEdit_table.setStyleSheet(u"""
                                    QLineEdit {
                                        background-color: #ECEFF4;
                                        border: 1px solid #D8DEE9;
                                        border-radius: 6px;
                                        padding: 8px;
                                        font-size: 14px;
                                        min-height: 30px;
                                    }
                                    QLineEdit:focus {
                                        border: 1px solid #5E81AC;
                                    }
                                """)
        self.form_layout.addWidget(self.textEdit_table)

        # Кнопка авторизации
        self.auth_button = QPushButton(self.form_frame)
        self.auth_button.setObjectName(u"auth_button")
        self.auth_button.setStyleSheet(u"""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)
        self.auth_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.form_layout.addWidget(self.auth_button)

        self.verticalLayout.addWidget(self.form_frame)
        self.verticalLayout.addStretch()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Авторизация", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Авторизация", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Misp Key", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Database IP", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Database login", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Database password", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Database table", None))
        self.auth_button.setText(QCoreApplication.translate("MainWindow", u"Войти", None))