from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton, QStyle, QSlider, QStatusBar
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QDir, Qt, QUrl, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
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
import qdarkstyle
import subprocess


class Main(QMainWindow, Ui_MainWindow):

    lyricList = []
    lyricCount = 0
    videoPath = ""
    videoName = ""
    darkMode = False
    redMode = False
    blueMode = False
    latestStartTime = QtCore.QTime(0, 0, 0)
    latestEndTime = QtCore.QTime(0, 0, 0)

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.removeButton.clicked.connect(self.OnRemove)
        self.addButton.clicked.connect(lambda:self.OnAddButton())
        self.createSRTButton.clicked.connect(self.CreateSRT)
        self.actionOpen_Video.triggered.connect(self.OpenVideoFile)

        #Modes
        self.actionDark_Mode_2.triggered.connect(lambda: self.ToggleDarkMode(self.darkMode))
        self.actionLight_Mode.triggered.connect(self.ToggleLightMode)
        self.actionRed_Palette.triggered.connect(lambda: self.ToggleRedMode(self.redMode))
        self.actionBlue_Palette.triggered.connect(lambda: self.ToggleBlueMode(self.blueMode))

        #Video
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()

        openButton = QPushButton("Abrir Video")
        openButton.setToolTip("Abrir Video")
        openButton.setStatusTip("Abrir Video")
        openButton.setFixedHeight(40)
        openButton.setIconSize(btnSize)
        openButton.setFont(QFont("Noto Sans", 15))
        openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
        openButton.clicked.connect(self.open)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(65)
        self.playButton.setFixedWidth(60)
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
        self.statusBar.showMessage("Listo")

        # connect buttons playback
        self.fiveBack.clicked.connect(lambda: self.TimeSkip(5, False))
        self.tenBack.clicked.connect(lambda: self.TimeSkip(10, False))
        self.oneMBack.clicked.connect(lambda: self.TimeSkip(.1, False))
        self.fiveForward.clicked.connect(lambda: self.TimeSkip(5, True))
        self.tenForward.clicked.connect(lambda: self.TimeSkip(10, True))
        self.oneMForward.clicked.connect(lambda: self.TimeSkip(.1, True))

        #Import srt
        self.actionInportar_Subtitulos_srt.triggered.connect(self.ImportSRT)
    def ToggleLightMode(self):
        light_palette = QPalette()
        appctxt.app.setPalette(light_palette)

    def ToggleRedMode(self, dark):

        if not dark:
            red_palette = QPalette()

            red_palette.setColor(QPalette.Window, QColor(100,53,53))
            red_palette.setColor(QPalette.WindowText, Qt.white)
            red_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            red_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            red_palette.setColor(QPalette.ToolTipBase, Qt.white)
            red_palette.setColor(QPalette.ToolTipText, Qt.white)
            red_palette.setColor(QPalette.Text, Qt.white)
            red_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            red_palette.setColor(QPalette.ButtonText, Qt.white)
            red_palette.setColor(QPalette.BrightText, Qt.red)
            red_palette.setColor(QPalette.Link, QColor(42, 130, 218))
            red_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            red_palette.setColor(QPalette.HighlightedText, Qt.black)

            appctxt.app.setPalette(red_palette)
            #appctxt.app.setStyleSheet(
            #    "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
            self.redMode = True
        else:
            light_palette = QPalette()
            appctxt.app.setPalette(light_palette)
            self.redMode = False

    def ToggleBlueMode(self, dark):

        if not dark:
            blue_palette = QPalette()

            blue_palette.setColor(QPalette.Window, QColor(53,53,100))
            blue_palette.setColor(QPalette.WindowText, Qt.white)
            blue_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            blue_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            blue_palette.setColor(QPalette.ToolTipBase, Qt.white)
            blue_palette.setColor(QPalette.ToolTipText, Qt.white)
            blue_palette.setColor(QPalette.Text, Qt.white)
            blue_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            blue_palette.setColor(QPalette.ButtonText, Qt.white)
            blue_palette.setColor(QPalette.BrightText, Qt.red)
            blue_palette.setColor(QPalette.Link, QColor(42, 130, 218))
            blue_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            blue_palette.setColor(QPalette.HighlightedText, Qt.black)

            appctxt.app.setPalette(blue_palette)
            #appctxt.app.setStyleSheet(
            #    "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
            self.blueMode = True
        else:
            light_palette = QPalette()
            appctxt.app.setPalette(light_palette)
            self.blueMode = False

    def ToggleDarkMode(self, dark):

        if not dark:
            dark_palette = QPalette()

            dark_palette.setColor(QPalette.Window, QColor(53,53,53))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)

            appctxt.app.setPalette(dark_palette)
            #appctxt.app.setStyleSheet(
            #    "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
            self.darkMode = True
        else:
            light_palette = QPalette()
            appctxt.app.setPalette(light_palette)
            self.darkMode = False

    # Currently only supports mp4
    def ImportSRT(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona los mediose", ".",
                                                  "SRT Files (*.srt)")
        videoFilePath = (fileName.split(".")[0]) + ".mp4"
        print(videoFilePath)
        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(videoFilePath)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(videoFilePath)
            self.play()
            self.videoPath = videoFilePath
            self.videoName = self.videoPath.split("/")[-1]

            # Delete existing objects
            count = self.lyricCount
            for i in range(count):
                self.OnRemove()

            # Create video objects
            self.CreateLyricObjectsFromSRT(fileName)

    def CreateLyricObjectsFromSRT(self, path):
        srtFile = open(path, "r", encoding="utf-8")

        # General srt format is
        # index
        # start time --> end time
        # lyrics
        # empty line

        #--- Temp variables
        index = 1
        foundStart = False
        foundEnd = False
        foundLyrics = False
        lyricsString = ""
        subStringTime = "-->"
        startString = ""
        endString = ""
        # iterate through srt file
        for line in srtFile:
            # after times is lyrics
            if foundStart and foundEnd and not foundLyrics:
                # until we find empty
                if line == "\n":
                    foundLyrics = True

                if lyricsString != "":
                    lyricsString = lyricsString + line.strip('\n').rstrip()
                else:
                    lyricsString = line
            # times
            if subStringTime in line:
                startString = line.split(" --> ")[0].rstrip()
                endString = line.split(" --> ")[-1].rstrip()
                if startString != "":
                    foundStart = True
                else:
                    print("No start time for item", index)
                if endString != "":
                    foundEnd = True
                else:
                    print("No end time for item ", index)
            index = index + 1
            if foundLyrics and startString != "" and endString != "":
                #Create lyrics object here

                startQTime = self.ReturnQTimeObject(startString)
                endQtime = self.ReturnQTimeObject(endString)

                self.OnAdd(start = startQTime, end = endQtime, lyrics= lyricsString )
                lyricsString = ""
                foundLyrics = False
                foundStart = False
                foundEnd = False

        srtFile.close()

    def ReturnQTimeObject(self, timeString):
        hours = timeString.split(":")[0]
        minutes = timeString.split(":")[1]
        secondsAndMsec = timeString.split(":")[2]
        seconds = secondsAndMsec.split(",")[0]
        mSeconds = secondsAndMsec.split(",")[1]

        return QtCore.QTime(int(hours), int(minutes), int(seconds), int(mSeconds))


    def TimeSkip(self, amount, forward):
        if forward:
            tempPosition = self.mediaPlayer.position()
            self.setPosition(tempPosition + int(amount * 1000))
        else:
            tempPosition = self.mediaPlayer.position()
            self.setPosition(tempPosition - int(amount * 1000))


    def SetCurrentTimeText(self, millis):
        millis = int(millis)
        seconds = (millis / 1000) % 60
        seconds = int(seconds)
        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)

        sMillis = self.ThreeCharSyntax(str(millis))
        sSeconds = self.TwoCharSyntax(str(seconds))
        sMinutes = self.TwoCharSyntax(str(minutes))

        self.currentTime.setText("Tiempo Actual " + sMinutes + ":" + sSeconds + ":" + sMillis)


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
            self.progressBar.setProperty("value", 0)

    def OnAddButton(self):
        if self.lyricCount > 0:

            endTimeObject = self.lyricList[self.lyricCount-1].findChild(QtWidgets.QTimeEdit, "endTime").time()
            newTime = QtCore.QTime(0, endTimeObject.minute(), endTimeObject.second(), endTimeObject.msec() + 1)
            self.OnAdd(start=newTime, end= newTime)
            self.scrollArea.ensureWidgetVisible(self.lyricGroup)
            max = self.scrollArea.verticalScrollBar().maximum()
            self.scrollArea.verticalScrollBar().setValue(999999)

        else:
            self.OnAdd()
            max = self.scrollArea.verticalScrollBar().maximum()
            self.scrollArea.verticalScrollBar().setValue(max)


    def OnAdd(self, start = QtCore.QTime(0, 0, 0), end = QtCore.QTime(0, 0, 0), lyrics = ""):
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
        self.startLabel.setText("Inicio:")
        self.gridLayout.addWidget(self.startLabel, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lyricsText = QtWidgets.QPlainTextEdit(self.lyricGroup)
        self.lyricsText.setObjectName("lyricsText")
        self.lyricsText.setFont(font)
        self.lyricsText.setPlainText(lyrics)
        self.gridLayout.addWidget(self.lyricsText, 0, 2, 2, 1)
        self.endLabel = QtWidgets.QLabel(self.lyricGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endLabel.setFont(font)
        self.endLabel.setObjectName("endLabel")
        self.endLabel.setText("Final:")
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
        self.endTime.setCurrentSectionIndex(0)
        self.endTime.setTime(end)


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
        self.startTime.setCurrentSection(2)
        self.startTime.setCurrentSectionIndex(2)
        self.startTime.setTime(start)
        self.startTime.setObjectName("startTime")
        self.startTime.setDisplayFormat("mm:ss:zzz")
        #self.startTime.timeChanged.connect(lambda:self.IncreaseTime(self.endTime))

        self.gridLayout.addWidget(self.startTime, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.lyricGroup, 0, QtCore.Qt.AlignTop)

        # add to list
        self.lyricList.append(self.lyricGroup)
        self.lyricCount += 1
        self.progressBar.setProperty("value", 0)


    def IncreaseTime(self, endTime):
        if endTime.time().currentTime() <= self.startTime.time().currentTime():
            startTimeObject =  self.startTime.time()
            newTime = QtCore.QTime(0, startTimeObject.minute(), startTimeObject.second(), startTimeObject.msec())
            endTime.setTime(newTime)


    def CreateSRT(self):
        # For progress bar
        self.progressCount = 1

        itemSelected = self.textAppendList.currentText()

        # Check to see if file has been open
        if self.videoPath:

            self.newVideoPath = self.videoPath.split(".")[0]+ " - NoTranslation" + ".srt"
            srtFile = open(self.newVideoPath, "w", encoding="utf-8")

            if self.translateEnglish.isChecked() and self.translateSpanish.isChecked():
                self.newVideoPath = self.videoPath.split(".")[0] + ".srt"
                srtFile = open(self.newVideoPath, "w", encoding="utf-8")
            elif self.translateEnglish.isChecked():
                self.newVideoPath = self.videoPath.split(".")[0] + " - English" + ".srt"
                srtFile = open(self.newVideoPath, "w", encoding="utf-8")
            elif self.translateSpanish.isChecked():
                self.newVideoPath = self.videoPath.split(".")[0] + " - Spanish" + ".srt"
                srtFile = open(self.newVideoPath, "w", encoding="utf-8")

            for i in range(len(self.lyricList)):
                # lyrics
                childLyricsText = self.lyricList[i].findChild(QtWidgets.QPlainTextEdit, "lyricsText")

                # start Time
                ## Format: hh:mm:ss:zzz
                childStartTime = self.lyricList[i].findChild(QtWidgets.QTimeEdit, "startTime").time()

                # end Time
                childEndTime = self.lyricList[i].findChild(QtWidgets.QTimeEdit, "endTime").time()

                #print("Start time : " + str(childStartTime.minute()) + str(childStartTime.second()) + str(
                #    childStartTime.msec()))

                # Number of iteration
                srtFile.write(str(self.progressCount) + "\n")

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
                    srtFile.write("\n" + result.rstrip().replace("\n", " ") + "\n")
                    result = self.translator.translate(childLyricsText.toPlainText(), lang_tgt='es')
                    srtFile.write(itemSelected + result.rstrip().replace("\n", " ") + itemSelected + "\n\n")
                elif self.translateEnglish.isChecked():
                    result = self.translator.translate(childLyricsText.toPlainText(), lang_tgt='en')
                    srtFile.write("\n" + result.rstrip().replace("\n", " ") + "\n\n")
                elif self.translateSpanish.isChecked():
                    result = self.translator.translate(childLyricsText.toPlainText(), lang_tgt='es')
                    srtFile.write("\n" + itemSelected + result.rstrip().replace("\n", " ") + itemSelected + "\n\n")
                else:
                    srtFile.write("\n" + childLyricsText.toPlainText().replace("\n", " ") + "\n\n")
                progress = self.progressCount / self.lyricCount
                print(int(progress*100))
                self.progressBar.setProperty("value", int(progress*100))
                self.progressCount += 1

                if progress == 1:
                    print(self.newVideoPath)
                    openPath = self.newVideoPath.replace('/', '\\')
                    subprocess.Popen(r'explorer /select,"'+openPath+'"')

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

        showingLyrics = False
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
                showingLyrics = True
        if showingLyrics == False:
            self.currentLyrics.setText("")

    def ShowPopUpMessage(self):
        errorMsg = QMessageBox()
        errorMsg.setWindowTitle("Error")
        errorMsg.setText("Por favor selecciona un video primero")
        x = errorMsg.exec_()

class WheelEventFilter(QtCore.QObject):
    def eventFilter(self, obj, ev):
        if obj.inherits("QTimeEdit") and ev.type() == QtCore.QEvent.Wheel:
            return True
        return False


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    #app = QApplication(sys.argv)
    window = Main()

    appctxt.app.setStyle("Fusion")

    app = QtWidgets.QApplication.instance()
    filter = WheelEventFilter()
    app.installEventFilter(filter)

    # dark_palette = QPalette()
    #
    # dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    # dark_palette.setColor(QPalette.WindowText, Qt.white)
    # dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    # dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    # dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    # dark_palette.setColor(QPalette.Text, Qt.white)
    # dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # dark_palette.setColor(QPalette.ButtonText, Qt.white)
    # dark_palette.setColor(QPalette.BrightText, Qt.red)
    # dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    #
    # appctxt.app.setPalette(dark_palette)
    # appctxt.app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    #appctxt.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #window.resize(250, 150)
    #window.show()
    window.showMaximized()


    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)