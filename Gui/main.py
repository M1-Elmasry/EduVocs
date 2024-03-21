#!/usr/bin/python3
"""
# Working with Qt?
    Import QApplication, QMainWindow, QWidget
    from PySide6.QtWidgets
"""

import ipaddress
from PySide6.QtWidgets import QApplication
from .main_window import MainWindow
from .learning_window import LearningWindow
from ..storage import storage

""" STEP [1]"""
# Creating an instance of QApplication class to use it as an application object
# That application object will be executed later
app = QApplication()

"""STEP [2]"""
# Create an instance of QMainWindow class to be the main application loading_window
if storage.user_exists() is None:
    window = MainWindow()
else:
    window = LearningWindow()

window.show()

# Usage of exec() method to the QApplication instance to execute the event loop
# this loop waits for any event to act with it
app.exec()
