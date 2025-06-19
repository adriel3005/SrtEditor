from PyQt5 import QtWidgets, QtCore, QtGui

class LyricGroup(QtWidgets.QWidget):
    def __init__(self, start=QtCore.QTime(0, 0, 0), end=QtCore.QTime(0, 0, 0), lyrics="", count=0, parent=None, on_add=None, on_remove=None):
        super().__init__(parent)

        self.setObjectName("lyricGroup")
        self.setMinimumSize(QtCore.QSize(0, 150))
        self.setMaximumSize(QtCore.QSize(600, 100))
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        layout = QtWidgets.QGridLayout(self)

        fontLabel = QtGui.QFont()
        fontLabel.setPointSize(10)

        fontText = QtGui.QFont()
        fontText.setPointSize(12)

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
        layout.addWidget(self.lyricsText, 0, 2, 2, 1)

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

        # Count label
        self.lyricCountLabel = QtWidgets.QLabel(str(count), self)
        self.lyricCountLabel.setFont(fontText)
        self.lyricCountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.lyricCountLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.lyricCountLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        layout.addWidget(self.lyricCountLabel, 0, 3, 1, 1)

        # Add Button
        self.addButton = QtWidgets.QPushButton("Añadir", self)
        self.addButton.setMinimumSize(QtCore.QSize(100, 30))
        self.addButton.setMaximumSize(QtCore.QSize(100, 16777215))
        layout.addWidget(self.addButton, 2, 0, 1, 1)

        # Connect the add button to the on_add callback if provided
        self.addButton.clicked.connect(lambda: on_add(self) if on_add else None)

        # Remove Button
        self.removeButton = QtWidgets.QPushButton("Eliminar", self)
        self.removeButton.setMinimumSize(QtCore.QSize(100, 30))
        self.removeButton.setMaximumSize(QtCore.QSize(100, 16777215))
        layout.addWidget(self.removeButton, 2, 1, 1, 1)

        # Connect remove button to callback
        self.removeButton.clicked.connect(lambda: on_remove(self) if on_remove else None)

        self.setLayout(layout)
