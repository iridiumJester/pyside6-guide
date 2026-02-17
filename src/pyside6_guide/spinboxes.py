"""
spinboxes.py
by iridiumJester
A demo of the two main types of spinboxes
"""

import random
import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spinbox City")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("--- Spinbox experiment app ---")

        # Create An HBox Layout with a QSpinBox that gets a whole number
        age_input_hbox = QHBoxLayout()
        age_label = QLabel("Age: ")
        self.age_spinbox = QSpinBox()

        # set min and max number
        self.age_spinbox.setMinimum(1)
        self.age_spinbox.setMaximum(100)

        # double spinbox yay
        double_hbox = QHBoxLayout()
        double_label = QLabel("USD: ")
        self.double_spinbox = QDoubleSpinBox()
        self.double_spinbox.setPrefix("$")
        self.double_spinbox.setSingleStep(0.25)
        self.double_spinbox.setMinimum(0)
        self.double_spinbox.setMaximum(1000)

        # add widgets for above labels and inputs
        age_input_hbox.addWidget(age_label)
        age_input_hbox.addWidget(self.age_spinbox)
        double_hbox.addWidget(double_label)
        double_hbox.addWidget(self.double_spinbox)

        # 2 buttons in an hbox: one for calculating & a clear button
        process_hbox = QHBoxLayout()
        calc_button = QPushButton("Do something crazy")
        calc_button.clicked.connect(self.calculate)

        clear_button = QPushButton("Reset your numbers")
        clear_button.clicked.connect(self.clear_text)

        # add secret!
        secret_hbox = QHBoxLayout()
        self.secret_button = QPushButton("Reveal crazy secret?")
        self.secret_button.clicked.connect(self.reveal_secret)
        self.secret_button.hide()
        self.secret_quota = 0

        # add widgets
        process_hbox.addWidget(calc_button)
        process_hbox.addWidget(clear_button)
        secret_hbox.addWidget(self.secret_button)

        # display the instructions and results
        self.instructions = "Put in your age and a dollar amount. Then click buttons."
        self.instructions += " You get it."
        self.instructions_label = QLabel(self.instructions)
        self.instructions_label.setWordWrap(True)

        """
        Challenge: make a simple calculator app that uses 2 inputs.
            * Pick a math or science formula (like area of circle or force).
            * Change the instructions to explain what the user should do.
            * Format the results by rounding the output to 2 decimal places.
            * Format the output using clear language.
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addLayout(age_input_hbox)
        layout.addLayout(double_hbox)
        layout.addLayout(process_hbox)
        layout.addWidget(self.instructions_label)
        layout.addLayout(secret_hbox)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def value_changed(self, value):
        print(f"Value Changed: doublespinbox: {value} - spinbox: {self.age_spinbox.value}")

    def value_changed_str(self, str_value):
        print(f"Value Changed (as string): {str_value}")

    def calculate(self):
        # calculate
        spinbox_num = self.age_spinbox.value()
        doublebox_num = self.double_spinbox.value()
        random_int = random.randint(1, 100)
        if spinbox_num == 1 or doublebox_num == 0.00:
            self.instructions_label.setText("You have to change the numbers first!")
        else:
            crazy_number = ((spinbox_num * (doublebox_num * 3)) * random_int / 77)
            self.instructions_label.setText(f"Here's your crazy number: {crazy_number}")
            if self.secret_quota < 4:
                self.secret_quota += 1
            elif self.secret_quota == 4:
                self.secret_button.show()
                self.secret_quota += 1

    def clear_text(self):
        # reset inputs
        spinbox_num = self.age_spinbox.value()
        doublebox_num = self.double_spinbox.value()
        if spinbox_num == 1 and doublebox_num == 0.00:
            self.instructions_label.setText("You want me to reset nothing?")
        else:
            self.age_spinbox.setValue(1)
            self.double_spinbox.setValue(0.00)
            self.instructions_label.setText(self.instructions)
    
    def reveal_secret(self):
        # reveal "crazy number" formula
        self.instructions_label.setText("The formula is: (age * (usd * 3)) * random / 77. Random is between 1 and 100.")
        self.secret_button.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
