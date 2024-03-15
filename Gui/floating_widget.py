from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QComboBox,
    QHBoxLayout,
)
from PySide6.QtCore import Qt, QPoint


class FABWidget(QPushButton):
    def __init__(self):
        super().__init__()

        # Set button properties
        self.setText("+")
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 25px;
                font-size: 20px;
                border: none;
                }
            QPushButton:hover {
                background-color: #0056b3;
                }
            """
        )

        # Set window properties
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Position the button initially
        self.setGeometry(100, 100, 50, 50)

        # Variables to track mouse movement
        self.drag_start_position = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPosition() - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            new_position = event.globalPosition() - self.drag_start_position
            self.move(new_position.toPoint())  # Convert QPointF to QPoint

    def mouseReleaseEvent(self, event):
        self.drag_start_position = QPoint()

    def mouseDoubleClickEvent(self, event):
        input_widget = InputWidget()
        input_widget.move(self.mapToGlobal(QPoint(0, self.height() + 5)))
        input_widget.show()
        print("double clicked")


class InputWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set window properties
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create input field
        self.input_field = QLineEdit(self)
        self.input_field.setMaximumWidth(200)
        self.input_field.setMaximumHeight(30)

        # Create dropdown menus
        langs = ["en", "ar", "es"]
        self.dropdown1 = QComboBox(self)
        self.dropdown1.addItems(langs)
        self.dropdown1.setMaximumWidth(60)
        self.dropdown2 = QComboBox(self)
        self.dropdown2.addItems(langs)
        self.dropdown2.setMaximumWidth(60)

        # Create layout
        layout = QHBoxLayout()
        layout.addWidget(self.dropdown1)
        layout.addWidget(self.dropdown2)
        layout.addWidget(self.input_field)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    fab = FABWidget()
    fab.show()
    app.exec()
