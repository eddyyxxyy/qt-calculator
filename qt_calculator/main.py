import os
import sys

# Import Main Window
from gui.windows.main_window.ui_main_window import *

from qt_core import *


# Main Window
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Main Window setup (ui_main_window)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # Show Aplication
        self.show()


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
