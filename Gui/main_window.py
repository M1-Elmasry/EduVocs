#!/usr/bin/python3

from PySide6.QtWidgets import (
                        QWidget,
                        QMainWindow,
                        QLabel,
                        QLineEdit,
                        QPushButton,
                        QComboBox,
                        QTextEdit,
                        QApplication,
                        QVBoxLayout,
                        QHBoxLayout
                            )
from .user_window import UserWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from .center_widget import center
from .knowing_window import KnowingWindow
# Insure about he email format
from re import match


# Creating Main_Window_Class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QWidget())
        # Big screens
        self.setMinimumSize(900, 600)
        self.setWindowTitle("EduVocs")
        self.setWindowIcon(QIcon("/home/mahmoud/Desktop/Repos/EduVocs/Gui/assets/EduVocs_icon.png"))
        
        center(self)
        if self.size().width() <= 767:
            # Create a main widjet to hold the main layout
            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            # Create a main verticle widget to hold all widgets from top to bottom
            main_layout = QVBoxLayout()
            main_layout.setAlignment(Qt.AlignTop)
            main_layout.setSpacing(50)

            # Create the welcome landing statments
            welcome_header = self.welcome_header()
            welcome_landing = self.welcome_landing()

            # Adding welcome landing statments to header layout
            main_layout.addWidget(welcome_header)
            main_layout.addWidget(welcome_landing)

            # Make a horizontal layout to hold username and email containers
            info_layout = QVBoxLayout()
            info_layout.setAlignment(Qt.AlignHCenter)

            user_name = self.UserName()
            user_email = self.UserEmail()

            info_layout.addWidget(user_name)
            info_layout.addWidget(user_email)

            main_layout.addLayout(info_layout)

            # Make a horizontal layout to hold native and target languages
            lang_layout = QVBoxLayout()
            lang_layout.setAlignment(Qt.AlignHCenter)

            native_lang = self.NativeLang()
            target_lang = self.TargetLang()

            lang_layout.addWidget(native_lang)
            lang_layout.addWidget(target_lang)

            main_layout.addLayout(lang_layout)


            # Adding the Done button
            button_layout = QVBoxLayout()
            done = self.done_button()
            button_layout.addWidget(done)
            button_layout.setAlignment(Qt.AlignHCenter)
            main_layout.addLayout(button_layout)

            # Adding alert widgets to the main layout
            alert_label = self.alert_element()
            main_layout.addWidget(alert_label)

            alert_box_layout = QVBoxLayout()
            alert_box_layout.setAlignment(Qt.AlignHCenter)
            alert_box = self.alert_box()
            alert_box_layout.addWidget(alert_box)


            main_layout.addLayout(alert_box_layout)


            self.welcome_header = welcome_header
            self.welcome_landing = welcome_landing
            self.info_layout = info_layout
            self.lang_layout = lang_layout
            self.done = done
            self.alert_label = alert_label
            self.alert_box = alert_box
            self.showEvent = self.window_shown

            central_widget.setLayout(main_layout)

        else:
            # Create a main widjet to hold the main layout
            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            # Create a main verticle widget to hold all widgets from top to bottom
            main_layout = QVBoxLayout()
            main_layout.setAlignment(Qt.AlignTop)
            main_layout.setSpacing(40)

            # Create the welcome landing statments
            welcome_header = self.welcome_header()
            welcome_landing = self.welcome_landing()

            # Adding welcome landing statments to header layout
            main_layout.addWidget(welcome_header)
            main_layout.addWidget(welcome_landing)

            # Make a horizontal layout to hold username and email containers
            info_layout = QHBoxLayout()
            info_layout.setAlignment(Qt.AlignHCenter)

            user_name = self.UserName()
            user_email = self.UserEmail()

            info_layout.addWidget(user_name)
            info_layout.addSpacing(100)
            info_layout.addWidget(user_email)

            main_layout.addLayout(info_layout)

            # Make a horizontal layout to hold native and target languages
            lang_layout = QHBoxLayout()
            lang_layout.setAlignment(Qt.AlignHCenter)

            native_lang = self.NativeLang()
            target_lang = self.TargetLang()

            lang_layout.addWidget(native_lang)
            lang_layout.setSpacing(148)
            lang_layout.addWidget(target_lang)

            main_layout.addLayout(lang_layout)


            # Adding the Done button
            button_layout = QHBoxLayout()
            done = self.done_button()
            button_layout.addWidget(done)
            main_layout.addLayout(button_layout)

            # Adding alert widgets to the main layout
            alert_label = self.alert_element()
            main_layout.addWidget(alert_label)

            alert_box_layout = QHBoxLayout()
            alert_box = self.alert_box()
            alert_box_layout.addWidget(alert_box)


            main_layout.addLayout(alert_box_layout)


            self.welcome_header = welcome_header
            self.welcome_landing = welcome_landing
            self.info_layout = info_layout
            self.lang_layout = lang_layout
            self.done = done
            self.alert_label = alert_label
            self.alert_box = alert_box
            self.showEvent = self.window_shown

            central_widget.setLayout(main_layout)



    def welcome_header(self):
        # Make a welcome message for the user at application intrance
        heading = QLabel("Welcome")
        heading.setAlignment(Qt.AlignHCenter)
        heading.setStyleSheet("font-size: 40px; margin-top: 40px")
        return (heading)

    def welcome_landing(self):
        WelcomeMessage = QLabel("Welcome to EduVocs, Where Language mestery meets innovation")
        WelcomeMessage.setAlignment(Qt.AlignHCenter)
        WelcomeMessage.setStyleSheet("font-size: 20px")
        WelcomeMessage.setContentsMargins(0, 0, 0, 0)
        return(WelcomeMessage)


    # Input the name of the user
    def UserName(self):
        self.user_name = QLineEdit(self)
        self.user_name.setPlaceholderText("Your name")
        self.user_name.setAlignment(Qt.AlignCenter)  # Align placeholder text to center
        self.user_name.setFixedSize(300, 40)
        self.user_name.setFocusPolicy(Qt.ClickFocus)
        return (self.user_name)

    # Input the email of the user
    def UserEmail(self):
        self.user_email = QLineEdit(self)
        self.user_email.setAlignment(Qt.AlignCenter)  # Align placeholder text to center
        self.user_email.setFixedSize(300, 40)
        self.user_email.setPlaceholderText("Your email")
        self.user_email.setFocusPolicy(Qt.ClickFocus)
        return (self.user_email)

    # Create a native language selection box
    def NativeLang(self):
        self.native_language = QComboBox(self)
        self.native_language.setFixedSize(300, 40)
        # Add items to the combo box
        self.native_language.addItem("Your Native Language")
        self.native_language.addItem("Arabic")
        self.native_language.addItem("English")
        self.native_language.addItem("French")
        self.native_language.addItem("German")
        self.native_language.setCurrentIndex(0)

        return (self.native_language)

    # Create a target language selection box
    def TargetLang(self):
        self.target_language = QComboBox(self)
        self.target_language.setFixedSize(300, 40)

        # Add items to the combo box
        self.target_language.addItem("Your Target Language")
        self.target_language.addItem("Arabic")
        self.target_language.addItem("English")
        self.target_language.addItem("French")
        self.target_language.addItem("German")
        self.target_language.setCurrentIndex(0)
        return (self.target_language)

    def alert_element(self):
        self.message_box_label = QLabel("Alerts:", self)
        self.message_box_label.setAlignment(Qt.AlignHCenter)
        return(self.message_box_label)

    def alert_box(self):
        self.message_box = QTextEdit(self)
        self.message_box.setReadOnly(True)
        self.message_box.setFixedWidth(600)
        self.message_box.setStyleSheet("margin-bottom: 50px")
        self.message_box.setAlignment(Qt.AlignCenter)  # Align text to center
        return(self.message_box)

    def done_button(self):
        # Make the done buttom
        self.button = QPushButton("Done", self)
        self.button.setStyleSheet("font-size: 15px;")
        self.button.setFixedSize(150, 50)
        self.button.setFocus()
        """ When the Done buttom clicked, it will turn to the translation screen """
        self.button.clicked.connect(self.click_done_button)
        return (self.button)

    def click_done_button(self):
        user_name = self.user_name.text()
        user_email = self.user_email.text()
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        name_pattern = r'^[a-zA-Z]+$'

        if not match(name_pattern, user_name):
            self.message_box.setText("Invalid name. Please enter a valid name.")

        elif not match(email_pattern, user_email):
            self.message_box.setText("Invalid email format. Please enter a valid email.")

        elif self.native_language.currentIndex() == 0:
            self.message_box.setText("Please choose your native language")

        elif self.target_language.currentIndex() == 0:
            self.message_box.setText("Please choose your target language")

        else:
            self.message_box.setText("everything is good")
            new_window = UserWindow()
            self.hide()
            new_window.show()


    def window_shown(self, event):
    # Set the stretch factors for the left and right widgets
        main_layout = self.centralWidget().layout()

        main_layout.setStretchFactor(self.welcome_header, 1)
        main_layout.setStretchFactor(self.welcome_landing, 1)
        main_layout.setStretchFactor(self.info_layout, 4)
        main_layout.setStretchFactor(self.lang_layout, 3)
        main_layout.setStretchFactor(self.done, 2)
        # main_layout.setStretchFactor(self.alert_label, 1)
        main_layout.setStretchFactor(self.alert_box, 4)
