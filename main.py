"""
BY: Edson Pimenta
PROJECT MADE WITH: Python, Qt, PyQT6
V: 0.1.0
"""
import sys

# Import Main Window
from gui.windows.main_window.ui_main_window import *
from qt_core import *


# Main Window
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Title and Icon
        self.setWindowTitle('Qt Calculator')
        self.setWindowIcon(QIcon('icons/calculator.png'))

        # Main Window setup (ui_main_window)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Btn home / std calc
        self.ui.std_calc_button.clicked.connect(self.show_page_1)

        # Btn sci / scientific calc
        self.ui.sci_calc_button.clicked.connect(self.show_page_2)

        # Btn config
        self.ui.settings_btn.clicked.connect(self.show_page_3)

        # Show Aplication
        self.show()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.standard_calc)
        self.ui.std_calc_button.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.scientific_calc)
        self.ui.sci_calc_button.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.config)
        self.ui.settings_btn.set_active(True)

    def toggle_button(self):
        # get menu width
        menu_width = self.ui.left_menu.width()

        # check menu width
        width = 50
        if menu_width == 50:
            width = 100

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b'minimumWidth')
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(250)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
