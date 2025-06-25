from PyQt5 import QtWidgets, QtCore, QtGui

class LyricGroup(QtWidgets.QWidget):
    def __init__(self, start=QtCore.QTime(0, 0, 0), end=QtCore.QTime(0, 0, 0), lyrics="", count=0, parent=None,
                 on_add=None, on_remove=None, on_set_start=None, on_set_end=None):
        super().__init__(parent)

        self.setObjectName("lyricGroup")
        self.setMinimumSize(QtCore.QSize(0, 150))
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)

        layout = QtWidgets.QGridLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(5)

        fontLabel = QtGui.QFont()
        fontLabel.setPointSize(10)

        lyricCountText = QtGui.QFont()
        lyricCountText.setPointSize(10)

        fontText = QtGui.QFont()
        fontText.setPointSize(12)

        # Start label and time
        self.startLabel = QtWidgets.QLabel("Inicio:", self)
        self.startLabel.setFont(fontLabel)
        layout.addWidget(self.startLabel, 0, 0)

        self.startTime = QtWidgets.QTimeEdit(self)
        self.startTime.setDisplayFormat("mm:ss:zzz")
        self.startTime.setFont(fontText)
        self.startTime.setTime(start)
        self.startTime.setMaximumWidth(125)
        layout.addWidget(self.startTime, 0, 1)

        # Lyrics box with overlay label
        lyricsContainer = QtWidgets.QStackedLayout()
        lyricsWidget = QtWidgets.QWidget(self)
        lyricsLayout = QtWidgets.QStackedLayout(lyricsWidget)

        self.lyricsText = QtWidgets.QPlainTextEdit(self)
        self.lyricsText.setFont(fontText)
        self.lyricsText.setPlainText(lyrics)
        lyricsLayout.addWidget(self.lyricsText)

        self.lyricCountLabel = QtWidgets.QLabel(str(count), self.lyricsText)
        self.lyricCountLabel.setFont(lyricCountText)
        self.lyricCountLabel.setStyleSheet("QLabel { background-color: transparent; padding: 2px; }")
        self.lyricCountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.lyricCountLabel.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.lyricCountLabel.move(self.lyricsText.viewport().width() - 20, 1)
        self.lyricCountLabel.raise_()

        self.lyricsText.viewport().installEventFilter(self)

        layout.addWidget(lyricsWidget, 0, 2, 2, 1)

        # End label and time
        self.endLabel = QtWidgets.QLabel("Final:", self)
        self.endLabel.setFont(fontLabel)
        layout.addWidget(self.endLabel, 1, 0)

        self.endTime = QtWidgets.QTimeEdit(self)
        self.endTime.setDisplayFormat("mm:ss:zzz")
        self.endTime.setFont(fontText)
        self.endTime.setTime(end)
        self.endTime.setMaximumWidth(125)
        layout.addWidget(self.endTime, 1, 1)

        # Buttons in a row with equal width
        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.setSpacing(10)

        buttonWidth = 100
        self.addButton = QtWidgets.QPushButton("Añadir", self)
        self.addButton.setMinimumWidth(buttonWidth)
        self.removeButton = QtWidgets.QPushButton("Eliminar", self)
        self.removeButton.setMinimumWidth(buttonWidth)
        self.setStartButton = QtWidgets.QPushButton("⏱ Inicio", self)
        self.setStartButton.setMinimumWidth(buttonWidth)
        self.setEndButton = QtWidgets.QPushButton("⏱ Final", self)
        self.setEndButton.setMinimumWidth(buttonWidth)

        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.removeButton)
        buttonLayout.addWidget(self.setStartButton)
        buttonLayout.addWidget(self.setEndButton)

        layout.addLayout(buttonLayout, 2, 0, 1, 3)

        # Connect callbacks
        self.addButton.clicked.connect(lambda: on_add(self) if on_add else None)
        self.removeButton.clicked.connect(lambda: on_remove(self) if on_remove else None)
        self.setStartButton.clicked.connect(lambda: on_set_start(self) if on_set_start else None)
        self.setEndButton.clicked.connect(lambda: on_set_end(self) if on_set_end else None)

        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if obj == self.lyricsText.viewport() and event.type() == QtCore.QEvent.Resize:
            self.lyricCountLabel.move(self.lyricsText.viewport().width() - 20, 2)
        return super().eventFilter(obj, event)
