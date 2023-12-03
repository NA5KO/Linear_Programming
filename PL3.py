import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
)


class MyWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Créer la fenêtre
        self.setWindowTitle("Ma fenêtre")
        self.resize(300, 200)

        # Créer un layout vertical
        layout = QVBoxLayout()

        # Créer la première section
        titre = QLabel("Enonce")
        titre.setFont(QFont("Arial", 24))
        layout.addWidget(titre)

        # Créer la deuxième section
        introduction = QLabel("Introduction à l'exercice")
        layout.addWidget(introduction)
        tableau = QTableWidget(8, 6)
        tableau.setHorizontalHeaderLabels(["Col 1", "Col 2", "Col 3", "Col 4", "Col 5", "Col 6"])
        tableau.setVerticalHeaderLabels(["Ligne 1", "Ligne 2", "Ligne 3", "Ligne 4", "Ligne 5", "Ligne 6", "Ligne 7", "Ligne 8"])
        layout.addWidget(tableau)

        # Créer la troisième section
        phrase1 = QLabel("Phrase 1")
        layout.addWidget(phrase1)
        input1 = QLineEdit()
        layout.addWidget(input1)
        phrase2 = QLabel("Phrase 2")
        layout.addWidget(phrase2)
        input2 = QLineEdit()
        layout.addWidget(input2)
        phrase3 = QLabel("Phrase 3")
        layout.addWidget(phrase3)
        input3 = QLineEdit()
        layout.addWidget(input3)

        # Créer la quatrième section
        bouton = QPushButton("Résoudre")
        layout.addWidget(bouton)

        # Définir le layout
        self.setLayout(layout)

        # Connecter l'événement de clic du bouton
        #bouton.clicked.connect(self.on_click)

    #def on_click(self):
        # Récupération des valeurs des entrées
        phrase1 = input1.text()
        phrase2 = input2.text()
        phrase3 = input3.text()

        # Traitement des données
        # ...

        # Affichage des résultats
        # ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
