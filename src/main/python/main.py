from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton, QStyle, QSlider, QStatusBar
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QDir, Qt, QUrl, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
# from SRT_GUI_Skeleton import Ui_MainWindow
from LyricGroup import LyricGroup
from test_gui_screen2item import Ui_MainWindow
# from test_gui_screen1itempromotedlyrics import Ui_MainWindow
# import from below allows the OnAdd function to work
from PyQt5 import QtCore, QtGui, QtWidgets
from google_trans_new import google_translator

import sip
import sys
import qdarkstyle
import subprocess
import whisper
from datetime import timedelta


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
        self.addButton.clicked.connect(lambda: self.OnAddButton())
        self.createSRTButton.clicked.connect(self.CreateSRT)
        self.actionOpen_Video.triggered.connect(self.OpenVideoFile)

        # Modes
        # self.actionDark_Mode_2.triggered.connect(lambda: self.ToggleDarkMode(self.darkMode))
        # self.actionLight_Mode.triggered.connect(self.ToggleLightMode)
        # self.actionRed_Palette.triggered.connect(lambda: self.ToggleRedMode(self.redMode))
        # self.actionBlue_Palette.triggered.connect(lambda: self.ToggleBlueMode(self.blueMode))

        # Video
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

        # self.QVideoBoxVLayout = QVBoxLayout()
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

        # Import srt
        self.actionInportar_Subtitulos_srt.triggered.connect(self.ImportSRT)
        # Auto Generate Subtitles
        self.actionAuto_Generar_Subtitulos.triggered.connect(self.GenerateSRT)
        # Displace times
        self.actionDesplazar_todos_los_tiempos.triggered.connect(self.OnShiftTimesClicked)

    def ShiftAllTimestamps(self, milliseconds):
        for group in self.lyricList:
            start = group.startTime.time()
            end = group.endTime.time()

            new_start = self._shift_time(start, milliseconds)
            new_end = self._shift_time(end, milliseconds)

            group.startTime.setTime(new_start)
            group.endTime.setTime(new_end)

    def _shift_time(self, qtime, delta_ms):
        total_ms = (
                qtime.hour() * 3600000 +
                qtime.minute() * 60000 +
                qtime.second() * 1000 +
                qtime.msec() +
                delta_ms
        )
        # Clamp at 0
        if total_ms < 0:
            total_ms = 0

        hours = (total_ms // 3600000) % 24
        minutes = (total_ms // 60000) % 60
        seconds = (total_ms // 1000) % 60
        ms = total_ms % 1000

        return QtCore.QTime(hours, minutes, seconds, ms)

    def OnShiftTimesClicked(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Desplazar todos los tiempos")

        layout = QtWidgets.QVBoxLayout(dialog)

        label = QtWidgets.QLabel("¿Cuánto tiempo quieres desplazar?", dialog)
        layout.addWidget(label)

        time_edit = QtWidgets.QTimeEdit(QtCore.QTime(0, 0, 0), dialog)
        time_edit.setDisplayFormat("mm:ss:zzz")
        layout.addWidget(time_edit)

        direction_combo = QtWidgets.QComboBox(dialog)
        direction_combo.addItems(["Adelantar (hacia adelante)", "Retrasar (hacia atrás)"])
        layout.addWidget(direction_combo)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            time = time_edit.time()
            delta_ms = (
                    time.minute() * 60000 +
                    time.second() * 1000 +
                    time.msec()
            )
            if direction_combo.currentIndex() == 1:  # "Retrasar"
                delta_ms *= -1

            self.ShiftAllTimestamps(delta_ms)

    def GenerateSRT(self):
        model = whisper.load_model("turbo")
        result = model.transcribe(self.videoPath)
        print(result["text"])
        # startQTime = self.ReturnQTimeObject(startString)
        # endQtime = self.ReturnQTimeObject(endString)
        # self.OnAdd(start=startQTime, end=endQtime, lyrics=lyricsString)
        if len(result["segments"]) > 0:
            self.RemoveAll()
            for segment in result["segments"]:
                startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
                endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
                text = segment['text']
                segmentId = segment['id'] + 1
                segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
                startQTime = self.ReturnQTimeObject(startTime)
                endQTime = self.ReturnQTimeObject(endTime)
                self.OnAdd(start=startQTime, end=endQTime, lyrics=text[1:] if text[0] is ' ' else text)
                # srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
                # with open(srtFilename, 'a', encoding='utf-8') as srtFile:
                #    srtFile.write(segment)

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
            #count = self.lyricCount
            # TODO: double check if lyricList is and skip on remove if so
            #       since we are now using lyricList.count instead of lyricCount we need to check if accurate.
            for i in range(len(self.lyricList) - 1):
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

        # --- Temp variables
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
                # Create lyrics object here

                startQTime = self.ReturnQTimeObject(startString)
                endQtime = self.ReturnQTimeObject(endString)

                # TODO: test this still works after changes
                lyricBoxToAdd = self.OnAdd(start=startQTime, end=endQtime, lyrics=lyricsString)
                self.AddToList(lyricGroup=lyricBoxToAdd)

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
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona los mediose", ".",
                                                  "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()
            self.videoPath = fileName
            self.videoName = self.videoPath.split("/")[-1]

    def OpenVideoFile(self):
        # self.videoPath, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.videoPath, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video File (*.mp4 *.avi *.ogv)",
                                                        options=options)
        self.videoName = self.videoPath.split("/")[-1]

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.SetCurrentTimeText(self.mediaPlayer.position())
            self.SetCurrentLyrics(self.mediaPlayer.position())  # Still passes int (ms)
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

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

    def RemoveAll(self):
        if len(self.lyricList) > 0:
            while len(self.lyricList) > 0:
                self.verticalLayout.removeWidget(self.lyricList[-1])
                sip.delete(self.lyricList[-1])
                self.lyricCount -= 1
                del (self.lyricList[-1])
                self.progressBar.setProperty("value", 0)

    def OnRemove(self):
        if len(self.lyricList) > 0:
            self.verticalLayout.removeWidget(self.lyricList[-1])
            sip.delete(self.lyricList[-1])
            self.lyricCount -= 1
            del (self.lyricList[-1])
            self.progressBar.setProperty("value", 0)

    def OnAddButton(self):
        if self.lyricList:
            lastLyric = self.lyricList[-1]
            endTime = lastLyric.endTime.time()
            newTime = QtCore.QTime(0, endTime.minute(), endTime.second(), endTime.msec() + 1)
            lyricBoxToAdd = self.OnAdd(start=newTime, end=newTime)
        else:
            lyricBoxToAdd = self.OnAdd()

        self.AddToList(lyricGroup=lyricBoxToAdd)
        self.scrollArea.ensureWidgetVisible(lyricBoxToAdd)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def OnAdd(self, start=QtCore.QTime(0, 0, 0), end=QtCore.QTime(0, 0, 0), lyrics=""):
        group = LyricGroup(
            start=start,
            end=end,
            lyrics=lyrics,
            count=self.lyricCount,
            parent=self.scrollAreaWidgetContents,
            on_add=self.OnAddAfter,
            on_remove=self.OnRemove,
            on_set_start=self.SetStartToCurrentTime,
            on_set_end=self.SetEndToCurrentTime,
        )
        group.setProperty("position", len(self.lyricList))
        return group

    def OnRemove(self, groupToRemove):
        if groupToRemove in self.lyricList:
            index = self.lyricList.index(groupToRemove)
            self.lyricList.pop(index)

            self.verticalLayout.removeWidget(groupToRemove)
            groupToRemove.setParent(None)  # Remove it from UI
            groupToRemove.deleteLater()  # Clean up

            # Update positions and labels
            for i, group in enumerate(self.lyricList):
                group.setProperty("position", i)
                group.lyricCountLabel.setText(str(i + 1))

            self.lyricCount -= 1

    def OnAddAfter(self, after_group):
        try:
            index = self.lyricList.index(after_group)
        except ValueError:
            index = len(self.lyricList) - 1  # fallback: append to end

        endTime = after_group.endTime.time()
        newTime = QtCore.QTime(0, endTime.minute(), endTime.second(), endTime.msec() + 1)

        newGroup = self.OnAdd(start=newTime, end=newTime)
        self.AddToList(lyricGroup=newGroup, positionParam=index + 1)

        self.scrollArea.ensureWidgetVisible(newGroup)

    def AddToList(self, lyricGroup, positionParam=None):
        position = positionParam if positionParam is not None else len(self.lyricList)

        self.lyricList.insert(position, lyricGroup)
        self.verticalLayout.insertWidget(position, lyricGroup, 0, QtCore.Qt.AlignTop)

        for i, group in enumerate(self.lyricList):
            group.setProperty("position", i)
            group.lyricCountLabel.setText(str(i + 1))

        self.lyricCount += 1

    def IncreaseTime(self, endTime):
        if endTime.time().currentTime() <= self.startTime.time().currentTime():
            startTimeObject = self.startTime.time()
            newTime = QtCore.QTime(0, startTimeObject.minute(), startTimeObject.second(), startTimeObject.msec())
            endTime.setTime(newTime)

    def SetStartToCurrentTime(self, group):
        current_ms = self.mediaPlayer.position()
        current_time = QtCore.QTime(0, 0, 0).addMSecs(current_ms)
        group.startTime.setTime(current_time)

    def SetEndToCurrentTime(self, group):
        current_ms = self.mediaPlayer.position()
        current_time = QtCore.QTime(0, 0, 0).addMSecs(current_ms)
        group.endTime.setTime(current_time)

    def _format_qtime(self, qtime):
        """
        Convert QTime to SRT timestamp format: hh:mm:ss,SSS
        Example: 00:01:23,456
        """
        return qtime.toString("hh:mm:ss,zzz").replace(".", ",")

    def CreateSRT(self):
        if not self.lyricList:
            QtWidgets.QMessageBox.warning(self, "Error", "No hay entradas de letras para exportar.")
            return

        srt_lines = []
        selected_emoji = self.textAppendList.currentText().strip()

        for i, group in enumerate(self.lyricList):
            start = group.startTime.time()
            end = group.endTime.time()
            text = group.lyricsText.toPlainText().strip()

            if not text:
                continue  # Skip empty entries

            # Add emoji at start and end if selected
            if selected_emoji:
                text = f"{selected_emoji} {text} {selected_emoji}"

            srt_lines.append(f"{i + 1}")
            srt_lines.append(f"{self._format_qtime(start)} --> {self._format_qtime(end)}")
            srt_lines.append(text)
            srt_lines.append("")  # Blank line between entries

        # Ask user where to save
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Guardar archivo SRT", "", "SubRip Files (*.srt)"
        )

        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(srt_lines))

            QtWidgets.QMessageBox.information(self, "Éxito", f"Archivo guardado:\n{file_path}")

    # check if string is only 1 character
    def TwoCharSyntax(self, str):
        if len(str) != 2:
            return "0" + str
        else:
            return str

    # Make into 3 char
    def ThreeCharSyntax(self, str):
        if len(str) == 1:
            return "00" + str
        elif len(str) == 2:
            return "0" + str
        elif len(str) >= 4:
            return str[-3:]
        else:
            return str

    def SetCurrentLyrics(self, current_position_ms):
        # Convert milliseconds to QTime
        current_time = QtCore.QTime(0, 0, 0).addMSecs(current_position_ms)

        found_lyric = False
        for lyric_group in self.lyricList:
            start_time = lyric_group.startTime.time()
            end_time = lyric_group.endTime.time()

            # Now all three are QTime objects
            if start_time <= current_time <= end_time:
                self.currentLyrics.setText(lyric_group.lyricsText.toPlainText())
                found_lyric = True
                break

        if not found_lyric:
            self.currentLyrics.setText("")  # Clear lyrics if no match

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
    app = QApplication(sys.argv)
    window = Main()

    #appctxt.app.setStyle("Fusion")

    app = QtWidgets.QApplication.instance()
    filter = WheelEventFilter()
    app.installEventFilter(filter)

    app.setWindowIcon(QIcon("srt_app_icon_multi_res.ico"))

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

    # appctxt.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # window.resize(250, 150)
    # window.show()
    window.showMaximized()

    sys.exit(app.exec_())
