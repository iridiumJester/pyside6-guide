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
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QPushButton,
    QInputDialog
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = None
        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(480, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Kitsch Inventory")
        title_label.setStyleSheet('font-size: 20px;')

        # instructions
        instructions = "Welcome! Click the category names or any button to begin tracking your shopping."
        self.instructions_label = QLabel(instructions)

        # show category tables
        table_hbox = QHBoxLayout()
        self.shopping_list = QTableWidget(2,2)
        self.shopping_list.setHorizontalHeaderLabels(["Name", "#"])
        self.shopping_list.setVerticalHeaderLabels(["", ""])

        table_hbox.addWidget(self.shopping_list)

        # set items
        self.items = [
            ["Granola Bars", "1 box"],
            ["Potato Chips" , "2 bags"]
        ]

        # create buttons
        button_hbox = QHBoxLayout()
        self.add_button = QPushButton("Add new")
        self.add_button.clicked.connect(self.add_new)

        self.edit_button = QPushButton("Update items")
        self.edit_button.clicked.connect(self.edit_items)

        self.shopping_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # show items

        # input for user name
        self.item_name = QLineEdit()
        self.item_name.setPlaceholderText("Name goes here")

        button_hbox.addWidget(self.add_button)
        button_hbox.addWidget(self.edit_button)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.instructions_label)
        layout.addLayout(table_hbox)
        layout.addLayout(button_hbox)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

    def add_new(self, checked):
        if self.w is None:
            self.w = NewWindow()
            self.w.show()
        else:
            self.w.close()  # Close window.
            self.w = None

    def edit_items(self, checked):
        if self.w is None:
            self.w = UpdateWindow()
            self.w.show()
        else:
            self.w.close()  # Close window.
            self.w = None

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Adding items...")
        self.label.setStyleSheet('font-size: 20px;')
        layout.addWidget(self.label)
        self.setLayout(layout)

class UpdateWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Updating items...")
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()