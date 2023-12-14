import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget , QStackedWidget
from PyQt5.QtGui import QPixmap, QFont , QPalette, QBrush 
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import Exercise2

def exit_program():
    app.quit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('Star.png'))
        self.setWindowTitle("Python LP Exercises With Gurobi")

        # Set window size and position
        window_width = 800
        window_height = 600
        screen_geometry = app.primaryScreen().geometry()
        x_coordinate = int((screen_geometry.width() / 2) - (window_width / 2))
        y_coordinate = int((screen_geometry.height() / 2) - (window_height / 2))
        self.setGeometry(x_coordinate, y_coordinate, window_width, window_height)

        # Apply background image to window using stylesheet
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("background_image.jpg").scaled(self.size())))
        self.setPalette(palette)

        # Project Name in the middle at the top
        self.project_name = QLabel("Linear Programming Exercises", self)
        self.project_name.setStyleSheet("color: #FF4949;")
        self.project_name.setFont(QFont("Arial", 30, QFont.Bold))
        self.project_name.setAlignment(Qt.AlignCenter)

        # Description of the project
        self.project_description = QLabel("This project aims to Let the user choose a Linear Programing Exercice.\n After choosing an exercice,the user can read the wording and then fill the fields\n with some variables which he can later solve the exercice based on those variables ", self)
        self.project_description.setFont(QFont("Arial", 15))
        self.project_description.setStyleSheet("color: white;")
        self.project_description.setAlignment(Qt.AlignCenter)

        # Layout to contain exercise buttons
        self.exercise_layout = QVBoxLayout()
        self.exercise_frame = QWidget(self)
        self.exercise_frame.setLayout(self.exercise_layout)
        self.exercise_layout.setAlignment(Qt.AlignHCenter)

        # Function to handle exercise selection

        # Example buttons for exercises
        Exercise_names = [
    "Optimise Argiculture Zone",
    "Manage production of a company",
    "Planify the needs of human ressources",
    "choice of location of bank branches",
    "Positioning Problem",
    "Netwrok Flow Problem",
    ]
        for exercise_name in Exercise_names:
            exercise_button = QPushButton(exercise_name, self)
            exercise_button.setFont(QFont("Arial", 12))
            exercise_button.setStyleSheet("background-color: white; color: black; border: 1px solid white ; border-radius: 10px ; active {background-color: #FF4949;}")
            exercise_button.setFixedSize(600, 40)
            exercise_button.clicked.connect(lambda checked, btn=exercise_button: self.select_exercise(btn))
            self.exercise_layout.addWidget(exercise_button)

        # Arrange buttons in 3 rows at the center
        self.exercise_layout.addStretch()
        self.exercise_layout.addStretch()
        self.exercise_layout.addStretch()

        # Exit Button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setFont(QFont("Arial", 16))
        self.exit_button.setFixedSize(100, 40)
        self.exit_button.setStyleSheet("background-color: #FF4949; color: white; border: 1px solid white ; border-radius: 10px; active {background-color: #FF4949;}")
        self.exit_button.clicked.connect(exit_program)

        exit_layout = QVBoxLayout()  # Create a layout for the exit button
        exit_layout.addWidget(self.exit_button)
        exit_layout.setAlignment(Qt.AlignCenter)  

        # Collaborators listed under each other
        self.collaborators = QLabel("Collaborators:\nAmine Yahya\nAmen Dhouibi\nInes Zghal\nLamya Bel Haj Sghayer\nRoua Timoumi", self)
        self.collaborators.setFont(QFont("Arial", 12))
        self.collaborators.setStyleSheet("color: White;")
        self.collaborators.setAlignment(Qt.AlignCenter)  # Center-align the collaborators


        # Arrange widgets
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.project_name)
        layout.addWidget(self.project_description)
        layout.addWidget(self.exercise_frame)
        layout.addLayout(exit_layout)
        layout.addWidget(self.collaborators)
        self.setCentralWidget(central_widget)


    def select_exercise(self, exercise_button):
        case = exercise_button.text()
        if case == "Optimise Argiculture Zone":
            from Exercise1 import Exercise1
            self.exercice1 = Exercise1()
            self.exercice1.show()
        elif case == "Manage production of a company":
            from Exercise2 import Exercise2
            self.exercise2 = Exercise2()
            self.exercise2.show()
        elif case == "Planify the needs of human ressources":
            from Exercise3 import Exercise3
            self.exercise3 = Exercise3()
            self.exercise3.show()
            #elif case == "choice of location of bank branches":
            #    from Exercice4 import Exercice4
            #    self.exercice4 = Exercice4()
             #   self.exercice4.show()
        elif case == "Positioning Problem":
            from Exercise5 import Exercise5
            self.exercics5 = Exercise5()
            self.exercics5.show()
            #elif case == "Netwrok Flow Problem":
              #  from Exercice6 import Exercice6
              #  self.exercice6 = Exercice6()
             #   self.exercice6.show()
        else:
            pass
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
