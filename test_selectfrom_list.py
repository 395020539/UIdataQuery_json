from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QListWidget, QPushButton

class ProjectSelectionDialog(QDialog):
    def __init__(self, project_names):
        super().__init__()
        self.project_names = project_names
        self.selected_project = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        for project_name in self.project_names:
            self.list_widget.addItem(project_name)
        layout.addWidget(self.list_widget)
        button = QPushButton("Select")
        button.clicked.connect(self.select_project)
        layout.addWidget(button)
        self.setLayout(layout)

    def select_project(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            self.selected_project = selected_items[0].text()
            self.close()

def select_project_dialog(project_names):
    app = QApplication([])
    dialog = ProjectSelectionDialog(project_names)
    dialog.exec()
    return dialog.selected_project


project_names = ["Project A", "Project B", "Project C"]
selected_project = select_project_dialog(project_names)
print("Selected project:", selected_project)
