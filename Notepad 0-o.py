class MainWindow(QMainWindow):
    def __init__(self, args, kwargs):
        super(MainWindow, self).__init__(args, kwargs)
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(14)
        self.editor.setFont(fixedfont)
        self.path = None
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        file_toolbar = QToolBar("File")
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&File")
        open_file_action = QAction("Open file", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)
        save_file_action = QAction("Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)
        saveas_file_action = QAction("Save As", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)
        edit_toolbar = QToolBar("Edit")
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")
        undo_action = QAction("Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)
        edit_toolbar.addAction(undo_action)
        edit_menu.addAction(undo_action)
        redo_action = QAction("Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)
 
app = QApplication(sys.argv)
app.setApplicationName("Notepad") 
window = MainWindow()
app.exec_()
 
 
        
 
 
 