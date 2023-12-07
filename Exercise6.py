import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap, QIntValidator, QIcon
from PyQt5.QtCore import Qt

def exit_program():
    app.quit()

class Link:
    def __init__(self, start_node, end_node, duration):
        self.start_node = start_node
        self.end_node = end_node
        self.duration = duration


class Exercise6(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Network Flow Problem")
        self.setGeometry(100, 100, 800, 600)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("Background_image.jpg").scaled(self.size())))
        self.setWindowIcon(QIcon("star.png"))
        self.setPalette(palette)

        title_label = QLabel("Network Flow Problem", self)
        title_label.setFont(QFont("Arial", 30, QFont.Bold))
        title_label.setStyleSheet("color: #FF4949;")
        title_label.setAlignment(Qt.AlignCenter)

        wording_label = QLabel("Wording: \n Determine the optimal Path From a starting node to an end node  \n Start by first creating your network by adding different links.  \n Every link has a starting node , an ending node and a duration \n", self)
        wording_label.setFont(QFont("Arial", 15))
        wording_label.setStyleSheet("color: white;")
        wording_label.setAlignment(Qt.AlignCenter)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        content_layout.addWidget(title_label)
        content_layout.addWidget(wording_label)

        #list of links
        self.links = []

        labels = ["Start Node for the link", "End Node for the link", "Duration for the link"]

        for label in labels:
            hbox = QHBoxLayout()
            lbl = QLabel(label)
            line_edit = QLineEdit()
            hbox.addWidget(lbl)
            hbox.addWidget(line_edit)
            content_layout.addLayout(hbox)
            lbl.setStyleSheet("color: white;")
            lbl.setFont(QFont("Arial", 15))
            line_edit.setObjectName(label)
            line_edit.setStyleSheet("color: black;")
            line_edit.setFont(QFont("Arial", 15))
            line_edit.setMaximumWidth(200)
            if label == "Start Node for the link" or label == "End Node for the link": 
                #only let him input one letter 
                line_edit.setMaxLength(1)
            else:
                line_edit.setValidator(QIntValidator())

        #create the start and end node to be choosen by the user 
        hbox1 = QHBoxLayout()
        Start_Node = QLabel("Start Node", self)
        Start_Node.setFont(QFont("Arial", 15))
        Start_Node.setStyleSheet("color: white;")
        start_node_edit = QLineEdit()
        start_node_edit.setObjectName("Start Node")
        start_node_edit.setStyleSheet("color: black;")
        start_node_edit.setFont(QFont("Arial", 15))
        start_node_edit.setMaximumWidth(200)
        start_node_edit.setMaxLength(1)
        hbox1.addWidget(Start_Node)
        hbox1.addWidget(start_node_edit)

        hbox2 = QHBoxLayout()
        End_Node = QLabel("End Node", self)
        End_Node.setFont(QFont("Arial", 15))
        End_Node.setStyleSheet("color: white;")
        end_node_edit = QLineEdit()
        end_node_edit.setObjectName("End Node")
        end_node_edit.setStyleSheet("color: black;")
        end_node_edit.setFont(QFont("Arial", 15))
        end_node_edit.setMaximumWidth(200)
        end_node_edit.setMaxLength(1)
        hbox2.addWidget(End_Node)
        hbox2.addWidget(end_node_edit)



        exit_button = QPushButton("Exit", self)
        exit_button.setFont(QFont("Arial", 15))
        exit_button.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        exit_button.setMaximumWidth(200)
        exit_button.clicked.connect(exit_program)

        add_button = QPushButton("Add", self)
        add_button.setFont(QFont("Arial", 15))
        add_button.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        add_button.setMaximumWidth(200)
        add_button.clicked.connect(self.add)

        solve_button = QPushButton("Solve", self)
        solve_button.setFont(QFont("Arial", 15))
        solve_button.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        solve_button.setMaximumWidth(200)
        solve_button.clicked.connect(self.solve)

        add_layout = QHBoxLayout()
        add_layout.addWidget(add_button)
        content_layout.addLayout(add_layout)
        content_layout.addLayout(hbox1)
        content_layout.addLayout(hbox2)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(solve_button)
        buttons_layout.addWidget(exit_button)
        content_layout.addLayout(buttons_layout)

        self.setCentralWidget(content_widget)


    def get_input_values(self):
        input_values = {}
        line_edits = self.findChildren(QLineEdit)
        for line_edit in line_edits:
            object_name = line_edit.objectName()
            input_values[object_name] = line_edit.text()
        return input_values

    def add(self):
        input_values = self.get_input_values()
        start_node = input_values.get("Start Node for the link", "")
        end_node = input_values.get("End Node for the link", "")
        duration = input_values.get("Duration for the link", "")

        if not (start_node and end_node and duration):
            QMessageBox.about(self, "Error", "Please fill all the fields")
        else:
            new_link = Link(start_node, end_node, int(duration))
            self.links.append(new_link)
            for line_edit in self.findChildren(QLineEdit):
                line_edit.clear()

    def solve(self):
        input_values = self.get_input_values()
        if input_values["Start Node for the link"] == "" or input_values["End Node for the link"] == "" or input_values["duration for the link"] == "":
            QMessageBox.about(self, "Error", "Please fill all the fields")
        else:
            self.input_values = input_values
            self.close()
            self.exercise = Exercise6()
            self.exercise.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Exercise6()
    main_window.show()
    sys.exit(app.exec_())