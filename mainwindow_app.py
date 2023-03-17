# -*- coding: utf-8 -*-


from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QFileDialog
from PySide6.QtCore import Qt

# from PySide6.QtWidgets import *
from form_demo import Ui_Formdemo
from demo_main import main

class MyWindow(QMainWindow, Ui_Formdemo):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)

        # self.pushButton.clicked.connect(self.hello)
        self.btntest.clicked.connect(self.select_file_mech)
        self.pushButton.clicked.connect(self.select_file_geskon)
        self.pushButton_2.clicked.connect(self.select_file_dcm)
        self.pushButton_3.clicked.connect(self.select_file_a2l)
        self.pushButton_4.clicked.connect(self.select_file_data)
        self.pushButton_5.clicked.connect(self.work)



    def hello(self):
        print("hello")

    def select_file_mech(self):
        file_path_mech, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_mech:
            # self.file_path_label.setText(file_path_mech)
            self.lineEdit.setText(file_path_mech)
            # self.compute_button.setEnabled(True)
            self.file_mech_table = file_path_mech
            print(self.file_mech_table)
        return self.file_mech_table

    def select_file_geskon(self):
        file_path_geskon, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_geskon:
            self.lineEdit_2.setText(file_path_geskon)
            self.file_geskon = file_path_geskon
            print(self.file_geskon)
        return self.file_geskon

    def select_file_dcm(self):
        file_path_dcm, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_dcm:
            self.lineEdit_3.setText(file_path_dcm)
            self.file_dcm = file_path_dcm
            print(self.file_dcm)
        return self.file_dcm

    def select_file_a2l(self):
        file_path_a2l, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_a2l:
            self.lineEdit_4.setText(file_path_a2l)
            self.file_a2l = file_path_a2l
            print(self.file_a2l)
        return self.file_a2l

    def select_file_data(self):
        file_path_data, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_data:
            self.lineEdit_5.setText(file_path_data)
            self.file_data_mytable = file_path_data
            print(self.file_data_mytable)
        return self.file_data_mytable

    def work(self):
        print(self.file_data_mytable)
        # main_data_query(self.file_data_mytable)

    def getfile(self):
        global file_a2l
        global file_geskon
        global file_dcm
        global file_data_mytable
        global file_mech_table
        file_a2l = self.file_a2l
        file_geskon = self.file_geskon
        file_dcm = self.file_dcm
        file_data_mytable = self.file_data_mytable
        file_mech_table = self.file_mech_table
        return file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()