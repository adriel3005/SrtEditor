from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton, QStyle, QSlider, QStatusBar
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import  QVideoWidget
#from SRT_GUI_Skeleton import Ui_MainWindow
from test_gui_screen1item import Ui_MainWindow
#from test_gui_screen1itempromotedlyrics import Ui_MainWindow
# import from below allows the OnAdd function to work
from PyQt5 import QtCore, QtGui, QtWidgets
from google_trans_new import google_translator


import sip
import sys



class Main(QMainWindow, Ui_MainWindow):

    lyricList = []
    lyricCount = 0
    videoPath = ""
    videoName = ""

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.removeButton.clicked.connect(self.OnRemove)
        self.addButton.clicked.connect(self.OnAdd)
        self.createSRTButton.clicked.connect(self.CreateSRT)
        self.actionOpen_Video.triggered.connect(self.OpenVideoFile)
        #self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        #Video
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()

        openButton = QPushButton("Open Video")
        openButton.setToolTip("Open Video File")
        openButton.setStatusTip("Open Video File")
        openButton.setFixedHeight(24)
        openButton.setIconSize(btnSize)
        openButton.setFont(QFont("Noto Sans", 8))
        openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
        openButton.clicked.connect(self.open)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(24)
        self.playButton.setIconSize(btnSize)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Noto Sans", 7))
        self.statusBar.setFixedHeight(14)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        #self.QVideoBoxVLayout = QVBoxLayout()
        self.QVideoBoxVLayout.addWidget(videoWidget)
        self.QVideoBoxVLayout.addLayout(controlLayout)
        self.QVideoBoxVLayout.addWidget(self.statusBar)

        self.setLayout(self.QVideoBoxVLayout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        # Every 200 ms
        self.mediaPlayer.setNotifyInterval(200)
        self.translator = google_translator()
        self.statusBar.showMessage("Ready")

    def SetCurrentTimeText(self, millis):
        millis = int(millis)
        seconds = (millis / 1000) % 60
        seconds = int(seconds)
        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)

        sMillis = self.ThreeCharSyntax(str(millis))
        sSeconds = self.TwoCharSyntax(str(seconds))
        sMinutes = self.TwoCharSyntax(str(minutes))

        self.currentTime.setText("Current time " + sMinutes + ":" + sSeconds + ":" + sMillis)


    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona los mediose",".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()
            self.videoPath = fileName
            self.videoName = self.videoPath.split("/")[-1]

    def OpenVideoFile(self):
        #self.videoPath, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.videoPath, _ = QFileDialog.getOpenFileName(self,"Select Video File", "","Video File (*.mp4 *.avi *.ogv)", options=options)
        self.videoName = self.videoPath.split("/")[-1]

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
            # Show exact time when paused
            self.SetCurrentTimeText(self.mediaPlayer.position())
            self.SetCurrentLyrics(self.mediaPlayer.position())
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)
        self.SetCurrentTimeText(self.mediaPlayer.position())
        self.SetCurrentLyrics(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())


    def OnRemove(self):
        if len(self.lyricList) > 0 :
            self.verticalLayout.removeWidget(self.lyricList[-1])
            sip.delete(self.lyricList[-1])
            self.lyricCount -= 1
            del (self.lyricList[-1])

    def OnAdd(self):
        self.lyricGroup = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lyricGroup.sizePolicy().hasHeightForWidth())
        self.lyricGroup.setSizePolicy(sizePolicy)
        self.lyricGroup.setMinimumSize(QtCore.QSize(0, 150))
        self.lyricGroup.setMaximumSize(QtCore.QSize(600, 100))
        self.lyricGroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lyricGroup.setObjectName("lyricGroup")

        self.gridLayout = QtWidgets.QGridLayout(self.lyricGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.startLabel = QtWidgets.QLabel(self.lyricGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startLabel.setFont(font)
        self.startLabel.setObjectName("startLabel")
        self.startLabel.setText("Start:")
        self.gridLayout.addWidget(self.startLabel, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lyricsText = QtWidgets.QPlainTextEdit(self.lyricGroup)
        self.lyricsText.setObjectName("lyricsText")
        self.lyricsText.setFont(font)
        self.gridLayout.addWidget(self.lyricsText, 0, 2, 2, 1)
        self.endLabel = QtWidgets.QLabel(self.lyricGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endLabel.setFont(font)
        self.endLabel.setObjectName("endLabel")
        self.endLabel.setText("End:")
        self.gridLayout.addWidget(self.endLabel, 1, 0, 1, 1)

        self.endTime = QtWidgets.QTimeEdit(self.lyricGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endTime.sizePolicy().hasHeightForWidth())
        self.endTime.setSizePolicy(sizePolicy)
        self.endTime.setMinimumSize(QtCore.QSize(100, 30))
        self.endTime.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.endTime.setFont(font)
        self.endTime.setObjectName("endTime")
        self.endTime.setDisplayFormat("mm:ss:zzz")
        self.gridLayout.addWidget(self.endTime, 1, 1, 1, 1)

        self.startTime = QtWidgets.QTimeEdit(self.lyricGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTime.sizePolicy().hasHeightForWidth())
        self.startTime.setSizePolicy(sizePolicy)
        self.startTime.setMinimumSize(QtCore.QSize(100, 30))
        self.startTime.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.startTime.setFont(font)
        self.startTime.setCurrentSection(QtWidgets.QDateTimeEdit.MSecSection)
        self.startTime.setCurrentSectionIndex(2)
        self.startTime.setTime(QtCore.QTime(0, 0, 0))
        self.startTime.setObjectName("startTime")
        self.startTime.setDisplayFormat("mm:ss:zzz")

        self.gridLayout.addWidget(self.startTime, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.lyricGroup, 0, QtCore.Qt.AlignTop)

        # add to list
        self.lyricList.append(self.lyricGroup)
        self.lyricCount += 1

    def CreateSRT(self):
        #print(len(self.lyricList))

        # For progress bar
        progressCount = 1

        # Check to see if file has been open
        if self.videoPath:
            self.newVideoPath = self.videoPath.split(".")[0]
            print(self.newVideoPath + ".srt")
            srtFile = open(self.newVideoPath + ".srt", "w")

            for i in range(len(self.lyricList)):
                # lyrics
                childLyricsText = self.lyricList[i].findChild(QtWidgets.QPlainTextEdit, "lyricsText")

                # start Time
                ## Format: hh:mm:ss:zzz
                childStartTime = self.lyricList[i].findChild(QtWidgets.QTimeEdit, "startTime").time()

                # end Time
                childEndTime = self.lyricList[i].findChild(QtWidgets.QTimeEdit, "endTime").time()

                print("Start time : " + str(childStartTime.minute()) + str(childStartTime.second()) + str(
                    childStartTime.msec()))

                # Number of iteration
                srtFile.write(str(progressCount) + "\n")

                # start time
                minuteTime = self.TwoCharSyntax(str(childStartTime.minute()))
                secondTime = self.TwoCharSyntax(str(childStartTime.second()))
                mSecTime = self.ThreeCharSyntax(str(childStartTime.msec()))
                srtFile.write("00:"+minuteTime+":"+secondTime+","+mSecTime + " --> ")

                # end time
                minuteTime = self.TwoCharSyntax(str(childEndTime.minute()))
                secondTime = self.TwoCharSyntax(str(childEndTime.second()))
                mSecTime = self.ThreeCharSyntax(str(childEndTime.msec()))
                srtFile.write("00:"+minuteTime + ":" + secondTime + "," + mSecTime)

                # Lyrics

                if self.translateEnglish.isChecked() and self.translateSpanish.isChecked():
                    result = self.translator.translate(childLyricsText.toPlainText(), lang_tgt='en')
                    srtFile.write("\n" + result + "\n")
                    result = self.translator.translate(childLyricsText.toPlainText(), lang_tgt='es')
                    srtFile.write(result + "\n\n")
                elif self.translateEnglish.isChecked():
                    result = self.translator.translate(childLyricsText.toPlainText(), lang_tgt='en')
                    srtFile.write("\n" + result + "\n\n")
                elif self.translateSpanish.isChecked():
                    result = self.translator.translate(childLyricsText.toPlainText(), lang_tgt='es')
                    srtFile.write("\n" + result + "\n\n")
                else:
                    srtFile.write("\n" + childLyricsText.toPlainText() + "\n\n")

                #srtFile.write("\n" + childLyricsText.toPlainText() + "\n\n")
                progressCount += 1

        else:
            self.ShowPopUpMessage()

    # check if string is only 1 character
    def TwoCharSyntax(self, str):
        if len(str) != 2:
            return "0"+str
        else:
            return str

    #Make into 3 char
    def ThreeCharSyntax(self, str):
        if len(str) == 1:
            return "00" + str
        elif len(str) == 2:
            return "0" + str
        elif len(str) >= 4:
            return str[-3:]
        else:
            return str

    def SetCurrentLyrics(self, currentTime):
        for i in range(len(self.lyricList)):
            # start Time
            ## Format: hh:mm:ss:zzz
            childStartTime = self.lyricList[i].findChild(QtWidgets.QTimeEdit, "startTime").time()

            # convert to msecs
            minuteTime = childStartTime.minute()
            secondTime = childStartTime.second()
            mSecTime = childStartTime.msec()
            startTotal = (minuteTime * 60000) + (secondTime * 1000) + mSecTime

            # end Time
            childEndTime = self.lyricList[i].findChild(QtWidgets.QTimeEdit, "endTime").time()

            # convert to msecs
            minuteTime = childEndTime.minute()
            secondTime = childEndTime.second()
            mSecTime = childEndTime.msec()
            endTotal = (minuteTime * 60000) + (secondTime * 1000) + mSecTime

            if currentTime >= startTotal and currentTime <= endTotal:
                childLyricsText = self.lyricList[i].findChild(QtWidgets.QPlainTextEdit, "lyricsText")
                self.currentLyrics.setText(childLyricsText.toPlainText())


    def ShowPopUpMessage(self):
        errorMsg = QMessageBox()
        errorMsg.setWindowTitle("Error")
        errorMsg.setText("Por favor selecciona un video primero")
        x = errorMsg.exec_()


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    #app = QApplication(sys.argv)
    window = Main()
    #window.resize(250, 150)
    #window.show()
    window.showMaximized()


    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)