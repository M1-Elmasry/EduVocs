#!/usr/bin/python3
""" This is for program the next window: as a test firstly """
from PySide6.QtWidgets import (
                            QApplication,
                            QMainWindow,
                            QVBoxLayout,
                            QHBoxLayout,
                            QWidget,
                            QLabel,
                            QLineEdit,
                            QPushButton
                            )
from .center_widget import center
from webbrowser import open
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QSizePolicy, QScrollArea
from .learning_window import LearningWindow
from .knowing_window import KnowingWindow
from .database_record import databaseRecord
from EduVocs.storage import Storage

class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduVocs")
        self.setWindowIcon(QIcon("/home/mahmoud/Desktop/Repos/EduVocs/Gui/assets/EduVocs_icon.png"))
        self.setMinimumSize(1000, 650)
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

        # Create a main horizontal widget to occupy the widgets left and right
        main_layout = QHBoxLayout()
        main_layout.setAlignment(Qt.AlignLeft)

        """ Creating the left widget """
        # Create the left widget [will hold the app name, connect known words window and learned words window]
        left_widget = QWidget()
        # left_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        left_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Adding the left widget to the main layout
        main_layout.addWidget(left_widget)

        # Creating the vertical left layout
        left_layout = QVBoxLayout(left_widget)

        # left_layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        left_layout.setAlignment(Qt.AlignTop)

        # Making the labels to the vertical left layout
        app_name = QLabel("EduVocs")
        app_name.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        app_name.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 35px")

        learning_words = QLabel("Learning words")
        learning_words.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 25px")
        learning_words.setCursor(Qt.PointingHandCursor)
        # learning_words.mousePressEvent = self.open_learning_words


        knowing_words = QLabel("Knowing words")
        knowing_words.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px")
        knowing_words.setCursor(Qt.PointingHandCursor)
        # knowing_words.mousePressEvent = self.open_knowing_words

        learning_words.mousePressEvent = lambda event: self.open_learning_words(event)
        knowing_words.mousePressEvent = lambda event: self.open_knowing_words(event)


        # Adding the labels to the left layout
        left_layout.addWidget(app_name)
        left_layout.addWidget(learning_words)
        left_layout.addWidget(knowing_words)

        # Set fixed width for the left widget
        # left_widget.setFixedWidth(200)
        left_widget.setStyleSheet("background-color: #202229")

        # Set the fixed width for the left widget after the window is shown
        self.showEvent = self.window_shown
        self.left_widget = left_widget

        """ Creating the right widget """
        # Create the right widget [will hold records counter, search bar and records fitched from database]

        right_widget = QWidget()
        right_widget.setStyleSheet("background-color: #15171c;")
        right_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Adding the right widget to the main horizontal layout
        main_layout.addWidget(right_widget)

        # Creating the vertical right layout & connect the right widget in it
        right_layout = QVBoxLayout(right_widget)
        right_layout.setAlignment(Qt.AlignTop)

        # Creating a horizontal layout carring records counter and the app logo
        header = QHBoxLayout()

        # Making the header labels which are the records counter and the app logo
        records_count = 0
        record_counter = QLineEdit(f"{records_count}")
        record_counter.setReadOnly(True)
        record_counter.setAlignment(Qt.AlignCenter)
        record_counter.setStyleSheet("padding: 3px; border: 1px solid #f7f6f7 \
                                    ; border-radius: 5px")
        record_counter.setFixedSize(35, 35)
        app_logo = QLabel("eduVocs")
        app_logo.setStyleSheet("font-size: 20px")
        app_logo.setAlignment(Qt.AlignCenter)


        # Adding the labels to the horizontal header layout
        header.addWidget(record_counter)
        header.addWidget(app_logo)

        # Adding the header layout to the right layout
        right_layout.addLayout(header)

        # Making labels (Later it will be the records counter, search bar and the database records)
        search_bar = QLineEdit()
        search_bar.setAlignment(Qt.AlignCenter)
        search_bar.setStyleSheet("margin: 25px 15px; padding: 10px 4px; \
                                border: 3px solid #686d75; border-radius: 5px")
        search_bar.setPlaceholderText("Search for something")

        # Connect it to textchange signal --> Slot: database searching algorithm
        search_bar.textChanged.connect(self.search_records)
        # Adding the word search bar to the right verticle layout
        right_layout.addWidget(search_bar)


        #######################################################################
        ##################### Start records representation ####################
        #######################################################################

        # Making a verticle layout for records
        # record_layout = QVBoxLayout()
        # record_layout.setAlignment(Qt.AlignCenter)
        # right_layout.addLayout(record_layout)

        # Make a QScrollArea to hold the records
        record_scroll_area = QScrollArea()
        record_scroll_area.setWidgetResizable(True)  # Allow the scroll area to resize its widget
        right_layout.addWidget(record_scroll_area)

        # Create a QWidget to contain the records layout
        record_container = QWidget()
        record_scroll_area.setWidget(record_container)

        # Make a verticle layout to hold the record container
        record_layout = QVBoxLayout(record_container)
        record_layout.setAlignment(Qt.AlignCenter)

        storage = Storage()

        for record in storage.load_records()["learning"]:
            records_count = records_count + 1
            record_widget = databaseRecord(record[0], record[1])
            record_layout.addWidget(record_widget)


        self.right_widget = right_widget
        central_widget.setLayout(main_layout)

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

        # Set to 3 to make it occupy 30% of the window width
        main_layout.setStretchFactor(self.left_widget, 2.5)

        # Set to 7 to make it occupy 70% of the window width
        main_layout.setStretchFactor(self.right_widget, 7.5)

    def search_records(self):
        # Searching algorithm
        # Update the shown results based on the searching text
        pass

    def open_learning_words(self, event):
        learning_window = LearningWindow()
        print("Opening learning words")
        learning_window.show()

    def open_knowing_words(self, event):
        knowing_window = KnowingWindow()
        print("Opening knowing words")
        knowing_window.show()

if __name__ == "__main__":
    app = QApplication()
    window = UserWindow()
    window.show()
    app.exec()