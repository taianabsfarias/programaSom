

from qtcore import *

class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #D4E2F0")


        self.main_layout = QHBoxLayout(self.central_frame)

        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #C8CCD1")

        self.content = QFrame()
        self.content.setStyleSheet("background-color: #C8CCD1")

        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        parent.setCentralWidget(self.central_frame)