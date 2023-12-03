import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush, QIntValidator, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox


class ExerciseSolver(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input_boxes = []

        self.init_ui()

    def init_ui(self):
        # Set the background image
        background_image_path = "C:/Users/21658/Desktop/RT3/RO/Project/Background_Image/background_image.jpg"
        self.set_background_image(background_image_path)

        # Big title "Enoncé"
        title_label = QLabel("Enoncé")
        title_label.setFont(QFont("Roboto", 20))
        title_label.setStyleSheet("color: red;")

        # Exercise text
        exercise_text = "Un bureau de poste a des besoins en personnel lors des sept jours de la semaine\nDéterminer la planification permettant de satisfaire les besoins du bureau en recourant\nau minimum d’employés\ntout en sachant que chaque employé doit travailler pendant\ncinq jours consécutifs avant de prendre deux jours de\ncongé"
        exercise_label = QLabel(exercise_text)

        exercise_label.setFont(QFont("Roboto", 12))
        exercise_label.setStyleSheet("color: white;")

        # Sentences and input boxes
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

        widget = QWidget()
        layout = QVBoxLayout(widget)

        for i in range(7):
            sentence_label = QLabel(f"Nombre d'employés le {jours[i]}: ")
            sentence_label.setFont(QFont("Roboto", 15))
            sentence_label.setStyleSheet("color: white;")

            input_box = QLineEdit(self)
            input_box.setMaxLength(3)
            input_box.setMaximumWidth(50)
            input_box.setAlignment(Qt.AlignCenter)
            input_box.setValidator(QIntValidator(1, 999))

            self.input_boxes.append(input_box)

            layout.addWidget(sentence_label, alignment=Qt.AlignCenter)
            layout.addWidget(input_box, alignment=Qt.AlignCenter)

        # Solve button with dark blue theme
        solve_button = QPushButton("Solve")
        solve_button.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 5px; font-size: 14pt; padding: 10px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        solve_button.clicked.connect(self.solve_button_clicked)

        # Main layout with vertical alignment
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.setSpacing(10)
        main_layout.addWidget(exercise_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(widget, alignment=Qt.AlignCenter)
        main_layout.addWidget(solve_button, alignment=Qt.AlignCenter)
        main_layout.setContentsMargins(0, 0, 0, 0)


        # Set the main layout and window properties
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setWindowIcon(QIcon("star.jpg"))
        self.setWindowTitle("Exercise Solver")
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def solve_button_clicked(self):
        # Check if all input boxes have values before proceeding
        for input_box in self.input_boxes:
            if not input_box.text():
                QMessageBox.warning(self, "Warning", "Please fill in all input boxes before solving.")
                return

        # Extract data from input boxes
        employee_numbers = [int(box.text()) for box in self.input_boxes]

        # Implement your actual solution logic here
        # This is a placeholder example, replace it with your algorithm
        # The solution should calculate the minimum number of employees needed
        # based on the provided employee numbers and working days
        # ... (your solution logic here) ...

        # Display the solution
        message = f"The minimum number of employees needed is "
        QMessageBox.information(self, "Solution", message)

    def set_background_image(self, image_path):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("Background_Image.jpg").scaled(self.size())))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExerciseSolver()
    sys.exit(app.exec_())
