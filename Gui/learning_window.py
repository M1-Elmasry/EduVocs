import sys
from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QScrollArea,
)
from PySide6.QtCore import Qt, QTimer
from .database_record import databaseRecord
from .base_window import BaseWindow
from ..storage import storage


class LearningWindow(BaseWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        menu_items = {
            "Learning Window": self.open_learning_window,
            "Knowing Window": self.open_knowing_window,
        }
        self.content_widget = self.create_content_widget()
        self.side_menu_widget = self.create_side_menu(menu_items, 25)
        self.add_horizontal_widget(self.side_menu_widget)
        self.add_horizontal_widget(self.content_widget)

        if self.parent is not None:
            QTimer.singleShot(500, self.parent.close)

    def open_learning_window(self, event):
        print("Learning Window currently opened")

    def open_knowing_window(self, event):
        from .knowing_window import KnowingWindow

        print("knowing from learning opened")
        knowing_window = KnowingWindow(parent=self)  # Pass parent reference
        knowing_window.show()

    def create_content_widget(self):
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: #15171c;")
        content_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setAlignment(Qt.AlignTop)
        header_layout = self.create_header()
        header_widget = QWidget()
        header_widget.setLayout(header_layout)
        content_layout.addWidget(header_widget)
        content_layout.addWidget(self.create_search_bar())
        content_layout.addWidget(self.create_record_scroll_area())
        return content_widget

    def create_header(self):
        header = QHBoxLayout()
        records_count = len(storage.load_records()["learning"])
        record_counter = QLineEdit(f"{records_count}")
        record_counter.setReadOnly(True)
        record_counter.setAlignment(Qt.AlignCenter)
        record_counter.setStyleSheet(
            "padding: 3px; border: 1px solid #f7f6f7; border-radius: 5px"
        )
        record_counter.setFixedSize(35, 35)
        app_logo = QLabel("eduVocs")
        app_logo.setStyleSheet("font-size: 20px")
        app_logo.setAlignment(Qt.AlignCenter)
        header.addWidget(record_counter)
        header.addWidget(app_logo)
        return header

    def create_search_bar(self):
        search_bar = QLineEdit()
        search_bar.setAlignment(Qt.AlignCenter)
        search_bar.setStyleSheet(
            "margin: 25px 15px; padding: 10px 4px; border: 3px solid #686d75; border-radius: 5px"
        )
        search_bar.setPlaceholderText("Search for something")
        search_bar.textChanged.connect(self.search_records)
        return search_bar

    def create_record_scroll_area(self):
        record_scroll_area = QScrollArea()
        record_scroll_area.setWidgetResizable(True)
        record_scroll_area.setWidget(self.create_record_container())
        return record_scroll_area

    def create_record_container(self):
        record_container = QWidget()
        record_layout = QVBoxLayout(record_container)
        record_layout.setAlignment(Qt.AlignCenter)
        for record in storage.load_records()["learning"][::-1]:
            record_widget = databaseRecord(record[0], record[1])
            record_layout.addWidget(record_widget)
        return record_container

    def search_records(self, text):
        # Implement your search functionality here
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LearningWindow()
    window.show()
    sys.exit(app.exec())
