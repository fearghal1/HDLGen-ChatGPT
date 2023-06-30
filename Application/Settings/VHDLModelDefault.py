from PySide2.QtWidgets import *
from PySide2.QtGui import *
import configparser

BLACK_COLOR = "color: black"
WHITE_COLOR = "color: white"

class VHDLModelDefaultDialog(QDialog):

    def __init__(self, add_or_edit, data=None):
        super().__init__()

        self.setWindowTitle("ChatGPT VHDL Model Default Command")
        title_font = QFont()
        title_font.setPointSize(10)
        title_font.setBold(True)
        bold_font = QFont()
        bold_font.setBold(True)

        self.input_layout = QGridLayout()
        self.mainLayout = QVBoxLayout()

        self.ChatGPT_model_label = QLabel("ChatGPT Model Commands")
        self.ChatGPT_model_label.setStyleSheet(WHITE_COLOR)
        self.ChatGPT_model_input = QPlainTextEdit()
        self.ChatGPT_model_input.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.ChatGPT_default_label = QLabel("ChatGPT Default Command Copy this text to above")
        self.ChatGPT_default_label.setStyleSheet(WHITE_COLOR)
        self.ChatGPT_default_input = QPlainTextEdit()
        self.ChatGPT_default_input.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setFixedSize(60, 25)
        self.reset_btn.setStyleSheet(
            "QPushButton {background-color: white; color: black; border-radius: 8px; border-style: plain; }"
            " QPushButton:pressed { background-color: rgb(250, 250, 250);  color: black; border-radius: 8px; border-style: plain;}")

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setFixedSize(60, 25)
        self.cancel_btn.setStyleSheet(
            "QPushButton {background-color: white; color: black; border-radius: 8px; border-style: plain; }"
            " QPushButton:pressed { background-color: rgb(250, 250, 250);  color: black; border-radius: 8px; border-style: plain;}")


        self.ok_btn = QPushButton("Ok")
        self.ok_btn.setFixedSize(60, 25)
        self.ok_btn.setStyleSheet(
            "QPushButton {background-color: rgb(169,169,169);  color: black; border-radius: 8px; border-style: plain;}"
            " QPushButton:pressed { background-color: rgb(250, 250, 250);  color: black; border-radius: 8px; border-style: plain;}"
            "QPushButton:enabled {background-color: white; color: black; border-radius: 8px; border-style: plain; }")
        self.input_frame = QFrame()

        self.cancelled = True
        self.config = configparser.ConfigParser()

        self.setup_ui()
        if add_or_edit == "edit" and data != None:
            self.ChatGPT_default_input.setPlainText(data)

    def setup_ui(self):
        self.input_layout.addWidget(self.ChatGPT_default_label, 0, 0, 1, 4)
        self.input_layout.addWidget(self.ChatGPT_default_input, 1, 0, 4, 4)

        self.input_layout.addWidget(self.reset_btn, 6, 1, 1, 1, alignment=Qt.AlignRight)
        self.input_layout.addWidget(self.cancel_btn, 6, 2, 1, 1, alignment=Qt.AlignRight)
        self.input_layout.addWidget(self.ok_btn, 6, 3, 1, 1, alignment=Qt.AlignRight)
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setStyleSheet('.QFrame{background-color: rgb(97, 107, 129); border-radius: 5px;}')
        self.input_frame.setContentsMargins(10, 10, 10, 10)
        self.input_frame.setFixedSize(600, 600)
        self.input_frame.setLayout(self.input_layout)
        self.cancel_btn.clicked.connect(self.cancel_selected)

        self.mainLayout.addWidget(self.input_frame, alignment=Qt.AlignCenter)

        self.setLayout(self.mainLayout)
        self.reset_btn.clicked.connect(self.reset)
        self.ok_btn.clicked.connect(self.get_data)

    def cancel_selected(self):
        self.cancelled = True
        self.close()

    def get_data(self):
        data = self.ChatGPT_default_input.toPlainText().strip()
        if data == "":
            data = "None"
        self.cancelled = False
        self.close()
        return data

    def reset(self):
        self.ChatGPT_default_input.setPlainText("This text includes ChatGPT commands which have been found useful for generating VHDL models in a series of projects. Copy, paste, edit in the top text box as required.	\n=== Optional ChatCPT messages for VHDL model development, which can be submitted sequentially after the ChatGPT run === \nKeep the '-- Default assignment' text on the same line as the original assignment, unchanged, and immediately before the VHDL logic generated for lines containing prefix '---'\nPlace the VHDL process line containing '-- Default assignment', unchanged, and immediately before the VHDL logic generated for lines containing prefix '---'\nFor all assignments which include arithmetic operators '+', '-', '*', '/', in processes or concurrent statements, use 'ieee.numeric_std' package signal type conversion functions\nDo not output the lines containing prefix '---'\n\n=== Default ChatGPT message header set for VHDL model development === Excluding this line\nComplete the following VHDL model, and output in a code box\nDo not include any assignment when-else VHDL constructs (conditional VHDL) inside process VHDL code (only supported in ieee 1076-2008)\nDo not add any new library 'use' statements, to avoid conflicts with the ieee.numeric_std package functions\nFor each line containing the prefix '---', replace with generated VHDL code for the logic described, and remove the '---'\nFor all assignments which include arithmetic operators '+' or '-', in processes or concurrent statements, use 'ieee.numeric_std' package signal type conversion functions\nFor all assignments which include a shift operation, only use ieee.numeric_std package shift_left or shift_right functions, and do not use sra, srl, sll functions.\nIn VHDL processes, place the modified line containing suffix '-- Default assignment' immediately before the VHDL statements generated for lines containing prefix '---'\nDo not include any assignments which duplicate the signal assignment values, for assignments labelled '-- Default assignment'\nLeave all labels unchanged")