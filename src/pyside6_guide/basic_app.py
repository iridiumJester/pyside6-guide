"""
basic_app.py
by iridiumJester
Demo of labels, text inputs, and buttons.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(520, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic greeting app")

        # input for user name
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name goes here")

        # input for silliness
        self.silly_input = QLineEdit()
        self.silly_input.setPlaceholderText("How silly are you out of 10")

        # push button greeting
        greeting_button = QPushButton("Get greeting")
        greeting_button.clicked.connect(self.get_greeting)

        # label to greet user
        greeting = "Hey. Enter your name and silliness and press that button"
        self.greeting_label = QLabel(greeting)
        
        # clear push button 
        clear_button = QPushButton("Reset text")
        clear_button.clicked.connect(self.clear_text)

        """
        CHALLENGES:
            * Add more inputs
            * Add clear button to reset
            * Add HBox for each input that has a label (on the left)
              it should line up btw
                - Add that box where init put input
                layout? then input? idk :?
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.silly_input)
        # put the hbox layout here...
        layout.addWidget(greeting_button)
        layout.addWidget(self.greeting_label)
        layout.addWidget(clear_button)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
        greeting_button.setCheckable(True) 

    def get_greeting(self):
        # get users name and greet them with it
        name = self.name_input.text()
        silliness = self.silly_input.text()
        greeting = f"Hiii {name}!!! You are a {silliness} out of 10 on the silliness scale!"
        self.greeting_label.setText(greeting)

    def clear_text(self):
        # reset inputs
        self.name_input.clear()
        self.silly_input.clear()
        greeting = "Woah! Where'd the text go?"
        self.greeting_label.setText(greeting)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()