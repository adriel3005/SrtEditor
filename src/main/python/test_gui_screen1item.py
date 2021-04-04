# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gui_screen1item.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1647, 1154)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.QFrameVideo = QtWidgets.QFrame(self.centralwidget)
        self.QFrameVideo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.QFrameVideo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QFrameVideo.setObjectName("QFrameVideo")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.QFrameVideo)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.QVideoBoxVLayout = QtWidgets.QVBoxLayout()
        self.QVideoBoxVLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.QVideoBoxVLayout.setObjectName("QVideoBoxVLayout")
        self.gridLayout_3.addLayout(self.QVideoBoxVLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.QFrameVideo, 2, 2, 2, 3)
        self.addremoveWidgetContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addremoveWidgetContainer.sizePolicy().hasHeightForWidth())
        self.addremoveWidgetContainer.setSizePolicy(sizePolicy)
        self.addremoveWidgetContainer.setMinimumSize(QtCore.QSize(150, 50))
        self.addremoveWidgetContainer.setObjectName("addremoveWidgetContainer")
        self.addButton = QtWidgets.QPushButton(self.addremoveWidgetContainer)
        self.addButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.addButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plus/plus-24844_1280.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.addremoveWidgetContainer)
        self.removeButton.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.removeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plus/MinusSign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon1)
        self.removeButton.setIconSize(QtCore.QSize(40, 40))
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.addremoveWidgetContainer, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(400, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.translateEnglish = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.translateEnglish.setFont(font)
        self.translateEnglish.setObjectName("translateEnglish")
        self.horizontalLayout.addWidget(self.translateEnglish)
        self.translateSpanish = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.translateSpanish.setFont(font)
        self.translateSpanish.setObjectName("translateSpanish")
        self.horizontalLayout.addWidget(self.translateSpanish)
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 1)
        self.currentLyrics = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.currentLyrics.setFont(font)
        self.currentLyrics.setFrameShadow(QtWidgets.QFrame.Plain)
        self.currentLyrics.setText("")
        self.currentLyrics.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLyrics.setWordWrap(True)
        self.currentLyrics.setObjectName("currentLyrics")
        self.gridLayout.addWidget(self.currentLyrics, 4, 2, 1, 3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 826))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 2, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.currentTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTime.sizePolicy().hasHeightForWidth())
        self.currentTime.setSizePolicy(sizePolicy)
        self.currentTime.setMinimumSize(QtCore.QSize(175, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentTime.setFont(font)
        self.currentTime.setText("")
        self.currentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime.setObjectName("currentTime")
        self.gridLayout_2.addWidget(self.currentTime, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.oneMForward = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oneMForward.setFont(font)
        self.oneMForward.setObjectName("oneMForward")
        self.horizontalLayout_3.addWidget(self.oneMForward)
        self.fiveForward = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fiveForward.setFont(font)
        self.fiveForward.setObjectName("fiveForward")
        self.horizontalLayout_3.addWidget(self.fiveForward)
        self.tenForward = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tenForward.setFont(font)
        self.tenForward.setObjectName("tenForward")
        self.horizontalLayout_3.addWidget(self.tenForward)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 4, 1, 1)
        self.lyricsTitle = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lyricsTitle.sizePolicy().hasHeightForWidth())
        self.lyricsTitle.setSizePolicy(sizePolicy)
        self.lyricsTitle.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lyricsTitle.setFont(font)
        self.lyricsTitle.setObjectName("lyricsTitle")
        self.gridLayout.addWidget(self.lyricsTitle, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tenBack = QtWidgets.QPushButton(self.centralwidget)
        self.tenBack.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tenBack.setFont(font)
        self.tenBack.setObjectName("tenBack")
        self.horizontalLayout_2.addWidget(self.tenBack)
        self.fiveBack = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fiveBack.setFont(font)
        self.fiveBack.setObjectName("fiveBack")
        self.horizontalLayout_2.addWidget(self.fiveBack)
        self.oneMBack = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oneMBack.setFont(font)
        self.oneMBack.setObjectName("oneMBack")
        self.horizontalLayout_2.addWidget(self.oneMBack)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)
        self.textAppendList = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textAppendList.setFont(font)
        self.textAppendList.setObjectName("textAppendList")
        self.textAppendList.addItem("")
        self.textAppendList.setItemText(0, "")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.textAppendList.addItem("")
        self.gridLayout.addWidget(self.textAppendList, 5, 0, 1, 1)
        self.createSRTButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.createSRTButton.setFont(font)
        self.createSRTButton.setAutoFillBackground(False)
        self.createSRTButton.setCheckable(False)
        self.createSRTButton.setObjectName("createSRTButton")
        self.gridLayout.addWidget(self.createSRTButton, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1647, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEstilos = QtWidgets.QMenu(self.menubar)
        self.menuEstilos.setObjectName("menuEstilos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Video = QtWidgets.QAction(MainWindow)
        self.actionOpen_Video.setObjectName("actionOpen_Video")
        self.actionInportar_Subtitulos_srt = QtWidgets.QAction(MainWindow)
        self.actionInportar_Subtitulos_srt.setObjectName("actionInportar_Subtitulos_srt")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionLight_Mode = QtWidgets.QAction(MainWindow)
        self.actionLight_Mode.setObjectName("actionLight_Mode")
        self.actionDark_Mode_2 = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode_2.setObjectName("actionDark_Mode_2")
        self.actionRed_Palette = QtWidgets.QAction(MainWindow)
        self.actionRed_Palette.setObjectName("actionRed_Palette")
        self.actionBlue_Palette = QtWidgets.QAction(MainWindow)
        self.actionBlue_Palette.setObjectName("actionBlue_Palette")
        self.menuFile.addAction(self.actionInportar_Subtitulos_srt)
        self.menuEstilos.addAction(self.actionLight_Mode)
        self.menuEstilos.addAction(self.actionDark_Mode_2)
        self.menuEstilos.addAction(self.actionRed_Palette)
        self.menuEstilos.addAction(self.actionBlue_Palette)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEstilos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SRT Editor"))
        self.translateEnglish.setText(_translate("MainWindow", "English"))
        self.translateSpanish.setText(_translate("MainWindow", "Español"))
        self.oneMForward.setText(_translate("MainWindow", "100 msegundos ->"))
        self.fiveForward.setText(_translate("MainWindow", "5 segundos ->"))
        self.tenForward.setText(_translate("MainWindow", "10 segundos ->"))
        self.lyricsTitle.setText(_translate("MainWindow", "Letra"))
        self.tenBack.setText(_translate("MainWindow", "<- 10 segundos"))
        self.fiveBack.setText(_translate("MainWindow", "<- 5 segundos"))
        self.oneMBack.setText(_translate("MainWindow", "<-100msegundos"))
        self.textAppendList.setItemText(1, _translate("MainWindow", "❤"))
        self.textAppendList.setItemText(2, _translate("MainWindow", "♥♥"))
        self.textAppendList.setItemText(3, _translate("MainWindow", "♪"))
        self.textAppendList.setItemText(4, _translate("MainWindow", "♪♪"))
        self.textAppendList.setItemText(5, _translate("MainWindow", "𝄞"))
        self.textAppendList.setItemText(6, _translate("MainWindow", "𝄞𝄞"))
        self.textAppendList.setItemText(7, _translate("MainWindow", "💘"))
        self.textAppendList.setItemText(8, _translate("MainWindow", "💘💘"))
        self.textAppendList.setItemText(9, _translate("MainWindow", "🎹"))
        self.textAppendList.setItemText(10, _translate("MainWindow", "🎸"))
        self.textAppendList.setItemText(11, _translate("MainWindow", "🎶"))
        self.textAppendList.setItemText(12, _translate("MainWindow", "🎙"))
        self.textAppendList.setItemText(13, _translate("MainWindow", "🎵"))
        self.createSRTButton.setText(_translate("MainWindow", "Crear SRT"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEstilos.setTitle(_translate("MainWindow", "Estilos"))
        self.actionOpen_Video.setText(_translate("MainWindow", "Open Video"))
        self.actionInportar_Subtitulos_srt.setText(_translate("MainWindow", "Importar Subtitulos srt"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionLight_Mode.setText(_translate("MainWindow", "Light Mode"))
        self.actionDark_Mode_2.setText(_translate("MainWindow", "Dark Mode"))
        self.actionRed_Palette.setText(_translate("MainWindow", "Red Palette"))
        self.actionBlue_Palette.setText(_translate("MainWindow", "Blue Palette"))
import plusandminus_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
