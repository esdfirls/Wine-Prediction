from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QLineEdit, QFormLayout, QProgressBar
from PyQt5 import QtGui
import sys
import requests


class MainWindow():
        
    def __init__(self, parent=None):
        #super().__init__(parent)
        self.window = QWidget()
        self.window.setWindowTitle('Wine Predict')
        self.window.setGeometry(200, 200, 450, 120)
        self.window.move(60, 15)

        #
        self.label = QLabel('<h1>Wine Quality Prediction</h1>', parent=self.window)
        self.tipo = QComboBox()
        self.layout = QFormLayout()
        self.get_datab = QPushButton('Predict Now')
        self.get_datab.clicked.connect(self.get_data)
        self.pbar = QProgressBar()
        #
        self.fixed = QLineEdit('7')
        self.citric = QLineEdit('1')
        self.volatile = QLineEdit('1')
        self.residual = QLineEdit('45')
        self.chlorides = QLineEdit('0.5')
        self.freesulfur = QLineEdit('150')
        self.totalsulfur = QLineEdit('200')
        self.density =  QLineEdit('1')
        self.ph = QLineEdit('3')
        self.sulphates =  QLineEdit('1')
        self.alcohol = QLineEdit('10')
        self.response = QLabel('')

        # stylesheet = 'background-image: url("wine_background.jpg");'
        # self.window.setStyleSheet(stylesheet)

        #
        self.tipo.addItems(['0','1'])
        self.layout.addWidget(self.label)
        self.layout.addRow('Type:', self.tipo)
        self.layout.addRow('Fixed Acidity:', self.fixed)
        self.layout.addRow('Volatile Acidity:', self.volatile)
        self.layout.addRow('Citric Acid:', self.citric)
        self.layout.addRow('Residual Surgar:', self.residual)
        self.layout.addRow('Chlorides:', self.chlorides)
        self.layout.addRow('Free SO2:', self.freesulfur)
        self.layout.addRow('Total SO2:', self.totalsulfur)
        self.layout.addRow('Density:', self.density)
        self.layout.addRow('pH:', self.ph)
        self.layout.addRow('Sulphates:', self.sulphates)
        self.layout.addRow('Alcohol:', self.alcohol)
        self.layout.addWidget(self.get_datab)
        self.layout.addRow('Progress:', self.pbar)
        self.layout.addWidget(self.response)
        self.window.setLayout(self.layout)


        self.window.show()


    def get_data(self):
        self.pbar.setValue(50)
        request_url = f"https://winepredict.azurewebsites.net/wine?tipo={self.tipo.currentText()}&fixed={self.fixed.text()}&volatile={self.volatile.text()}&citric={self.citric.text()}&residual={self.residual.text()}&chlorides={self.chlorides.text()}&freesulfur={self.freesulfur.text()}&totalsulfur={self.totalsulfur.text()}&density={self.density.text()}&ph={self.ph.text()}&sulphates={self.sulphates.text()}&alcohol={self.alcohol.text()}"
        response = requests.get(request_url)
        self.pbar.setValue(60)
        try:
            Wine_Type = response.json()["Wine_Type"]
            self.response.setText(f"<h2>This Wine is a {Wine_Type}</h2>")
            self.pbar.setValue(70)
        except:
            self.response.setText(f'API Error - Server Offline')
        self.pbar.setValue(100)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QtGui.QIcon('winealt.ico'))

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


