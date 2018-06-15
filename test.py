
import sys
from Admin import AdminForm
from  Register import RegisterForm
from Owner import OwnerForm
from eRepresentative import eRepresentativeForm
from wRepresentative import wRepresentativeForm

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main =wRepresentativeForm()
    main.show()
    sys.exit(app.exec_())