from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from ui.base_qt_ui.ui_mainwindow import Ui_MainWindow
from ui.coordwidget import CoordWidget
from ui.flowlayout import FlowLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0

        self.flowlayout = FlowLayout()
        self.ui.coordwidget_layout.addLayout(self.flowlayout)
        self.ui.add_pushbutton.clicked.connect(self.add_coordwidget)
        self.ui.clear_pushbutton.clicked.connect(self.clear_area)

    @Slot()
    def add_coordwidget(self):
        self.counter_id += 1
        coord_widget = CoordWidget(self.counter_id)
        self.flowlayout.addWidget(coord_widget)
        coord_widget.delete.connect(self.delete_coordwidget)

    @Slot()
    def clear_area(self):
        while self.flowlayout.count() > 0:
            item = self.flowlayout.takeAt(0)
            item.widget().deleteLater()

    @Slot(int)
    def delete_coordwidget(self, wid: int):
        print(f'Удаляем виджет с id: {wid}')
        widget = self.sender()
        self.flowlayout.removeWidget(widget)
        widget.deleteLater()

