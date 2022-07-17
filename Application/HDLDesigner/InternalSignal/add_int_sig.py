from xml.dom import minidom
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
sys.path.append("..")
from ProjectManager.project_manager import ProjectManager

BLACK_COLOR = "color: black"
WHITE_COLOR = "color: white"

class AddIntSignal(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Internal Signal")
        title_font = QFont()
        title_font.setPointSize(10)
        title_font.setBold(True)
        bold_font = QFont()
        bold_font.setBold(True)

        self.input_signals = []
        self.output_signals = []

        self.input_layout = QGridLayout()

        self.mainLayout = QVBoxLayout()

        self.intSig_name_label = QLabel("Internal Signal Name*")
        self.intSig_name_label.setStyleSheet(WHITE_COLOR)
        self.intSig_name_input = QLineEdit()

        self.sig_type_label = QLabel("Signal Type")
        self.sig_type_label.setStyleSheet(WHITE_COLOR)
        self.sig_type_combo = QComboBox()
        self.sig_type_combo.setFixedWidth(150)

        self.sig_desc_label = QLabel("Signal Description")
        self.sig_desc_label.setStyleSheet(WHITE_COLOR)
        self.sig_desc_input = QLineEdit()

        self.sig_layout = QHBoxLayout()


        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setFixedSize(60, 25)
        self.cancel_btn.setStyleSheet(
            "QPushButton {background-color: white; color: black; border-radius: 8px; border-style: plain; }"
            " QPushButton:pressed { background-color: rgb(250, 250, 250);  color: black; border-radius: 8px; border-style: plain;}")


        self.ok_btn = QPushButton("Ok")
        self.ok_btn.setEnabled(False)
        self.ok_btn.setFixedSize(60, 25)
        self.ok_btn.setStyleSheet(
            "QPushButton {background-color: rgb(169,169,169);  color: black; border-radius: 8px; border-style: plain;}"
            " QPushButton:pressed { background-color: rgb(250, 250, 250);  color: black; border-radius: 8px; border-style: plain;}"
            "QPushButton:enabled {background-color: white; color: black; border-radius: 8px; border-style: plain; }")

        self.input_frame = QFrame()

        self.cancelled = True

        self.setup_ui()

        # self.populate_signals(ProjectManager.get_xml_data_path())

    def setup_ui(self):

        self.input_layout.addWidget(self.intSig_name_label, 0, 0, 1, 1)
        self.input_layout.addWidget(self.intSig_name_input, 1, 0, 1, 4)
        self.input_layout.addWidget(self.sig_type_label, 0, 4, 1, 1)
        self.input_layout.addWidget(self.sig_type_combo, 1, 4, 1, 2)
        self.input_layout.addWidget(self.sig_desc_label, 2, 0, 1, 1)
        self.input_layout.addWidget(self.sig_desc_input, 3, 0, 1, 6)
        self.input_layout.addItem(QSpacerItem(0, 10), 4, 0, 1, 3)
        self.input_layout.addWidget(self.cancel_btn, 5, 4, 1, 1, alignment=Qt.AlignRight)
        self.input_layout.addWidget(self.ok_btn, 5, 5, 1, 1, alignment=Qt.AlignRight)

        self.intSig_name_input.textChanged.connect(self.enable_ok_btn);
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setStyleSheet('.QFrame{background-color: rgb(97, 107, 129); border-radius: 5px;}')
        self.input_frame.setContentsMargins(10, 10, 10, 10)
        self.input_frame.setFixedSize(400, 175)
        self.input_frame.setLayout(self.input_layout)

        # self.ok_btn.clicked.connect(self.get_data)
        self.cancel_btn.clicked.connect(self.cancel_selected)

        self.mainLayout.addWidget(self.input_frame, alignment=Qt.AlignCenter)

        self.setLayout(self.mainLayout)

    def cancel_selected(self):
        self.cancelled = True
        self.close()

    def enable_ok_btn(self):
        if self.intSig_name_input.text() != "":
            self.ok_btn.setEnabled(True)
        else:
            self.ok_btn.setEnabled(False)