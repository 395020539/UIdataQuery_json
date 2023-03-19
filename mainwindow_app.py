# -*- coding: utf-8 -*-

import time



from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QFileDialog,QMessageBox, QMenu,QTextBrowser,QVBoxLayout
from PySide6.QtCore import Qt, QObject, Signal, QThread, Slot,QRect
from PySide6.QtGui import QAction


from form_demo import Ui_Formdemo

file_a2l = ""
file_geskon = ""
file_dcm = ""
file_data_mytable = ""
file_mech_table = ""


class MyTask(QObject):
    started = Signal()
    finished = Signal()

    def run(self):
        from logging_maker import logger
        from demo_main import main_data_query
        # 发出 started 信号以通知 UI 线程
        self.started.emit()

        t_start = time.perf_counter()
        # 在这里执行你的任务代码
        # time.sleep(5)
        # t_start = time.perf_counter()

        main_data_query(file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table)

        t_end = time.perf_counter()
        t_cost = t_end - t_start
        print(f'运行耗时:{t_cost:.8f}s')
        logger.info(f'运行耗时:{t_cost:.8f}s')
        logger.info(f'进程结束')
        # 任务完成后发出 finished 信号
        self.finished.emit()


class MyWindow(QMainWindow, Ui_Formdemo):

    def __init__(self):
        super().__init__()

        self.task = None
        self.setupUi(self)
        self.retranslateUi(self)

        # 创建 QThread 对象
        self.worker = MyTask()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()

        # 连接任务的 started 信号到槽函数，禁用按钮
        self.worker.started.connect(self.on_task_started)

        # 连接任务的 finished 信号到槽函数，恢复按钮
        self.worker.finished.connect(self.on_task_finished)

        # self.pushButton.clicked.connect(self.hello)
        self.btntest.clicked.connect(self.select_file_mech)
        self.pushButton.clicked.connect(self.select_file_geskon)
        self.pushButton_2.clicked.connect(self.select_file_dcm)
        self.pushButton_3.clicked.connect(self.select_file_a2l)
        self.pushButton_4.clicked.connect(self.select_file_data)
        self.startbtn.clicked.connect(self.worker.run)

        # 创建菜单栏
        self.menu_bar = self.menuBar()
        menubar = self.menuBar()
        # 创建“文件”菜单
        file_menu = menubar.addMenu('文件')

        # 创建“退出”菜单项
        exit_action = QAction('退出', self)
        exit_action.triggered.connect(self.close)  # 关联退出菜单项的单击事件
        file_menu.addAction(exit_action)

        # 创建“帮助”菜单
        self.help_menu  = self.menu_bar.addMenu("帮助")
        # 创建“关于”菜单项
        about_action = QAction('关于', self)
        about_action.triggered.connect(self.show_about_dialog)  # 关联关于菜单项的单击事件
        self.help_menu.addAction(about_action)

    def show_about_dialog(self):
        # 创建应用程序说明框
        about_dialog = QMessageBox()
        about_dialog.setWindowTitle('关于')

        # 添加软件说明文本和网页链接
        about_dialog.setText('SysEng 2.0 Data Query Tool')
        about_dialog.setInformativeText(
            "如果您有任何问题或建议，请发送电子邮件至"
            '<a href="mailto:zhengli.yang@boschhuayu-steering.com">zhengli.yang@boschhuayu-steering.com</a>'
            "本工具详细说明请查阅"
            '<a href="https://www.baidu.com/">Baidu</a>'
        )

        about_dialog.setDetailedText('更新历史:\n'
                                     'V1.1 Demo 03/17/2023')
        about_dialog.setTextFormat(Qt.RichText)
        about_dialog.setTextInteractionFlags(Qt.TextBrowserInteraction)
        about_dialog.setIcon(QMessageBox.Information)
        # 调整窗口大小和布局
        about_dialog.resize(1000, 800)
        about_dialog.setMinimumSize(1000, 800)
        about_dialog.setMaximumSize(1000, 800)
        layout = QVBoxLayout(about_dialog)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        about_dialog.setLayout(layout)
        # 设置样式表
        style_sheet = """
        QMessageBox QLabel {
            font-size: 10pt;
        }
        QMessageBox QTextBrowser {
            font-size: 10pt;
        }
        """
        about_dialog.setStyleSheet(style_sheet)

        # 在网页链接上添加链接打开功能
        for text_browser in about_dialog.findChildren(QTextBrowser):
            text_browser.setOpenExternalLinks(True)

        about_dialog.exec()



    def hello(self):
        print("hello")

    def select_file_mech(self):
        global file_mech_table
        file_mech_table = ""
        file_path_mech, _ = QFileDialog.getOpenFileName(self, "选择机械参数表", ".", "表格文件(*.xlsm);;所有文件(*)")
        if file_path_mech:
            # self.file_path_label.setText(file_path_mech)
            self.lineEdit.setText(file_path_mech)
            # self.compute_button.setEnabled(True)
            file_mech_table = file_path_mech
            print(file_mech_table)
        return file_mech_table

    def select_file_geskon(self):
        global file_geskon
        file_geskon = ""
        file_path_geskon, _ = QFileDialog.getOpenFileName(self, "选择Geskon文件", ".", "geskon文件(*.kon);;所有文件(*)")
        if file_path_geskon:
            self.lineEdit_2.setText(file_path_geskon)
            file_geskon = file_path_geskon
            print(file_geskon)
        return file_geskon

    def select_file_dcm(self):
        global file_dcm
        file_dcm = ""
        file_path_dcm, _ = QFileDialog.getOpenFileName(self, "选择DCM文件", ".", "dcm文件(*.dcm);;所有文件(*)")
        if file_path_dcm:
            self.lineEdit_3.setText(file_path_dcm)
            file_dcm = file_path_dcm
            print(file_dcm)
        return file_dcm

    def select_file_a2l(self):
        global file_a2l
        file_a2l = ""
        file_path_a2l, _ = QFileDialog.getOpenFileName(self, "选择A2L文件", ".", "a2l文件(*.a2l);;所有文件(*)")
        if file_path_a2l:
            self.lineEdit_4.setText(file_path_a2l)
            file_a2l = file_path_a2l
            print(file_a2l)
        return file_a2l

    def select_file_data(self):
        global file_data_mytable
        file_data_mytable = ""
        file_path_data, _ = QFileDialog.getOpenFileName(self, "选择Data更新表", ".", "表格文件(*.xlsx);;所有文件(*)")
        if file_path_data:
            self.lineEdit_5.setText(file_path_data)
            file_data_mytable = file_path_data
            print(file_data_mytable)
        return file_data_mytable

    def on_button_clicked(self):
        # 创建 MyTask 对象并将其移动到 QThread 中
        self.task = MyTask()
        # self.thread = QThread()
        self.task.moveToThread(self.thread)
        print("按钮被点击")

        # 连接任务的 started 信号到槽函数，禁用按钮
        self.task.started.connect(self.on_task_started)

        # 连接任务的 finished 信号到槽函数，恢复按钮
        self.task.finished.connect(self.on_task_finished)
        # 启动线程并开始任务
        self.thread.start()
        self.task.run(file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table)


    def on_task_started(self):
        # 禁用按钮
        self.lineEdit_info.setText("正在运行中, 请耐心等待...请勿关闭程序")
        self.btntest.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.startbtn.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)

    def on_task_finished(self):
        QMessageBox.information(self, "提示", "操作已完成！")
        # 恢复按钮
        self.lineEdit_info.setText("运行结束.")
        self.startbtn.setEnabled(True)
        self.btntest.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)

        # 任务执行完毕后，清理并退出线程
        self.worker.deleteLater()
        self.thread.quit()
        self.thread.wait()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
