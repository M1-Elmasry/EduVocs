#!/usr/bin/python3

from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QFrame,
    QApplication
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSizePolicy, QSpacerItem
from .. import storage

class databaseRecord(QWidget):
    def __init__(self, word_rec, trans_rec):
        super().__init__()
        self.word_rec = word_rec
        self.trans_rec = trans_rec
        self.storage_obj = storage.Storage()

        # Creating frame to hold the record charastaristics
        frame = QFrame()
        frame_layout = QHBoxLayout(frame)
        # frame_layout.setSpacing(20)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        record_word = QLabel(f"{word_rec}")
        translate_word = QLabel(f"{trans_rec}")
        delete_record = QPushButton("Delete")
        edit_record = QPushButton("Edit")
        add_to_knowing = QPushButton("Know")
        read_button = QPushButton("Read")

        # Style Sheets
        button_stylesheet = """
        QPushButton {
            background-color: #00838F;
            color: #F0F8FF;
            width: 60px;
            padding: 10px;
        }
        """
        delete_button_stylesheet = """
        QPushButton {
            background-color: #800E01;
            color: #F0F8FF;
            width: 60px;
            padding: 10px;
        }
        """

        record_styesheet = """
            color: #F0F8FF;
            font-size: 16px;
            border: none;
            width: fit-content;
        """

        frame.setStyleSheet("""
            QFrame {
                border: 2px solid #686d75;
                border-radius: 50px;
                padding: 5px 20px;
                min-width: 100%;
            }
        """)

        read_button.setStyleSheet(button_stylesheet)
        add_to_knowing.setStyleSheet(button_stylesheet)
        delete_record.setStyleSheet(delete_button_stylesheet)
        edit_record.setStyleSheet(button_stylesheet)

        # Setting actions when clicking the bottoms
        read_button.clicked.connect(self.read_action)
        add_to_knowing.clicked.connect(self.add_to_knowing_buttom)
        delete_record.clicked.connect(self.delete_record_buttom)
        edit_record.clicked.connect(self.edit_record_buttom)

        # Creating Horizontal layout to hold buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)
        buttons_layout.addWidget(delete_record)
        buttons_layout.addWidget(edit_record)
        buttons_layout.addWidget(read_button)
        buttons_layout.addWidget(add_to_knowing)


        # Adding the widgets and buttons layout to the frame
        spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        frame_layout.addWidget(record_word)
        frame_layout.addItem(spacer)
        frame_layout.addWidget(translate_word)
        frame_layout.addItem(spacer)
        frame_layout.addLayout(buttons_layout)
        

        record_word.setStyleSheet(record_styesheet)
        translate_word.setStyleSheet(record_styesheet)

        database_records = QHBoxLayout(self)
        database_records.addWidget(frame)

        database_records.setAlignment(Qt.AlignCenter)

    def read_action(self):
        print("Added to learning")

    def add_to_knowing_buttom(self):
        # storage.flip_record(self.word_rec)
        print("Added to knowing")

    def delete_record_buttom(self):
        self.storage_obj.delete_record(self.word_rec)
        print("Deleted")

    def edit_record_buttom(self):
        print("Edit")


if __name__ == "__main__":
    app = QApplication()
    window = databaseRecord("Hello", "مرحبا")
    window.show()
    app.exec()