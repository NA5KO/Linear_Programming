"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush, QIntValidator, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, \
    QMessageBox, QHBoxLayout, QTableWidget, QTableWidgetItem, QScrollArea


def exit_program():
    app.quit()


class Exercise3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input_boxes = []

        self.init_ui()

    def init_ui(self):
        # Set the background image
        background_image_path = "background_image.jpg"
        self.set_background_image(background_image_path)

        # Big title "Enoncé"
        title_label = QLabel("Wording :")
        title_label.setFont(QFont("Roboto", 30))
        title_label.setStyleSheet("color: #FF4949;")

        # Exercise text
        exercise_text = " A bank with a budget of B dinars is looking to determine the optimal location of new branches and DAB servers to open in January 2006.\n The investment is K dinars per branch, and D dinars per DAB server.\n Nine regions are under consideration. In each region, there can be at most one branch.\n By opening an agency in region Ri, the bank will gain a number of customers equal to a% of the population of region Ri and b% of the population of neighboring regions.\n A DAB server in region Ri will gain a number of customers equal to c% of the population of region Ri.\n The matrix A = (aij) i = 1, ..., 9 and j = 1, ..., 9 gives for each region the neighboring regions (1 if neighboring regions, 0 otherwise)."
        exercise_label = QLabel(exercise_text)
        exercise_label.setFont(QFont("Roboto", 12))
        exercise_label.setStyleSheet("color: white;")

        # Sentences and input boxes
        terms = ["Nombre de regions", "Budget total", "Cout douverture agence", "Cout douverture DAB",
                 "%Pop regions agence", "%Pop regions voisins", "%Pop DAB"]

        widget = QWidget()
        layout = QVBoxLayout(widget)

        for i in range(7):
            input_layout = QHBoxLayout()
            sentence_label = QLabel(f" {terms[i]}: ")
            sentence_label.setFont(QFont("Roboto", 15))
            sentence_label.setStyleSheet("color: white;")

            input_box = QLineEdit(self)
            input_box.setMaxLength(3)
            input_box.setMaximumWidth(50)
            input_box.setAlignment(Qt.AlignCenter)
            input_box.setValidator(QIntValidator(1, 999))

            self.input_boxes.append(input_box)

            input_layout.addWidget(sentence_label)
            input_layout.addWidget(input_box)

            layout.addLayout(input_layout)  # Add the horizontal layout to the main layout

        # Table
        table = QTableWidget(10, 10)
        table.setMinimumSize(1000, 1000)

        # Wrap the table with a QScrollArea
        table_scroll_area = QScrollArea()
        table_scroll_area.setWidget(table)
        table_scroll_area.setWidgetResizable(True)

        # Solve button with dark blue theme
        solve_button = QPushButton("Solve")
        solve_button.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        solve_button.setMaximumWidth(150)
        solve_button.clicked.connect(self.solve_button_clicked)

        exit_button = QPushButton("Exit", self)
        exit_button.setFont(QFont("Arial", 16))
        exit_button.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        exit_button.setMaximumWidth(150)
        exit_button.clicked.connect(exit_program)

        # Button layout: Solve and Exit buttons in a horizontal layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(solve_button)
        button_layout.addWidget(exit_button)

        # Main layout with vertical alignment
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.setSpacing(10)
        main_layout.addWidget(exercise_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(widget, alignment=Qt.AlignCenter)
        main_layout.addWidget(table_scroll_area, alignment=Qt.AlignCenter)  # Add the scroll area instead of the table directly
        main_layout.addLayout(button_layout)  # Add the button layout here
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set the main layout and window properties
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setWindowIcon(QIcon("star.png"))
        self.setWindowTitle("Exercise Solver")
        self.resize(1000, 900)
        self.show()

    def solve_button_clicked(self):
        # Check if all input boxes have values before proceeding
        for input_box in self.input_boxes:
            if not input_box.text():
                QMessageBox.warning(self, "Warning", "Please fill in all input boxes before solving.")
                return

        # Extract data from input boxes
        employee_numbers = [int(box.text()) for box in self.input_boxes]

        # Clear the table
        table = self.centralWidget().findChild(QTableWidget)
        table.clearContents()

        # Fill the table with dummy data (you should replace this with your actual data)
        for i in range(15):
            for j in range(15):
                item = QTableWidgetItem(f"{i * 15 + j}")
                table.setItem(i, j, item)

    def set_background_image(self, image_path):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap(image_path).scaled(self.size())))
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex3_window = Exercise3()
    ex3_window.show()
"""
import sys
import PL1
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTableWidget, QSpinBox, QPushButton, \
    QVBoxLayout, QHBoxLayout, QMainWindow, QMessageBox


def exit_program():
    app.quit()

class Exercise1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        background_image_path = "background_image.jpg"
        self.set_background_image(background_image_path)

        # Section 1: Titre
        self.titre = QLabel("Wording :", self)
        self.titre.setFont(QFont("Roboto", 20, QFont.Bold))
        self.titre.setStyleSheet("color: #FF4949;")
        self.titre.setAlignment(Qt.AlignCenter)

        # Section 2: Introduction et tableau
        self.introduction = QLabel("A bank with a budget of B dinars is looking to determine the optimal location of new branches and DAB servers to open in January 2006.\n The investment is K dinars per branch, and D dinars per DAB server.\n Nine regions are under consideration. In each region, there can be at most one branch.\n By opening an agency in region Ri, the bank will gain a number of customers equal to a% of the population of region Ri and b% of the population of neighboring regions.\n A DAB server in region Ri will gain a number of customers equal to c% of the population of region Ri.\n The matrix A = (aij) i = 1, ..., 9 and j = 1, ..., 9 gives for each region the neighboring regions (1 if neighboring regions, 0 otherwise)")
        self.introduction.setFont(QFont("Roboto", 10))
        self.introduction.setStyleSheet("color: white;")
        self.tableau = QTableWidget(10, 11)
        self.tableau.setHorizontalHeaderLabels(["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"])
        self.tableau.setVerticalHeaderLabels(["Nombre de Population", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"])

        for i in range(7):
            for j in range(5):
                spin_box = QSpinBox(self)
                spin_box.setRange(0, 999999)  # Set the range according to your needs
                self.tableau.setCellWidget(i, j, spin_box)

        # Section 3: Champs de saisie
        self.ligne1 = QLabel("Main d’œuvre(nb_ouvries) :")
        self.ligne1.setFont(QFont("Roboto", 10))
        self.ligne1.setStyleSheet("color: white;")
        self.saisie1 = QSpinBox(self)
        self.saisie1.setMaximumWidth(100)
        self.saisie1.setAlignment(Qt.AlignCenter)
        self.ligne2 = QLabel("Eau d’irrigation(m3):")
        self.ligne2.setFont(QFont("Roboto", 10))
        self.ligne2.setStyleSheet("color: white;")
        self.saisie2 = QSpinBox(self)
        self.saisie2.setMaximumWidth(100)
        self.saisie2.setAlignment(Qt.AlignCenter)
        self.ligne3 = QLabel("Heures machine(heures machine) :")
        self.ligne3.setFont(QFont("Roboto", 10))
        self.ligne3.setStyleSheet("color: white;")
        self.saisie3 = QSpinBox(self)
        self.saisie3.setMaximumWidth(100)
        self.saisie3.setAlignment(Qt.AlignCenter)
        self.ligne4 = QLabel("Cout Main :")
        self.ligne4.setFont(QFont("Roboto", 10))
        self.ligne4.setStyleSheet("color: white;")
        self.saisie4 = QSpinBox(self)
        self.saisie4.setMaximumWidth(100)
        self.saisie4.setAlignment(Qt.AlignCenter)
        self.ligne5= QLabel("cout Eau:")
        self.ligne5.setFont(QFont("Roboto", 10))
        self.ligne5.setStyleSheet("color: white;")
        self.saisie5 = QSpinBox(self)
        self.saisie5.setMaximumWidth(100)
        self.saisie5.setAlignment(Qt.AlignCenter)

        # Section 4: Bouton
        self.bouton = QPushButton("Solve", self)
        self.bouton.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        self.bouton.setMaximumWidth(150)
        self.bouton.clicked.connect(self.solve)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setFont(QFont("Arial", 16))
        self.exit_button.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        self.exit_button.clicked.connect(exit_program)
        self.exit_button.setMaximumWidth(150)

        # Mise en page
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.titre)
        layout.addWidget(self.introduction)
        layout.addWidget(self.tableau)
        layout.addWidget(self.ligne1, alignment=Qt.AlignCenter)
        layout.addWidget(self.saisie1, alignment=Qt.AlignCenter)
        layout.addWidget(self.ligne2, alignment=Qt.AlignCenter)
        layout.addWidget(self.saisie2, alignment=Qt.AlignCenter)
        layout.addWidget(self.ligne3, alignment=Qt.AlignCenter)
        layout.addWidget(self.saisie3, alignment=Qt.AlignCenter)
        layout.addWidget(self.ligne4, alignment=Qt.AlignCenter)
        layout.addWidget(self.saisie4, alignment=Qt.AlignCenter)
        layout.addWidget(self.ligne5, alignment=Qt.AlignCenter)
        layout.addWidget(self.saisie5, alignment=Qt.AlignCenter)
        layout.setSpacing(5)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.bouton)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(button_layout)

        self.setWindowIcon(QIcon("star.png"))
        self.setWindowTitle("PL1")
        self.resize(800, 700)

    def set_background_image(self, image_path):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("Background_Image.jpg").scaled(self.size())))
        self.setPalette(palette)

    def get_tableau_values(self):
        # Itère à travers le tableau et récupère les valeurs des cellules
        tableau_values = {}
        for i in range(7):
            for j in range(5):
                spin_box = self.tableau.cellWidget(i, j)
                if spin_box is not None:
                    key = (self.tableau.verticalHeaderItem(i).text(), self.tableau.horizontalHeaderItem(j).text())
                    tableau_values[key] = spin_box.value()
        return tableau_values

    def get_saisie_values(self):
        # Récupère les valeurs des saisies
        saisie_values = [self.saisie1.value(), self.saisie2.value(), self.saisie3.value(),self.saisie4.value(),self.saisie5.value()]
        return saisie_values

    def solve(self):
        t=self.get_tableau_values()
        s=self.get_saisie_values()
        print(t,s)
        results = PL1.solve_optimization(t,s)
        print(results)
         #Display the solution
        message = f"The minimum number of employees needed is {results}"
        QMessageBox.information(self, "Solution", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex1_window = Exercise1()
    ex1_window.show()
    sys.exit(app.exec_())
