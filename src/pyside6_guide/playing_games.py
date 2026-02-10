"""
app_starter.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Title Label (Make this bigger, please!)")

        # instructions
        instructions = "Welcome to Kitsch-Inventory. Click the category names or any button to begin tracking your things."
        self.instructions_label = QLabel(instructions)

        # show categories
        self.inventory = QTableWidget(2,2)
        self.inventory.setHorizontalHeaderLabels(["Name", "#"])
        self.inventory.setVerticalHeaderLabels(["", ""])

        # set items
        self.items = [
            ["Granola Bars", "1 box"],
            ["Potato Chips" , "2 bags"]
        ]

        self.inventory.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # show items

        # input for user name
        self.item_name = QLineEdit()
        self.item_name.setPlaceholderText("Name goes here")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.instructions_label)
        layout.addWidget(self.inventory)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()