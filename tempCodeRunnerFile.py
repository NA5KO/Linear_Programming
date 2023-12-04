import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt


def exit_program():
    app.quit()

class Exercice2Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage Production of a Company")

        # Set window size and position
        self.setGeometry(100, 100, 800, 600)

        # Apply background image to window using stylesheet
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("tech-background-1l29np90hcci8axg.jpg").scaled(self.size())))
        self.setPalette(palette)

        # Title label
        title_label = QLabel("Manage Production of a Company", self)
        title_label.setFont(QFont("Arial", 30, QFont.Bold))
        title_label.setStyleSheet("color: #FF4949;")
        title_label.setAlignment(Qt.AlignCenter)

        # Wording label
        wording_label = QLabel("Wording: This is where you describe the exercise.", self)
        wording_label.setFont(QFont("Arial", 15))
        wording_label.setStyleSheet("color: white;")
        wording_label.setAlignment(Qt.AlignCenter)

        # Labels and text fields for inputs
        input_labels = [
            "Months 1:", "Months 2:", "Months 3:", "Months 4:", "Months 5:", "Months 6:", "Months 7:", "Months 8:",
            "Months 9:", "Months 10:", "Months 11:", "Months 12:",
            "Initial Stock:", "Initial Employee Number:", "Salary of Employee:",
            "Number of Hours for One Employee per Month:", "Max Supplementary Hours:",
            "Price of Supplementary Hour:", "Number of Hours per Shoes Pair:",
            "Price of Matiere Primaire for One Pair:", "Recruitment Fees:", "Licensing Fees:",
            "Stocking Fees:"
        ]

        self.input_fields = {}

        input_layout = QVBoxLayout()
        input_layout.addWidget(title_label)
        input_layout.addWidget(wording_label)

        for label_text in input_labels:
            label = QLabel(label_text, self)
            label.setFont(QFont("Arial", 12))
            label.setStyleSheet("color: white;")
            label.setFixedSize(600, 40)
            input_layout.addWidget(label)
            line_edit = QLineEdit(self)
            self.input_fields[label_text] = line_edit
            input_layout.addWidget(line_edit)

        # Exit Button
        exit_button = QPushButton("Exit", self)
        exit_button.setFont(QFont("Arial", 16))
        exit_button.setFixedSize(100, 40)
        exit_button.setStyleSheet("background-color: #FF4949; color: white; border: 1px solid white ; border-radius: 10px; active {background-color: #FF4949;}")
        exit_button.clicked.connect(exit_program)

        exit_layout = QVBoxLayout()  # Create a layout for the exit button
        exit_layout.addWidget(exit_button)
        exit_layout.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(exit_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex2_window = Exercice2Window()
    ex2_window.show()
    sys.exit(app.exec_())
