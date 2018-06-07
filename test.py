#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from  Register import RegisterForm
from Owner import OwnerForm

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = OwnerForm('11')
    main.show()
    sys.exit(app.exec_())