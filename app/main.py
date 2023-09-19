# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication
from app.ui.main_window import MainWindow

from app.ui.icon_rc import *

__author__ = 'InG_byr'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    font = app.font()
    font.setPointSize(11)
    app.setFont(font)
    ui = MainWindow()
    ui.main_window.show()
    sys.exit(app.exec_())
