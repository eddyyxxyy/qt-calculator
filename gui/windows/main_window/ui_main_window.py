"""
BY: Edson Pimenta
PROJECT MADE WITH: Python, Pyside6
V: 0.1.2
"""
# Import pages
from gui.pages.ui_pages import Ui_StackedWidget
from gui.widgets.py_push_button import PyPushButton
from qt_core import *


class UiMainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

        # Initial Parameters
        # sets Main Window in main.py when initialize
        # //////////////////////////////////////////////////////////////
        parent.resize(436, 614)
        parent.setMinimumSize(436, 614)  # sets Main Window minimum size

        # Create Central Widget
        self.central_frame = (
            QFrame()  # creates the widget to put widgets on it
        )

        # Create Main Layout
        # Creates a layout that has no borders and no
        # spacing between widgets insidethe central_frame
        # //////////////////////////////////////////////////////////////
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left Menu
        # Creates the left menu with 50 pixels
        # width and the background color for it
        # //////////////////////////////////////////////////////////////
        self.left_menu = QFrame()
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        self.left_menu.setStyleSheet('background-color: #44475a')

        # Left Menu layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Top Left Frame Menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName('left_menu_top_frame')

        # Top Frame Layout
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # Top buttons
        self.toggle_button = PyPushButton(
            text='Menu', icon_path='icon_menu.svg'
        )
        self.std_calc_button = PyPushButton(
            text='Std', is_active=True, icon_path='icon_stdcalc.svg'
        )
        self.sci_calc_button = PyPushButton(
            text='Sci', icon_path='icon_scicalc.svg'
        )

        # Add buttons to Top Frame Layout
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.std_calc_button)
        self.left_menu_top_layout.addWidget(self.sci_calc_button)

        # Left Menu spacer
        # //////////////////////////////////////////////////////////////
        self.left_menu_spacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        # Botton Left Menu Frame
        # //////////////////////////////////////////////////////////////
        self.left_menu_botton_frame = QFrame()
        self.left_menu_botton_frame.setMinimumHeight(40)
        self.left_menu_botton_frame.setObjectName('left_menu_botton_frame')

        # Bottom Left Menu Frame Layout
        self.left_menu_botton_layout = QVBoxLayout(self.left_menu_botton_frame)
        self.left_menu_botton_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_botton_layout.setSpacing(0)

        # Bottom buttons
        self.settings_btn = PyPushButton(
            text='Config', icon_path='icon_settings.svg'
        )

        # Add to bottom left menu frame layout
        self.left_menu_botton_layout.addWidget(self.settings_btn)

        # Botton label Left Menu
        self.left_menu_label_version = QLabel('v1.0.0')
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet('color: #c3ccdf')

        # Content
        # Creates the widget that will be the
        # content of our Main Window
        # //////////////////////////////////////////////////////////////
        self.content = QFrame()
        self.content.setStyleSheet('background-color: #282a36')

        # Top bar
        # It's always good to set a min/max
        # height to these kind of widgets,
        # we don't want the layout to 'break'
        # when we resize the window
        # //////////////////////////////////////////////////////////////
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet('background-color: #21232d; color: #6272a4')
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Top bar left label
        self.top_bar_label_left = QLabel('')

        # Top bar spacer
        self.top_bar_spacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        # Top bar right label
        self.top_bar_label_right = QLabel('| QT Calculator')
        self.top_bar_label_right.setStyleSheet('font: 700 9pt "Segoe UI"')

        # Add to top bar layout
        self.top_bar_layout.addWidget(self.top_bar_label_left)
        self.top_bar_layout.addItem(self.top_bar_spacer)
        self.top_bar_layout.addWidget(self.top_bar_label_right)

        # Application pages
        # //////////////////////////////////////////////////////////////
        self.pages = QStackedWidget()
        self.pages.setStyleSheet('font-size: 12pt; color: #f8f8f2')
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.standard_calc)

        # Content Layout
        # //////////////////////////////////////////////////////////////
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Botton bar
        # //////////////////////////////////////////////////////////////
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet(
            'background-color: #21232d; color: #6272a4'
        )
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Bottom bar left label
        self.bottom_bar_label_left = QLabel(
            'Criado por: Edson Pimenta / eeddyyxxyy'
        )

        # Bottom bar spacer
        self.bottom_bar_spacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        # Bottom bar right label
        self.bottom_bar_label_right = QLabel('© 2022')

        # Add to left menu
        # //////////////////////////////////////////////////////////////
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_botton_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # Add to bottom bar layout
        # //////////////////////////////////////////////////////////////
        self.bottom_bar_layout.addWidget(self.bottom_bar_label_left)
        self.bottom_bar_layout.addItem(self.bottom_bar_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_bar_label_right)

        # Add widgets to content layout
        # //////////////////////////////////////////////////////////////
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Add Widgets to app
        # //////////////////////////////////////////////////////////////
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET Central Widget
        # //////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_frame)
