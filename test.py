#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from Admin import AdminForm
from  Register import RegisterForm
from Owner import OwnerForm
from Representative import RepresentativeForm

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = RepresentativeForm()
    main.show()
    sys.exit(app.exec_())