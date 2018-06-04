#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from Admin import AdminForm

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AdminForm()
    main.show()
    sys.exit(app.exec_())