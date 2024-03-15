#!/usr/bin/python3
"""
# Working with Qt?
    Import QApplication, QMainWindow, QWidget
    from PySide6.QtWidgets
"""

from PySide6.QtWidgets import QApplication
from .main_window import MainWindow
from .loading_window import Loading
from PySide6.QtCore import QTimer

""" STEP [1]"""
# Creating an instance of QApplication class to use it as an application object
# That application object will be executed later
app = QApplication()

"""STEP [2]"""
# Create an instance of QMainWindow class to be the main application window
window = MainWindow()
loading = Loading()

# Show the loading widget
loading.show()

# Hide the loading widget and show the main window content after 5 seconds
QTimer.singleShot(3000, loading.hide)
QTimer.singleShot(3000, window.show)
# Usage of exec() method to the QApplication instance to execute the event loop
# this loop waits for any event to act with it

app.exec()