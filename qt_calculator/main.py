import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self._window_settings()

    def _window_settings(self) -> None:
        self.setWindowTitle('Qt Calculator')
        self.setWindowIcon(QtGui.QIcon('icons/calculator.png'))
        self.setMinimumSize(310, 340)


def main() -> None:
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
