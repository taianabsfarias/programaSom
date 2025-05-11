

import sys
import os

from qtcore import *

from graf.windows.mainwin.uiMainWin import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        self.show()


if __name__ == "__main__":
   
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())