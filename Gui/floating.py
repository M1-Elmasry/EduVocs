#!/usr/bin/python3

from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QApplication,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt

class FloatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hovered = False
        self.label = QLabel("Click me", self)
        self.text_area = QTextEdit(self)
        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet("padding: 15px")
        self.add_button.clicked.connect(self.add_word_button)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        self.label.setAlignment(Qt.AlignCenter)  # Align the label text to the center

        layout.addWidget(self.label)
        layout.addWidget(self.text_area)
        layout.addWidget(self.add_button)

        self.text_area.hide()  # Hide text area by default
        self.add_button.hide()  # Hide button by default

        self.setMinimumSize(200, 100)
        self.setMaximumSize(300, 300)  # Increased maximum height to ensure the enlarged text area is fully visible

    def enterEvent(self, event):
        if not self.hovered:
            self.hovered = True
            self.text_area.show()  # Show text area on hover
            self.add_button.show()  # Show button on hover
            self.resize(300, 300)
            event.accept()

    def leaveEvent(self, event):
        if self.hovered:
            self.hovered = False
            self.text_area.hide()  # Hide text area when not hovering
            self.add_button.hide()  # Hide button when not hovering
            self.resize(200, 100)
            event.accept()

    def add_word_button(self):
        text = self.text_area.toPlainText()  # Get text from text area
        self.process_text(text)  # Call a function to process the text

    def process_text(self, text):
        print("Text from text area:", text)  # Example: Print text to console

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FloatingWindow()

    screen_rect = QApplication.primaryScreen().geometry()
    locate_y = (screen_rect.height() - 100) // 2
    window.setGeometry(0, locate_y, 200, 100)
    window.show()
    sys.exit(app.exec())
