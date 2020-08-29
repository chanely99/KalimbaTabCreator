from qtpy import QtWidgets
from qtpy.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from TabTable import TabTable
from Ui_MainWindow import Ui_MainWindow

#To remake UI -> pyuic5 -o Ui_MainWindow.py mainwindow.ui

CHUNK_SIZE = 8
NUM_TINES = 17
TINES_WITH_HIGHLIGHT = [2,5,8,11,14]

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.note_data = []
        self.add_chunk()
        self.load_table()

        self.ui.ui_add_measure_btn.clicked.connect(self.add_chunk)
        self.ui.ui_load_btn.clicked.connect(self.load_file)
        self.ui.ui_save_btn.clicked.connect(self.save_file)  

    def load_table(self):
        self.table = TabTable(self, self.ui.ui_tab_tbl, self.note_data)
        self.ui.ui_tab_tbl.setModel(self.table)
        
        for i in range(NUM_TINES): 
            self.ui.ui_tab_tbl.setColumnWidth(i, 27)
            self.ui.ui_tab_tbl.horizontalHeader().setSectionResizeMode(i,QHeaderView.Fixed)

    def add_chunk(self):
        new_chunk = []
        for _ in range(CHUNK_SIZE):
            row = []
            for _ in range(NUM_TINES): 
                row.append("|") 
            new_chunk.append(row)
        self.note_data.append(new_chunk)
        self.load_table()

    def load_file(self): 
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filenames = None
        if dlg.exec_():
            filenames = dlg.selectedFiles()

        with open(filenames[0], "r") as f:
            text = f.readlines()
            file_data = []
            chunk = []
            for line in text: 
                row = line.split(' ')
                chunk.append(row[0:-1])
                if len(chunk) == 8: 
                    file_data.append(chunk)
                    chunk = []
            self.note_data = file_data
            print(f"file_data: {file_data}")
            self.load_table()

    def save_file(self): 
        self.note_data = self.table.note_data

        text, ok = QInputDialog.getText(self, 'Save File Dialog', 'Save as:')
        if ok:
            with open(f"{text}.txt","w+") as f: 
                for chunk in self.note_data: 
                    for row in chunk: 
                        row_content = ""
                        for note in row: 
                            row_content += note 
                            row_content += " "
                        row_content += '\n'
                        f.write(row_content)