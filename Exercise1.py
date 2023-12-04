import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTableWidget, QPushButton, QVBoxLayout, \
    QMainWindow


class Exercice1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        background_image_path = "background_image.jpg"
        self.set_background_image(background_image_path)
        # Section 1: Titre
        self.titre = QLabel("Énoncé", self)
        self.titre.setFont(QFont("Roboto", 20, QFont.Bold))
        self.titre.setStyleSheet("color: red;")
        self.titre.setAlignment(Qt.AlignCenter)

        # Section 2: Introduction et tableau
        self.introduction = QLabel(" L’Etat tunisien veut mettre en valeur une zone agricole de 1000 hectares ou cinq cultures sont à priori possibles :\n le blé, l’orge, le mais, la betterave à sucre et le tournesol. On dispose des données suivantes sur les cinq cultures")
        self.introduction.setFont(QFont("Roboto", 10))
        self.introduction.setStyleSheet("color: white;")
        self.tableau = QTableWidget(7, 5)
        self.tableau.setHorizontalHeaderLabels(["Ble", "Orge", "Mais", "Bet-Sucre", "Tournesol"])
        self.tableau.setVerticalHeaderLabels(["Rendement Q/ha", "Prix de vente UM/Q", "M.O.Ouvriers/ha", "Temps machine H/ha", "Eau m3/ha", "Salaire annuel/ouvrier", "Frais fixe de gestion"])

        # Section 3: Champs de saisie
        self.ligne1 = QLabel("Main d’œuvre(nb_ouvries) :")
        self.ligne1.setFont(QFont("Roboto", 10))
        self.ligne1.setStyleSheet("color: white;")
        self.saisie1 = QLineEdit(self)
        self.saisie1.setMaximumWidth(100)
        self.saisie1.setAlignment(Qt.AlignCenter)
        self.ligne2 = QLabel("Eau d’irrigation(m3):")
        self.ligne2.setFont(QFont("Roboto", 10))
        self.ligne2.setStyleSheet("color: white;")
        self.saisie2 = QLineEdit(self)
        self.saisie2.setMaximumWidth(100)
        self.saisie2.setAlignment(Qt.AlignCenter)
        self.ligne3 = QLabel("Heures machine(heures machine) :")
        self.ligne3.setFont(QFont("Roboto", 10))
        self.ligne3.setStyleSheet("color: white;")
        self.saisie3 = QLineEdit(self)
        self.saisie3.setMaximumWidth(100)
        self.saisie3.setAlignment(Qt.AlignCenter)

        # Section 4: Bouton
        self.bouton = QPushButton("Résoudre", self)
        self.bouton.setStyleSheet("color: red")
        self.bouton.setStyleSheet(
            "QPushButton { background-color: #ff4949; color: white; border: none; border-radius: 20px; font-size: 14pt; padding: 15px; }"
            "QPushButton:hover { background-color: #003366; }"
        )
        self.bouton.setMaximumWidth(150)

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
        layout.setSpacing(10)
        layout.addWidget(self.bouton, alignment=Qt.AlignCenter)

        self.setWindowIcon(QIcon("star.png"))
        self.setWindowTitle("PL1")
        self.resize(800, 600)


    def set_background_image(self, image_path):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("Background_Image.jpg").scaled(self.size())))
        self.setPalette(palette)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Exercice1()
    ex.show()
    sys.exit(app.exec_())
