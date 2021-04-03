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
        MainWindow.resize(1274, 862)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.QFrameVideo = QtWidgets.QFrame(self.centralwidget)
        self.QFrameVideo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.QFrameVideo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QFrameVideo.setObjectName("QFrameVideo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.QFrameVideo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 731, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.QVideoBoxVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.QVideoBoxVLayout.setContentsMargins(0, 0, 0, 0)
        self.QVideoBoxVLayout.setObjectName("QVideoBoxVLayout")
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
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.currentTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentTime.setFont(font)
        self.currentTime.setText("")
        self.currentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime.setObjectName("currentTime")
        self.gridLayout_2.addWidget(self.currentTime, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 3, 1, 1)
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
        self.createSRTButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.createSRTButton.setFont(font)
        self.createSRTButton.setAutoFillBackground(False)
        self.createSRTButton.setStyleSheet("background-color: rgb(169, 180, 200);")
        self.createSRTButton.setCheckable(False)
        self.createSRTButton.setObjectName("createSRTButton")
        self.gridLayout.addWidget(self.createSRTButton, 5, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 5)
        self.mediaPlayerTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mediaPlayerTitle.setFont(font)
        self.mediaPlayerTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mediaPlayerTitle.setObjectName("mediaPlayerTitle")
        self.gridLayout.addWidget(self.mediaPlayerTitle, 0, 4, 1, 1)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 631))
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.translateEnglish = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.translateEnglish.setFont(font)
        self.translateEnglish.setObjectName("translateEnglish")
        self.horizontalLayout.addWidget(self.translateEnglish)
        self.translateSpanish = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.translateSpanish.setFont(font)
        self.translateSpanish.setObjectName("translateSpanish")
        self.horizontalLayout.addWidget(self.translateSpanish)
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1274, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Video = QtWidgets.QAction(MainWindow)
        self.actionOpen_Video.setObjectName("actionOpen_Video")
        self.menuFile.addAction(self.actionOpen_Video)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lyricsTitle.setText(_translate("MainWindow", "Lyrics"))
        self.createSRTButton.setText(_translate("MainWindow", "Create SRT"))
        self.mediaPlayerTitle.setText(_translate("MainWindow", "Media Player"))
        self.translateEnglish.setText(_translate("MainWindow", "English"))
        self.translateSpanish.setText(_translate("MainWindow", "Español"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Video.setText(_translate("MainWindow", "Open Video"))
import plusandminus_rc
