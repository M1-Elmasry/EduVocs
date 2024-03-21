import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QSizePolicy,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from webbrowser import open as web_open
from .center_widget import center


class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduVocs")
        self.setWindowIcon(QIcon("Gui/assets/EduVocs_icon.png"))
        self.setMinimumSize(1000, 650)
        self.create_menu_bar()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignLeft)
        self.central_widget.setLayout(self.main_layout)
        center(self)

    def create_menu_bar(self):
        taskBar = self.menuBar()
        taskBar.setStyleSheet("padding: 5px")

        about = QAction("About", self)
        help = QAction("Help", self)
        readme = QAction("Readme", self)
        quit_action = QAction("Quit", self)

        about.triggered.connect(self.open_about_page)
        help.triggered.connect(self.open_help_page)
        readme.triggered.connect(self.open_readme_page)
        quit_action.triggered.connect(self.quit_the_app)

        taskBar.addAction(about)
        taskBar.addAction(help)
        taskBar.addAction(readme)
        taskBar.addAction(quit_action)

    def create_side_menu(self, menu_items, percentage_width):
        side_menu_layout = QVBoxLayout()
        side_menu_layout.setAlignment(Qt.AlignTop)
        side_menu_widget = QWidget()
        side_menu_widget.setStyleSheet("background-color: #202229")
        side_menu_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        side_menu_widget.setLayout(side_menu_layout)
        side_menu_widget.setFixedWidth(self.width() * percentage_width / 100)

        app_name = QLabel("EduVocs")
        app_name.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        app_name.setStyleSheet(
            "font-size: 20px; font-weight: bold; margin-bottom: 35px"
        )

        side_menu_layout.addWidget(app_name)

        for item_name, event_func in menu_items.items():
            label = QLabel(item_name)
            label.setStyleSheet(
                "font-size: 18px; font-weight: bold; margin-bottom: 25px"
            )
            label.setCursor(Qt.PointingHandCursor)
            label.mousePressEvent = event_func
            side_menu_layout.addWidget(label)

        return side_menu_widget

    def add_horizontal_widget(self, widget):
        self.main_layout.addWidget(widget)

    def open_about_page(self):
        web_open("< About page link here >")

    def open_help_page(self):
        web_open("< help page link here >")

    def open_readme_page(self):
        web_open("< readme page link here >")

    def quit_the_app(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BaseWindow()
    window.show()
    sys.exit(app.exec())
