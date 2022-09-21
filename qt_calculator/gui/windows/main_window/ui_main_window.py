from qt_calculator.qt_core import *


class UiMainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

        # Initial Parameters
        # sets Main Window in main.py as 1200x720 when initialize
        parent.resize(
            1200, 720
        )
        parent.setMinimumSize(960, 540)  # sets Main Window minimum size

        # Create Central Widget
        self.central_frame = (
            QFrame()  # creates the widget to put widgets on it
        )

        # Create Main Layout
        # Creates a layout that has no borders and no
        # spacing between widgets insidethe central_frame
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left Menu
        # Creates the left menu with 50 pixels
        # width and the background color for it
        self.left_menu = QFrame()
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setStyleSheet('background-color: #44475a')

        # Content
        # Creates the widget that will be the
        # content of our Main Window
        self.content = QFrame()
        self.content.setStyleSheet('background-color: #282a36')

        # Add Widgets to app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET Central Widget
        parent.setCentralWidget(self.central_frame)
