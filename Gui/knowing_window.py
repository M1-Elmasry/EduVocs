#!/usr/bin/python3
""" This is for program the next window: as a test firstly """
from PySide6.QtWidgets import (
                            QApplication,
                            QMainWindow,
                            QVBoxLayout,
                            QHBoxLayout,
                            QWidget,
                            QLabel,
                            QLineEdit
                            )
from .center_widget import center
from webbrowser import open
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QSizePolicy
from .learning_window import LearningWindow

class KnowingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduVocs")
        self.setWindowIcon(QIcon("assets/EduVocs_icon.png"))
        self.setFixedSize(900, 600)
        self.showEvent = self.window_shown

        # self.setFixedSize(767, 1024)
        center(self)

        """ Making menuBar"""
        taskBar = self.menuBar()
        taskBar.setStyleSheet("padding: 5px")

        # Adding menus
        about = taskBar.addAction("About")
        help = taskBar.addAction("Help")
        readme = taskBar.addAction("Readme")
        quit = taskBar.addAction("Quit")

        about.triggered.connect(self.open_about_page)
        help.triggered.connect(self.open_help_page)
        readme.triggered.connect(self.open_readme_page)
        quit.triggered.connect(self.quit_the_app)

        # Create a main widget to hold the main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)


    def open_about_page(self):
        open("< About page link here >")

    def open_help_page(self):
        open("< help page link here >")

    def open_readme_page(self):
        open("< readme page link here >")

    def quit_the_app(self):
        QApplication.quit()

    def window_shown(self, event):
    # Set the stretch factors for the left and right widgets
        main_layout = self.centralWidget().layout()



