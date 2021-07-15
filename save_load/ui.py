from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc


class UI(Qw.QWidget):
    def __init__(self, controller, title, buttons, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.setAttribute(Qc.Qt.WidgetAttribute.WA_QuitOnClose)

        self.setParent(parent)
        self.setWindowFlags(Qc.Qt.Tool)

        self.setWindowTitle(title)

        self.controller = controller
        self.buttons = buttons

        self.set_ui()
        self.init_connections()

    def set_ui(self):

        self.setFixedSize(400, 250)

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        main_layout.addLayout(self.type_layout())
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        main_layout.addLayout(self.library_layout())
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        main_layout.addLayout(self.buttons_layout())
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 20))
        main_layout.addLayout(self.accept_close_layout())

        self.setLayout(main_layout)

    def type_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.chara_btn = Qw.QPushButton("CHARA")
        self.chara_btn.setCheckable(True)
        self.chara_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.props_btn = Qw.QPushButton("PROPS")
        self.props_btn.setCheckable(True)
        self.props_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.set_btn = Qw.QPushButton("SET")
        self.set_btn.setCheckable(True)
        self.set_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.fx_btn = Qw.QPushButton("FX")
        self.fx_btn.setCheckable(True)
        self.fx_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        self.fx_btn.setEnabled(False)  # TODO talk with teddy about workflow with cache files

        h_layout.addWidget(self.chara_btn)
        h_layout.addWidget(self.props_btn)
        h_layout.addWidget(self.set_btn)
        h_layout.addWidget(self.fx_btn)

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Character, Props, Set or FX:")

        v_layout.addWidget(label)
        v_layout.addLayout(h_layout)

        return v_layout

    def department_layout(self, btns):

        h_layout = Qw.QHBoxLayout()

        for btn in btns:
            h_layout.addWidget(btn)

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Department:")

        v_layout.addWidget(label)
        v_layout.addLayout(h_layout)

        return v_layout

    def buttons_layout(self):
        self.btns = list()
        for title in self.buttons:
            btn = self.dpt_btn(title, True)
            self.btns.append(btn)

        self.btns[0].setChecked(True)

        return self.department_layout(self.btns)

    def dpt_btn(self, title, is_checkable=False):
        dpt_btn = Qw.QPushButton(title)
        dpt_btn.setCheckable(is_checkable)
        dpt_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        dpt_btn.clicked.connect(self.dpt_btn_action)

        return dpt_btn

    def dpt_btn_action(self):
        self.controller.dpt = self.sender().text()

        for btn in self.btns:
            if btn != self.sender():
                btn.setChecked(False)

    def library_layout(self):

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Asset:")

        self.library_combobox = Qw.QComboBox()
        self.library_combobox.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Ignored)
        self.library_combobox.setMinimumSize(0, 25)

        v_layout.addWidget(label)
        v_layout.addWidget(self.library_combobox)

        return v_layout

    def accept_close_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.accept_btn = Qw.QPushButton()
        self.accept_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Fixed)

        self.close_btn = Qw.QPushButton("Close")
        self.close_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Fixed)

        h_layout.addWidget(self.accept_btn)
        h_layout.addSpacerItem(Qw.QSpacerItem(10, 1))
        h_layout.addWidget(self.close_btn)

        return h_layout

    def chara_action(self):
        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.set_btn.setChecked(False)
        self.fx_btn.setChecked(False)

        for btn in self.btns:
            btn.setEnabled(self.buttons[btn.text()]["CHARA"])

    def props_action(self):
        self.props_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.set_btn.setChecked(False)
        self.fx_btn.setChecked(False)

        for btn in self.btns:
            btn.setEnabled(self.buttons[btn.text()]["PROPS"])

    def set_action(self):
        self.set_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.props_btn.setChecked(False)
        self.fx_btn.setChecked(False)

        for btn in self.btns:
            btn.setEnabled(self.buttons[btn.text()]["SET"])

    def fx_action(self):
        self.fx_btn.setChecked(True)
        self.set_btn.setChecked(False)
        self.chara_btn.setChecked(False)
        self.props_btn.setChecked(False)

        for btn in self.btns:
            btn.setEnabled(self.buttons[btn.text()]["FX"])

    def init_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.set_btn.clicked.connect(self.set_action)
        self.fx_btn.clicked.connect(self.fx_action)

        self.close_btn.clicked.connect(self.close)

    def message_box(self, title, text, informative_text):

        msg_box = Qw.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setInformativeText(informative_text)
        msg_box.setStandardButtons(Qw.QMessageBox.Ok | Qw.QMessageBox.Cancel)
        msg_box.setDefaultButton(Qw.QMessageBox.Ok)

        choice = msg_box.exec_()

        return choice, Qw.QMessageBox.Ok

    def closeEvent(self, QCloseEvent):
        self.destroy()
