# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(631, 567)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_4.addWidget(self.listWidget_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.point = QtWidgets.QPlainTextEdit(Form)
        self.point.setMinimumSize(QtCore.QSize(0, 35))
        self.point.setMaximumSize(QtCore.QSize(16777215, 35))
        self.point.setReadOnly(True)
        self.point.setObjectName("point")
        self.verticalLayout_5.addWidget(self.point)
        self.listWidget = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_5.addWidget(self.listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(95, 95, 97);\n"
"font: 75 9pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate"))
        self.label.setText(_translate("Form", "Evaluate the performance Fantasy Cricket"))
        self.plainTextEdit.setPlainText(_translate("Form", "Players"))
        self.point.setPlainText(_translate("Form", "Points: 00"))
        self.pushButton.setText(_translate("Form", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

