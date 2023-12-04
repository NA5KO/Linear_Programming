import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout 
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap, QDoubleValidator, QIntValidator ,QIcon
from PyQt5.QtCore import Qt

def exit_program():
    app.quit()

class Exercise2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage Production of a Company")
        self.setGeometry(100, 100, 800, 600)

        # Apply background image to window using stylesheet
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("Background_image.jpg").scaled(self.size())))
        self.setWindowIcon(QIcon("star.png"))
        self.setPalette(palette)

        # Title label
        title_label = QLabel("Manage Production of a Company", self)
        title_label.setFont(QFont("Arial", 30, QFont.Bold))
        title_label.setStyleSheet("color: #FF4949;")
        title_label.setAlignment(Qt.AlignCenter)

        # Wording label
        wording_label = QLabel("Wording: \n Determine the optimal production schedule and the best policy for managing the workforce \n by Determining for how long you will be working,staff salary ,Supp hours   \n Working cost ,initial staff , working hours , hours per product ... \n", self)
        wording_label.setFont(QFont("Arial", 15))
        wording_label.setStyleSheet("color: white;")
        wording_label.setAlignment(Qt.AlignCenter)

        # Content widget to hold the input fields
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        # Add title and wording labels to content layout
        content_layout.addWidget(title_label)
        content_layout.addWidget(wording_label)

        # Add your labels and line edits here...
        input_labels = [
            "Months 1:", "Months 2:", "Months 3:", "Months 4:", "Months 5:", "Months 6:", "Months 7:", "Months 8:",
            "Months 9:", "Months 10:", "Months 11:", "Months 12:",
            "Initial Stock:", "Initial Employee Number:", "Salary of Employee:",
            "Employee Hours/M", "Max Supp Hours:",
            "Price of Supp Hour:", "Hours for pair :",
            "Price of one pair prod:", "Recruitment Fees:", "Licensing Fees:",
            "Stocking Fees:"
        ]

        rows = len(input_labels) // 2 + len(input_labels) % 2

        for row in range(rows):
            hbox = QHBoxLayout()
            for column in range(2):
                index = row * 2 + column
                if index < len(input_labels):
                    label = QLabel(input_labels[index], self)
                    label.setFont(QFont("Arial", 12))
                    label.setStyleSheet("color: white;")

                    line_edit = QLineEdit(self)
                    line_edit.setFixedSize(200, 25)

                    # Set validator for line edit fields to accept only integers or floats
                    if "Number" in input_labels[index] or "Price" in input_labels[index]:
                        line_edit.setValidator(QDoubleValidator())
                    else:
                        line_edit.setValidator(QIntValidator())

                    hbox.addWidget(label)
                    hbox.addWidget(line_edit)

            content_layout.addLayout(hbox)

        # Set the content widget as the central widget
        self.setCentralWidget(content_widget)

        # Exit Button
        exit_button = QPushButton("Exit", self)
        exit_button.setFont(QFont("Arial", 16))
        exit_button.setStyleSheet("background-color: #FF4949; color: white; border: 1px solid white ; border-radius: 10px; active {background-color: #FF4949;}")
        exit_button.clicked.connect(exit_program)

        # Solve Button
        solve_button = QPushButton("Solve", self)
        solve_button.setFont(QFont("Arial", 16))
        solve_button.setStyleSheet("background-color: #FF4949; color: white; border: 1px solid white ; border-radius: 10px; active {background-color: #FF4949;}")
        # Connect solve_button to a solve function if needed

        # Layout for exit and solve buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(solve_button)
        buttons_layout.addWidget(exit_button)
        buttons_layout.setAlignment(Qt.AlignCenter)

        # Add buttons layout to the content widget
        content_layout.addLayout(buttons_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex2_window = Exercise2()
    ex2_window.show()
    sys.exit(app.exec_())
