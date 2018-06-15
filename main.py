#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from Login import LoginForm

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LoginForm()              #载入登录界面
    main.show()
    sys.exit(app.exec_())