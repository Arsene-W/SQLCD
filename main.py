#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from Login import LoginForm

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LoginForm()
    main.show()
    sys.exit(app.exec_())