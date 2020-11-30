from QuickMLMain.Model.GUI import Model
from PyQt5 import QtWidgets
from QuickMLMain import preprocessingGUI, testingGUI

def showModelGUI():
    MainWindow1.close()
    MainWindow2.show()

def showTestingGUI():
    MainWindow2.close()
    MainWindow3.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui1 = preprocessingGUI.Ui_MainWindow()
    ui1.setupUi(MainWindow1)
    ui1.nextBtn.clicked.connect(lambda: showModelGUI())
    MainWindow1.show()

    MainWindow2 = QtWidgets.QMainWindow()
    ui2 = Model.Ui_MainWindow()
    ui2.setupUi(MainWindow2)
    ui2.NextButton.clicked.connect(lambda: showTestingGUI())

    MainWindow3 = QtWidgets.QMainWindow()
    ui3 = testingGUI.Ui_MainWindow()
    ui3.setupUi(MainWindow3)


    sys.exit(app.exec_())