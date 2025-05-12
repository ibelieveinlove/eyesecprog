## -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1204, 899)
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        font.setBold(True)
        MainWindow.setFont(font)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        MainWindow.setStyleSheet(u"background-color: #f5f7fa;")
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #f5f7fa;")

        # Main title
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 20, 641, 180))
        self.label.setStyleSheet(u"""
            font-size: 100px;
            font-weight: bold;
            color: #2E3440;
            background: transparent;
        """)

        # Sidebar
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 231, 901))

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 231, 941))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setStyleSheet(u"""
            background-color: #2E3440;
            border-right: none;
            border-radius: 0 15px 15px 0;
        """)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 120, 231, 861))

        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setSpacing(5)

        # Buttons
        button_style = u"""
            QPushButton {
                text-align: left;
                padding: 12px 15px;
                color: #ECEFF4;
                background-color: transparent;
                border: none;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #3B4252;
            }
        """

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(button_style)
        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(button_style)
        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(button_style)
        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(button_style)
        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(button_style)
        self.verticalLayout_2.addWidget(self.pushButton_2)

        # Sidebar header
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 30, 101, 41))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: #ECEFF4; background-color: transparent;")

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 30, 91, 41))
        self.pushButton.setStyleSheet(u"""
            color: #ECEFF4;
            background-color: #3B4252;
            border: none;
            border-radius: 8px;
            padding: 5px;
        """)

        # Content area
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(400, 700, 561, 151))
        self.textBrowser.setStyleSheet(u"""
            background-color: #ECEFF4;
            border: none;
            border-radius: 12px;
            padding: 15px;
            color: #2E3440;
            font-size: 14px;
        """)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 220, 551, 261))
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setPixmap(QPixmap(u"istockphoto-845329690-612x612.jpg"))

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 500, 781, 101))
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT"])
        font3.setPointSize(26)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: #4C566A; background-color: transparent;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" Eye Sec - \u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EyeSec", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:600;\">\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u043a\u0438\u0431\u0435\u0440\u0443\u0433\u0440\u043e\u0437.<br />\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043b: \u041f\u043e\u0434\u043b\u0438\u043f\u0447\u0443\u043a \u0415.\u0412.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:600;\">\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c: \u0424\u0440\u0438\u0434 \u0410.\u0418.</span></p></body></html>", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u0443\u0441\u043a\u043d\u0430\u044f \u043a\u0432\u0430\u043b\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
