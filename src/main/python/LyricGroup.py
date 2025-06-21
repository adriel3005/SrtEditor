from PyQt5 import QtWidgets, QtCore, QtGui

class LyricGroup(QtWidgets.QWidget):
    def __init__(self, start=QtCore.QTime(0, 0, 0), end=QtCore.QTime(0, 0, 0), lyrics="", count=0, parent=None, on_add=None, on_remove=None, on_set_start=None, on_set_end=None):
        super().__init__(parent)

        self.setObjectName("lyricGroup")
        self.setMinimumSize(QtCore.QSize(0, 150))
        ##self.setMaximumSize(QtCore.QSize(600, 100))
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)


        layout = QtWidgets.QGridLayout(self)

        fontLabel = QtGui.QFont()
        fontLabel.setPointSize(10)

        fontText = QtGui.QFont()
        fontText.setPointSize(12)

        button_width = 100  # or whatever looks good

        # Start Label
        self.startLabel = QtWidgets.QLabel("Inicio:", self)
        self.startLabel.setFont(fontLabel)
        layout.addWidget(self.startLabel, 0, 0, 1, 1)

        # Start Time
        self.startTime = QtWidgets.QTimeEdit(self)
        self.startTime.setDisplayFormat("mm:ss:zzz")
        self.startTime.setFont(fontText)
        self.startTime.setMinimumSize(QtCore.QSize(100, 30))
        self.startTime.setMaximumSize(QtCore.QSize(75, 16777215))
        self.startTime.setTime(start)
        layout.addWidget(self.startTime, 0, 1, 1, 1)

        # Lyrics Text
        self.lyricsText = QtWidgets.QPlainTextEdit(self)
        self.lyricsText.setFont(fontText)
        self.lyricsText.setPlainText(lyrics)
        layout.addWidget(self.lyricsText, 0, 2, 2, 2)  # Span 2 columns to reclaim space

        # End Label
        self.endLabel = QtWidgets.QLabel("Final:", self)
        self.endLabel.setFont(fontLabel)
        layout.addWidget(self.endLabel, 1, 0, 1, 1)

        # End Time
        self.endTime = QtWidgets.QTimeEdit(self)
        self.endTime.setDisplayFormat("mm:ss:zzz")
        self.endTime.setFont(fontText)
        self.endTime.setMinimumSize(QtCore.QSize(100, 30))
        self.endTime.setMaximumSize(QtCore.QSize(75, 16777215))
        self.endTime.setTime(end)
        layout.addWidget(self.endTime, 1, 1, 1, 1)

        # Count label positioned *inside* lyricsText
        self.lyricCountLabel = QtWidgets.QLabel(str(count), self.lyricsText)
        countFont = QtGui.QFont()
        countFont.setPointSize(9)
        self.lyricCountLabel.setFont(countFont)
        self.lyricCountLabel.setStyleSheet("background-color: transparent; color: gray;")
        self.lyricCountLabel.setFixedSize(20, 15)
        self.lyricCountLabel.move(self.lyricsText.width() - 25, 5)
        self.lyricCountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.lyricCountLabel.raise_()

        # Update position if resized
        self.lyricsText.resizeEvent = lambda event: self.lyricCountLabel.move(self.lyricsText.width() - 25, 5)

        # Add Button
        self.addButton = QtWidgets.QPushButton("Añadir", self)
        self.addButton.setMinimumSize(QtCore.QSize(100, 30))
        #self.addButton.setMaximumSize(QtCore.QSize(100, 16777215))
        #self.addButton.setFixedWidth(button_width)

        layout.addWidget(self.addButton, 2, 0, 1, 1)

        # Connect the add button to the on_add callback if provided
        self.addButton.clicked.connect(lambda: on_add(self) if on_add else None)

        # Remove Button
        self.removeButton = QtWidgets.QPushButton("Eliminar", self)
        self.removeButton.setMinimumSize(QtCore.QSize(100, 30))
        #self.removeButton.setMaximumSize(QtCore.QSize(100, 16777215))
        #self.removeButton.setFixedWidth(button_width)
        layout.addWidget(self.removeButton, 2, 1, 1, 1)

        # Connect remove button to callback
        self.removeButton.clicked.connect(lambda: on_remove(self) if on_remove else None)

        # Set Start Time button
        self.setStartButton = QtWidgets.QPushButton("⏱ Inicio", self)
        self.setStartButton.setMinimumSize(QtCore.QSize(100, 30))
        self.setStartButton.clicked.connect(lambda: self.on_set_start(self) if self.on_set_start else None)
        #self.setStartButton.setFixedWidth(button_width)
        layout.addWidget(self.setStartButton, 2, 2, 1, 1)

        # Set End Time button
        self.setEndButton = QtWidgets.QPushButton("⏱ Final", self)
        self.setEndButton.setMinimumSize(QtCore.QSize(100, 30))
        self.setEndButton.clicked.connect(lambda: self.on_set_end(self) if self.on_set_end else None)
        #self.setEndButton.setFixedWidth(button_width)
        layout.addWidget(self.setEndButton, 2, 3, 1, 1)

        self.on_set_start = on_set_start
        self.on_set_end = on_set_end

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        self.setLayout(layout)
