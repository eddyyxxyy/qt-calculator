# -*- coding: utf-8 -*-
from qt_core import *


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName('StackedWidget')
        StackedWidget.resize(373, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            StackedWidget.sizePolicy().hasHeightForWidth()
        )
        StackedWidget.setSizePolicy(sizePolicy)
        StackedWidget.setMinimumSize(QSize(298, 306))
        StackedWidget.setFrameShadow(QFrame.Plain)
        self.standard_calc = QWidget()
        self.standard_calc.setObjectName('standard_calc')
        self.gridLayout = QGridLayout(self.standard_calc)
        self.gridLayout.setObjectName('gridLayout')
        self.sqrt_button = QPushButton(self.standard_calc)
        self.sqrt_button.setObjectName('sqrt_button')
        sizePolicy1 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.sqrt_button.sizePolicy().hasHeightForWidth()
        )
        self.sqrt_button.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        self.sqrt_button.setFont(font)

        self.gridLayout.addWidget(self.sqrt_button, 3, 2, 1, 1)

        self.seven_button = QPushButton(self.standard_calc)
        self.seven_button.setObjectName('seven_button')
        sizePolicy1.setHeightForWidth(
            self.seven_button.sizePolicy().hasHeightForWidth()
        )
        self.seven_button.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.seven_button.setFont(font1)

        self.gridLayout.addWidget(self.seven_button, 4, 0, 1, 1)

        self.divided_by_x_button = QPushButton(self.standard_calc)
        self.divided_by_x_button.setObjectName('divided_by_x_button')
        sizePolicy1.setHeightForWidth(
            self.divided_by_x_button.sizePolicy().hasHeightForWidth()
        )
        self.divided_by_x_button.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(30)
        self.divided_by_x_button.setFont(font2)

        self.gridLayout.addWidget(self.divided_by_x_button, 3, 0, 1, 1)

        self.four_button = QPushButton(self.standard_calc)
        self.four_button.setObjectName('four_button')
        sizePolicy1.setHeightForWidth(
            self.four_button.sizePolicy().hasHeightForWidth()
        )
        self.four_button.setSizePolicy(sizePolicy1)
        self.four_button.setFont(font1)

        self.gridLayout.addWidget(self.four_button, 5, 0, 1, 1)

        self.backspace_button = QPushButton(self.standard_calc)
        self.backspace_button.setObjectName('backspace_button')
        sizePolicy1.setHeightForWidth(
            self.backspace_button.sizePolicy().hasHeightForWidth()
        )
        self.backspace_button.setSizePolicy(sizePolicy1)
        self.backspace_button.setFont(font1)

        self.gridLayout.addWidget(self.backspace_button, 2, 3, 1, 1)

        self.division_button = QPushButton(self.standard_calc)
        self.division_button.setObjectName('division_button')
        sizePolicy1.setHeightForWidth(
            self.division_button.sizePolicy().hasHeightForWidth()
        )
        self.division_button.setSizePolicy(sizePolicy1)
        self.division_button.setFont(font2)

        self.gridLayout.addWidget(self.division_button, 3, 3, 1, 1)

        self.percent_button = QPushButton(self.standard_calc)
        self.percent_button.setObjectName('percent_button')
        sizePolicy1.setHeightForWidth(
            self.percent_button.sizePolicy().hasHeightForWidth()
        )
        self.percent_button.setSizePolicy(sizePolicy1)
        self.percent_button.setFont(font2)

        self.gridLayout.addWidget(self.percent_button, 2, 0, 1, 1)

        self.plus_button = QPushButton(self.standard_calc)
        self.plus_button.setObjectName('plus_button')
        sizePolicy1.setHeightForWidth(
            self.plus_button.sizePolicy().hasHeightForWidth()
        )
        self.plus_button.setSizePolicy(sizePolicy1)
        self.plus_button.setFont(font2)

        self.gridLayout.addWidget(self.plus_button, 6, 3, 1, 1)

        self.six_button = QPushButton(self.standard_calc)
        self.six_button.setObjectName('six_button')
        sizePolicy1.setHeightForWidth(
            self.six_button.sizePolicy().hasHeightForWidth()
        )
        self.six_button.setSizePolicy(sizePolicy1)
        self.six_button.setFont(font1)

        self.gridLayout.addWidget(self.six_button, 5, 2, 1, 1)

        self.c_button = QPushButton(self.standard_calc)
        self.c_button.setObjectName('c_button')
        sizePolicy1.setHeightForWidth(
            self.c_button.sizePolicy().hasHeightForWidth()
        )
        self.c_button.setSizePolicy(sizePolicy1)
        self.c_button.setMinimumSize(QSize(0, 0))
        self.c_button.setFont(font1)

        self.gridLayout.addWidget(self.c_button, 2, 2, 1, 1)

        self.two_button = QPushButton(self.standard_calc)
        self.two_button.setObjectName('two_button')
        sizePolicy1.setHeightForWidth(
            self.two_button.sizePolicy().hasHeightForWidth()
        )
        self.two_button.setSizePolicy(sizePolicy1)
        self.two_button.setFont(font1)

        self.gridLayout.addWidget(self.two_button, 6, 1, 1, 1)

        self.minus_button = QPushButton(self.standard_calc)
        self.minus_button.setObjectName('minus_button')
        sizePolicy1.setHeightForWidth(
            self.minus_button.sizePolicy().hasHeightForWidth()
        )
        self.minus_button.setSizePolicy(sizePolicy1)
        self.minus_button.setFont(font2)

        self.gridLayout.addWidget(self.minus_button, 5, 3, 1, 1)

        self.nine_button = QPushButton(self.standard_calc)
        self.nine_button.setObjectName('nine_button')
        sizePolicy1.setHeightForWidth(
            self.nine_button.sizePolicy().hasHeightForWidth()
        )
        self.nine_button.setSizePolicy(sizePolicy1)
        self.nine_button.setFont(font1)

        self.gridLayout.addWidget(self.nine_button, 4, 2, 1, 1)

        self.comma_button = QPushButton(self.standard_calc)
        self.comma_button.setObjectName('comma_button')
        sizePolicy1.setHeightForWidth(
            self.comma_button.sizePolicy().hasHeightForWidth()
        )
        self.comma_button.setSizePolicy(sizePolicy1)
        self.comma_button.setFont(font2)

        self.gridLayout.addWidget(self.comma_button, 7, 2, 1, 1)

        self.plus_minus_button = QPushButton(self.standard_calc)
        self.plus_minus_button.setObjectName('plus_minus_button')
        sizePolicy1.setHeightForWidth(
            self.plus_minus_button.sizePolicy().hasHeightForWidth()
        )
        self.plus_minus_button.setSizePolicy(sizePolicy1)
        self.plus_minus_button.setFont(font2)

        self.gridLayout.addWidget(self.plus_minus_button, 7, 0, 1, 1)

        self.eight_button = QPushButton(self.standard_calc)
        self.eight_button.setObjectName('eight_button')
        sizePolicy1.setHeightForWidth(
            self.eight_button.sizePolicy().hasHeightForWidth()
        )
        self.eight_button.setSizePolicy(sizePolicy1)
        self.eight_button.setFont(font1)

        self.gridLayout.addWidget(self.eight_button, 4, 1, 1, 1)

        self.ce_button = QPushButton(self.standard_calc)
        self.ce_button.setObjectName('ce_button')
        sizePolicy1.setHeightForWidth(
            self.ce_button.sizePolicy().hasHeightForWidth()
        )
        self.ce_button.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setKerning(True)
        self.ce_button.setFont(font3)

        self.gridLayout.addWidget(self.ce_button, 2, 1, 1, 1)

        self.three_button = QPushButton(self.standard_calc)
        self.three_button.setObjectName('three_button')
        sizePolicy1.setHeightForWidth(
            self.three_button.sizePolicy().hasHeightForWidth()
        )
        self.three_button.setSizePolicy(sizePolicy1)
        self.three_button.setFont(font1)

        self.gridLayout.addWidget(self.three_button, 6, 2, 1, 1)

        self.one_button = QPushButton(self.standard_calc)
        self.one_button.setObjectName('one_button')
        sizePolicy1.setHeightForWidth(
            self.one_button.sizePolicy().hasHeightForWidth()
        )
        self.one_button.setSizePolicy(sizePolicy1)
        self.one_button.setFont(font1)

        self.gridLayout.addWidget(self.one_button, 6, 0, 1, 1)

        self.zero_button = QPushButton(self.standard_calc)
        self.zero_button.setObjectName('zero_button')
        sizePolicy1.setHeightForWidth(
            self.zero_button.sizePolicy().hasHeightForWidth()
        )
        self.zero_button.setSizePolicy(sizePolicy1)
        self.zero_button.setFont(font1)

        self.gridLayout.addWidget(self.zero_button, 7, 1, 1, 1)

        self.mul_button = QPushButton(self.standard_calc)
        self.mul_button.setObjectName('mul_button')
        sizePolicy1.setHeightForWidth(
            self.mul_button.sizePolicy().hasHeightForWidth()
        )
        self.mul_button.setSizePolicy(sizePolicy1)
        self.mul_button.setFont(font2)

        self.gridLayout.addWidget(self.mul_button, 4, 3, 1, 1)

        self.equal_button = QPushButton(self.standard_calc)
        self.equal_button.setObjectName('equal_button')
        sizePolicy1.setHeightForWidth(
            self.equal_button.sizePolicy().hasHeightForWidth()
        )
        self.equal_button.setSizePolicy(sizePolicy1)
        self.equal_button.setFont(font1)

        self.gridLayout.addWidget(self.equal_button, 7, 3, 1, 1)

        self.five__button = QPushButton(self.standard_calc)
        self.five__button.setObjectName('five__button')
        sizePolicy1.setHeightForWidth(
            self.five__button.sizePolicy().hasHeightForWidth()
        )
        self.five__button.setSizePolicy(sizePolicy1)
        self.five__button.setFont(font1)

        self.gridLayout.addWidget(self.five__button, 5, 1, 1, 1)

        self.sqr_button = QPushButton(self.standard_calc)
        self.sqr_button.setObjectName('sqr_button')
        sizePolicy1.setHeightForWidth(
            self.sqr_button.sizePolicy().hasHeightForWidth()
        )
        self.sqr_button.setSizePolicy(sizePolicy1)
        self.sqr_button.setFont(font2)

        self.gridLayout.addWidget(self.sqr_button, 3, 1, 1, 1)

        self.std_calc_output = QLabel(self.standard_calc)
        self.std_calc_output.setObjectName('std_calc_output')
        sizePolicy1.setHeightForWidth(
            self.std_calc_output.sizePolicy().hasHeightForWidth()
        )
        self.std_calc_output.setSizePolicy(sizePolicy1)
        self.std_calc_output.setMinimumSize(QSize(0, 150))
        self.std_calc_output.setSizeIncrement(QSize(20, 0))
        font4 = QFont()
        font4.setPointSize(35)
        font4.setBold(True)
        self.std_calc_output.setFont(font4)
        self.std_calc_output.setAutoFillBackground(False)
        self.std_calc_output.setFrameShape(QFrame.Box)
        self.std_calc_output.setFrameShadow(QFrame.Raised)
        self.std_calc_output.setScaledContents(True)
        self.std_calc_output.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.std_calc_output.setMargin(10)

        self.gridLayout.addWidget(self.std_calc_output, 1, 0, 1, 4)

        StackedWidget.addWidget(self.standard_calc)

        self.scientific_calc = QWidget()
        self.scientific_calc.setObjectName('scientific_calc')
        self.verticalLayout = QVBoxLayout(self.scientific_calc)
        self.verticalLayout.setObjectName('verticalLayout')
        self.label_2 = QLabel(self.scientific_calc)
        self.label_2.setObjectName('label_2')
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        StackedWidget.addWidget(self.scientific_calc)
        self.config = QWidget()
        self.config.setObjectName('config')
        self.verticalLayout_2 = QVBoxLayout(self.config)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.label = QLabel(self.config)
        self.label.setObjectName('label')
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        StackedWidget.addWidget(self.config)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(StackedWidget)

    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(
            QCoreApplication.translate('StackedWidget', 'StackedWidget', None)
        )
        self.sqrt_button.setText(
            QCoreApplication.translate('StackedWidget', '²√x', None)
        )
        self.seven_button.setText(
            QCoreApplication.translate('StackedWidget', '7', None)
        )
        self.divided_by_x_button.setText(
            QCoreApplication.translate('StackedWidget', '1/x', None)
        )
        self.four_button.setText(
            QCoreApplication.translate('StackedWidget', '4', None)
        )
        self.backspace_button.setText(
            QCoreApplication.translate('StackedWidget', '<', None)
        )
        self.division_button.setText(
            QCoreApplication.translate('StackedWidget', '/', None)
        )
        self.percent_button.setText(
            QCoreApplication.translate('StackedWidget', '%', None)
        )
        self.plus_button.setText(
            QCoreApplication.translate('StackedWidget', '+', None)
        )
        self.six_button.setText(
            QCoreApplication.translate('StackedWidget', '6', None)
        )
        self.c_button.setText(
            QCoreApplication.translate('StackedWidget', 'C', None)
        )
        self.two_button.setText(
            QCoreApplication.translate('StackedWidget', '2', None)
        )
        self.minus_button.setText(
            QCoreApplication.translate('StackedWidget', '-', None)
        )
        self.nine_button.setText(
            QCoreApplication.translate('StackedWidget', '9', None)
        )
        self.comma_button.setText(
            QCoreApplication.translate('StackedWidget', ',', None)
        )
        self.plus_minus_button.setText(
            QCoreApplication.translate('StackedWidget', '+/-', None)
        )
        self.eight_button.setText(
            QCoreApplication.translate('StackedWidget', '8', None)
        )
        self.ce_button.setText(
            QCoreApplication.translate('StackedWidget', 'CE', None)
        )
        self.three_button.setText(
            QCoreApplication.translate('StackedWidget', '3', None)
        )
        self.one_button.setText(
            QCoreApplication.translate('StackedWidget', '1', None)
        )
        self.zero_button.setText(
            QCoreApplication.translate('StackedWidget', '0', None)
        )
        self.mul_button.setText(
            QCoreApplication.translate('StackedWidget', 'X', None)
        )
        self.equal_button.setText(
            QCoreApplication.translate('StackedWidget', '=', None)
        )
        self.five__button.setText(
            QCoreApplication.translate('StackedWidget', '5', None)
        )
        self.sqr_button.setText(
            QCoreApplication.translate('StackedWidget', 'x\u00b2', None)
        )
        self.std_calc_output.setText(
            QCoreApplication.translate('StackedWidget', '0', None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                'StackedWidget', 'Scientific Calculator', None
            )
        )
        self.label.setText(
            QCoreApplication.translate('StackedWidget', 'config', None)
        )

    # retranslateUi
