import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.hello)

    def hello(self):
        text = self.ui.name_line_edit.text()
        if text == "":
            text = "Oo"
        self.ui.otput_hello_label.setText(f'Привет, {text}!!!')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
