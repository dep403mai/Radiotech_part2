# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created: Tue Aug 19 12:06:03 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(488, 324)
        MainWindow.setMinimumSize(QtCore.QSize(488, 324))
        MainWindow.setMaximumSize(QtCore.QSize(488, 324))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(20, 14, 445, 280))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_14 = QtGui.QLabel(self.splitter_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_7)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.FC = QtGui.QLineEdit(self.widget)
        self.FC.setFrame(True)
        self.FC.setObjectName(_fromUtf8("FC"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.FC)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.FD = QtGui.QLineEdit(self.widget)
        self.FD.setObjectName(_fromUtf8("FD"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.FD)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.N = QtGui.QLineEdit(self.widget)
        self.N.setObjectName(_fromUtf8("N"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.N)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.SPEED = QtGui.QLineEdit(self.widget)
        self.SPEED.setObjectName(_fromUtf8("SPEED"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.SPEED)
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.FDD = QtGui.QLineEdit(self.widget)
        self.FDD.setObjectName(_fromUtf8("FDD"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.FDD)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.A_NOISE = QtGui.QLineEdit(self.widget)
        self.A_NOISE.setObjectName(_fromUtf8("A_NOISE"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.A_NOISE)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_5)
        self.A_SIGNAL = QtGui.QLineEdit(self.widget)
        self.A_SIGNAL.setObjectName(_fromUtf8("A_SIGNAL"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.A_SIGNAL)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_6)
        self.DETECTION_THRESHOLD = QtGui.QDoubleSpinBox(self.widget)
        self.DETECTION_THRESHOLD.setSingleStep(0.05)
        self.DETECTION_THRESHOLD.setProperty("value", 0.3)
        self.DETECTION_THRESHOLD.setObjectName(_fromUtf8("DETECTION_THRESHOLD"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.DETECTION_THRESHOLD)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.formLayout_3 = QtGui.QFormLayout(self.widget1)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.EXPER_COUNT = QtGui.QSpinBox(self.widget1)
        self.EXPER_COUNT.setProperty("value", 1)
        self.EXPER_COUNT.setObjectName(_fromUtf8("EXPER_COUNT"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.EXPER_COUNT)
        self.CONDUCT_EXPERIMENT = QtGui.QPushButton(self.widget1)
        self.CONDUCT_EXPERIMENT.setObjectName(_fromUtf8("CONDUCT_EXPERIMENT"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.CONDUCT_EXPERIMENT)
        self.PLOT_GRAPH = QtGui.QPushButton(self.widget1)
        self.PLOT_GRAPH.setObjectName(_fromUtf8("PLOT_GRAPH"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.SpanningRole, self.PLOT_GRAPH)
        self.widget2 = QtGui.QWidget(self.splitter)
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.formLayout_2 = QtGui.QFormLayout(self.widget2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_13 = QtGui.QLabel(self.widget2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.EXPECTED_VALUE = QtGui.QLabel(self.widget2)
        self.EXPECTED_VALUE.setObjectName(_fromUtf8("EXPECTED_VALUE"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.EXPECTED_VALUE)
        self.label_11 = QtGui.QLabel(self.widget2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.DISPERSION = QtGui.QLabel(self.widget2)
        self.DISPERSION.setObjectName(_fromUtf8("DISPERSION"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.DISPERSION)
        self.label_10 = QtGui.QLabel(self.widget2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Моделирование приемо-передающей системы", None))
        self.label_14.setText(_translate("MainWindow", "Амплитудная манипуляция с помехоусточивым кодированим Хемминг(7,4,3)", None))
        self.label_7.setText(_translate("MainWindow", "Параметры системы", None))
        self.label.setText(_translate("MainWindow", "Частота несущей [Гц]", None))
        self.FC.setText(_translate("MainWindow", "10", None))
        self.label_9.setText(_translate("MainWindow", "Частота дискретизации несущего сигнала", None))
        self.FD.setText(_translate("MainWindow", "200", None))
        self.label_2.setText(_translate("MainWindow", "Количество передающихся символов", None))
        self.N.setText(_translate("MainWindow", "32", None))
        self.label_3.setText(_translate("MainWindow", "Символьная скорость", None))
        self.SPEED.setText(_translate("MainWindow", "10", None))
        self.label_12.setText(_translate("MainWindow", "Частота дискретизации исходного сигнала", None))
        self.FDD.setText(_translate("MainWindow", "500", None))
        self.label_4.setText(_translate("MainWindow", "Амплитуда шума", None))
        self.A_NOISE.setText(_translate("MainWindow", "1", None))
        self.label_5.setText(_translate("MainWindow", "Амплитуда сигнала", None))
        self.A_SIGNAL.setText(_translate("MainWindow", "1.25", None))
        self.label_6.setText(_translate("MainWindow", "Порог детектирования", None))
        self.label_8.setText(_translate("MainWindow", "Количество экспериментов", None))
        self.CONDUCT_EXPERIMENT.setText(_translate("MainWindow", "Провести эксперимент", None))
        self.PLOT_GRAPH.setText(_translate("MainWindow", "Построить графики", None))
        self.label_13.setText(_translate("MainWindow", "Результаты", None))
        self.EXPECTED_VALUE.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "Дисперсия", None))
        self.DISPERSION.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Мат. ожидание", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created: Tue Aug 19 12:08:07 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(488, 324)
        MainWindow.setMinimumSize(QtCore.QSize(488, 324))
        MainWindow.setMaximumSize(QtCore.QSize(488, 324))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(20, 14, 445, 280))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_14 = QtGui.QLabel(self.splitter_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_7)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.FC = QtGui.QLineEdit(self.layoutWidget)
        self.FC.setFrame(True)
        self.FC.setObjectName(_fromUtf8("FC"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.FC)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.FD = QtGui.QLineEdit(self.layoutWidget)
        self.FD.setObjectName(_fromUtf8("FD"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.FD)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.N = QtGui.QLineEdit(self.layoutWidget)
        self.N.setObjectName(_fromUtf8("N"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.N)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.SPEED = QtGui.QLineEdit(self.layoutWidget)
        self.SPEED.setObjectName(_fromUtf8("SPEED"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.SPEED)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.FDD = QtGui.QLineEdit(self.layoutWidget)
        self.FDD.setObjectName(_fromUtf8("FDD"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.FDD)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.A_NOISE = QtGui.QLineEdit(self.layoutWidget)
        self.A_NOISE.setObjectName(_fromUtf8("A_NOISE"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.A_NOISE)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_5)
        self.A_SIGNAL = QtGui.QLineEdit(self.layoutWidget)
        self.A_SIGNAL.setObjectName(_fromUtf8("A_SIGNAL"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.A_SIGNAL)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_6)
        self.DETECTION_THRESHOLD = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.DETECTION_THRESHOLD.setSingleStep(0.05)
        self.DETECTION_THRESHOLD.setProperty("value", 0.3)
        self.DETECTION_THRESHOLD.setObjectName(_fromUtf8("DETECTION_THRESHOLD"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.DETECTION_THRESHOLD)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout_3 = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.EXPER_COUNT = QtGui.QSpinBox(self.layoutWidget1)
        self.EXPER_COUNT.setProperty("value", 1)
        self.EXPER_COUNT.setObjectName(_fromUtf8("EXPER_COUNT"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.EXPER_COUNT)
        self.CONDUCT_EXPERIMENT = QtGui.QPushButton(self.layoutWidget1)
        self.CONDUCT_EXPERIMENT.setObjectName(_fromUtf8("CONDUCT_EXPERIMENT"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.CONDUCT_EXPERIMENT)
        self.PLOT_GRAPH = QtGui.QPushButton(self.layoutWidget1)
        self.PLOT_GRAPH.setObjectName(_fromUtf8("PLOT_GRAPH"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.SpanningRole, self.PLOT_GRAPH)
        self.layoutWidget2 = QtGui.QWidget(self.splitter)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.EXPECTED_VALUE = QtGui.QLabel(self.layoutWidget2)
        self.EXPECTED_VALUE.setObjectName(_fromUtf8("EXPECTED_VALUE"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.EXPECTED_VALUE)
        self.label_11 = QtGui.QLabel(self.layoutWidget2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.DISPERSION = QtGui.QLabel(self.layoutWidget2)
        self.DISPERSION.setObjectName(_fromUtf8("DISPERSION"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.DISPERSION)
        self.label_10 = QtGui.QLabel(self.layoutWidget2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_13 = QtGui.QLabel(self.layoutWidget2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Моделирование приемо-передающей системы", None))
        self.label_14.setText(_translate("MainWindow", "Амплитудная манипуляция с помехоусточивым кодированим Хемминг(7,4,3)", None))
        self.label_7.setText(_translate("MainWindow", "Параметры системы", None))
        self.label.setText(_translate("MainWindow", "Частота несущей [Гц]", None))
        self.FC.setText(_translate("MainWindow", "10", None))
        self.label_9.setText(_translate("MainWindow", "Частота дискретизации несущего сигнала", None))
        self.FD.setText(_translate("MainWindow", "200", None))
        self.label_2.setText(_translate("MainWindow", "Количество передающихся символов", None))
        self.N.setText(_translate("MainWindow", "32", None))
        self.label_3.setText(_translate("MainWindow", "Символьная скорость", None))
        self.SPEED.setText(_translate("MainWindow", "10", None))
        self.label_12.setText(_translate("MainWindow", "Частота дискретизации исходного сигнала", None))
        self.FDD.setText(_translate("MainWindow", "500", None))
        self.label_4.setText(_translate("MainWindow", "Амплитуда шума", None))
        self.A_NOISE.setText(_translate("MainWindow", "1", None))
        self.label_5.setText(_translate("MainWindow", "Амплитуда сигнала", None))
        self.A_SIGNAL.setText(_translate("MainWindow", "1.25", None))
        self.label_6.setText(_translate("MainWindow", "Порог детектирования", None))
        self.label_8.setText(_translate("MainWindow", "Количество экспериментов", None))
        self.CONDUCT_EXPERIMENT.setText(_translate("MainWindow", "Провести эксперимент", None))
        self.PLOT_GRAPH.setText(_translate("MainWindow", "Построить графики", None))
        self.EXPECTED_VALUE.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "Дисперсия", None))
        self.DISPERSION.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Мат. ожидание", None))
        self.label_13.setText(_translate("MainWindow", "Результаты", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created: Tue Aug 19 15:07:09 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(488, 324)
        MainWindow.setMinimumSize(QtCore.QSize(488, 324))
        MainWindow.setMaximumSize(QtCore.QSize(488, 324))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(20, 14, 445, 280))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_14 = QtGui.QLabel(self.splitter_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_7)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.FC = QtGui.QLineEdit(self.layoutWidget)
        self.FC.setFrame(True)
        self.FC.setObjectName(_fromUtf8("FC"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.FC)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.FD = QtGui.QLineEdit(self.layoutWidget)
        self.FD.setObjectName(_fromUtf8("FD"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.FD)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.N = QtGui.QLineEdit(self.layoutWidget)
        self.N.setObjectName(_fromUtf8("N"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.N)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.SPEED = QtGui.QLineEdit(self.layoutWidget)
        self.SPEED.setObjectName(_fromUtf8("SPEED"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.SPEED)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.FDD = QtGui.QLineEdit(self.layoutWidget)
        self.FDD.setObjectName(_fromUtf8("FDD"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.FDD)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.A_NOISE = QtGui.QLineEdit(self.layoutWidget)
        self.A_NOISE.setObjectName(_fromUtf8("A_NOISE"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.A_NOISE)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_5)
        self.A_SIGNAL = QtGui.QLineEdit(self.layoutWidget)
        self.A_SIGNAL.setObjectName(_fromUtf8("A_SIGNAL"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.A_SIGNAL)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_6)
        self.DETECTION_THRESHOLD = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.DETECTION_THRESHOLD.setSingleStep(0.05)
        self.DETECTION_THRESHOLD.setProperty("value", 0.3)
        self.DETECTION_THRESHOLD.setObjectName(_fromUtf8("DETECTION_THRESHOLD"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.DETECTION_THRESHOLD)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout_3 = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.EXPER_COUNT = QtGui.QSpinBox(self.layoutWidget1)
        self.EXPER_COUNT.setProperty("value", 1)
        self.EXPER_COUNT.setObjectName(_fromUtf8("EXPER_COUNT"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.EXPER_COUNT)
        self.CONDUCT_EXPERIMENT = QtGui.QPushButton(self.layoutWidget1)
        self.CONDUCT_EXPERIMENT.setObjectName(_fromUtf8("CONDUCT_EXPERIMENT"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.CONDUCT_EXPERIMENT)
        self.PLOT_GRAPH = QtGui.QPushButton(self.layoutWidget1)
        self.PLOT_GRAPH.setObjectName(_fromUtf8("PLOT_GRAPH"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.SpanningRole, self.PLOT_GRAPH)
        self.layoutWidget2 = QtGui.QWidget(self.splitter)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.EXPECTED_VALUE = QtGui.QLabel(self.layoutWidget2)
        self.EXPECTED_VALUE.setObjectName(_fromUtf8("EXPECTED_VALUE"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.EXPECTED_VALUE)
        self.label_11 = QtGui.QLabel(self.layoutWidget2)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.DISPERSION = QtGui.QLabel(self.layoutWidget2)
        self.DISPERSION.setObjectName(_fromUtf8("DISPERSION"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.DISPERSION)
        self.label_10 = QtGui.QLabel(self.layoutWidget2)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_13 = QtGui.QLabel(self.layoutWidget2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Моделирование приемо-передающей системы", None))
        self.label_14.setText(_translate("MainWindow", "Амплитудная манипуляция с помехоусточивым кодированим Хемминг(7,4,3)", None))
        self.label_7.setText(_translate("MainWindow", "Параметры системы", None))
        self.label.setText(_translate("MainWindow", "Частота несущей [Гц]", None))
        self.FC.setText(_translate("MainWindow", "10", None))
        self.label_9.setText(_translate("MainWindow", "Частота дискретизации несущего сигнала", None))
        self.FD.setText(_translate("MainWindow", "200", None))
        self.label_2.setText(_translate("MainWindow", "Количество передающихся символов", None))
        self.N.setText(_translate("MainWindow", "32", None))
        self.label_3.setText(_translate("MainWindow", "Символьная скорость", None))
        self.SPEED.setText(_translate("MainWindow", "10", None))
        self.label_12.setText(_translate("MainWindow", "Частота дискретизации исходного сигнала", None))
        self.FDD.setText(_translate("MainWindow", "500", None))
        self.label_4.setText(_translate("MainWindow", "Амплитуда шума", None))
        self.A_NOISE.setText(_translate("MainWindow", "1", None))
        self.label_5.setText(_translate("MainWindow", "Амплитуда сигнала", None))
        self.A_SIGNAL.setText(_translate("MainWindow", "1.25", None))
        self.label_6.setText(_translate("MainWindow", "Порог детектирования", None))
        self.label_8.setText(_translate("MainWindow", "Количество экспериментов", None))
        self.CONDUCT_EXPERIMENT.setText(_translate("MainWindow", "Провести эксперимент", None))
        self.PLOT_GRAPH.setText(_translate("MainWindow", "Построить графики", None))
        self.EXPECTED_VALUE.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "Дисперсия битовой ошибки", None))
        self.DISPERSION.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Среднее значение битовой ошибки", None))
        self.label_13.setText(_translate("MainWindow", "Результаты", None))

