from PySide6.QtWidgets import QWidget, QLabel
from .center_widget import center
from PySide6.QtGui import QMovie, QIcon

# Create loading Label
class Loading(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduVocs Loading")
        self.setWindowIcon(QIcon("assets/EduVocs_icon.png"))
        self.setFixedSize(900, 600)
        self.movie = QMovie("assets/loading.gif")
        self.label = QLabel(self)
        self.label.setMovie(self.movie)
        self.label.setGeometry(380, 100, 400, 400)
        self.movie.start()
        center(self)
