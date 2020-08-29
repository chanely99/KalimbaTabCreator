import math
from qtpy.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from qtpy.QtGui import QColor

CHUNK_SIZE = 8
NUM_TINES = 17
TINES_WITH_HIGHLIGHT = [2,5,8,11,14]

class TabTable(QAbstractTableModel):
    def __init__(self, parent, view, note_data):
        super().__init__()

        self.view = view
        
        self.parent = parent
        self.section = 1
        self.note_data = note_data
        self.view.clicked.connect(self.onItemClicked)

    def headerData(self, section, orientation, role):
        return QVariant()
        
    def rowCount(self, parent = QModelIndex()):
        return 8*len(self.note_data)

    def columnCount(self, parent = QModelIndex()):
        return NUM_TINES
        
    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid():
            return QVariant()

        row = index.row()
        col = index.column()
        if row >= self.rowCount() or col >= self.columnCount():
            return QVariant()

        if role == Qt.DisplayRole:
            note_data_index = math.floor(row/CHUNK_SIZE)
            chunk_index = row % CHUNK_SIZE
            note = self.note_data[note_data_index][chunk_index][col]

            return QVariant(self.note_from_val(note))

        if role == Qt.BackgroundRole:
            if col in TINES_WITH_HIGHLIGHT: 
                return QColor(255, 102, 102)

    def note_from_val(self, value): 
        if value == "|": 
            return "  "
        elif value == "O": 
            return "⚫"
        else: 
            return "⬛"

    def onItemClicked(self): 
        indexes = self.view.selectedIndexes()
        row, col = None, None
        for index in indexes: #only going to be one
            row = index.row()
            col = index.column()
        note_data_index = math.floor(row/CHUNK_SIZE)
        chunk_index = row % CHUNK_SIZE
        cur_note = self.note_data[note_data_index][chunk_index][col]
        if cur_note == "O": 
            self.note_data[note_data_index][chunk_index][col] = "|"
        else: 
            self.note_data[note_data_index][chunk_index][col] = "O"

