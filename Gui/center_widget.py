from PySide6.QtWidgets import QApplication

def center(widget):
    # Get the screen's rectangle
    screen_rect = QApplication.primaryScreen().geometry()
    # Get the center point of the screen
    center_point = screen_rect.center()
    # Move the widget to the center of the screen
    widget.move(center_point - widget.rect().center())