from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc


class UI(Qw.QWidget):
    def __init__(self, controller, title, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.setParent(parent)
        self.setWindowFlags(Qc.Qt.Tool)

        self.setWindowTitle(title)

        self.controller = controller

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
        main_layout.addLayout(self.department_layout())
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

    def department_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.mod_btn = Qw.QPushButton("MOD")
        self.mod_btn.setCheckable(True)
        self.mod_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.shd_btn = Qw.QPushButton("SHD")
        self.shd_btn.setCheckable(True)
        self.shd_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.rig_btn = Qw.QPushButton("RIG")
        self.rig_btn.setCheckable(True)
        self.rig_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        h_layout.addWidget(self.mod_btn)
        h_layout.addWidget(self.shd_btn)
        h_layout.addWidget(self.rig_btn)

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Department:")

        v_layout.addWidget(label)
        v_layout.addLayout(h_layout)

        return v_layout

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

        self.mod_btn.setEnabled(True)
        self.shd_btn.setEnabled(True)
        self.rig_btn.setEnabled(True)

    def props_action(self):
        self.props_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.set_btn.setChecked(False)
        self.fx_btn.setChecked(False)

        self.mod_btn.setEnabled(True)
        self.shd_btn.setEnabled(True)
        self.rig_btn.setEnabled(True)

    def set_action(self):
        self.set_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.props_btn.setChecked(False)
        self.fx_btn.setChecked(False)

        self.mod_btn.setEnabled(True)
        self.shd_btn.setEnabled(True)
        self.rig_btn.setEnabled(False)

    def fx_action(self):
        self.fx_btn.setChecked(True)
        self.set_btn.setChecked(False)
        self.chara_btn.setChecked(False)
        self.props_btn.setChecked(False)

        self.mod_btn.setEnabled(False)
        self.shd_btn.setEnabled(False)
        self.rig_btn.setEnabled(False)

    def mod_action(self):
        self.mod_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.rig_btn.setChecked(False)

    def shd_action(self):
        self.mod_btn.setChecked(False)
        self.shd_btn.setChecked(True)
        self.rig_btn.setChecked(False)

    def rig_action(self):
        self.mod_btn.setChecked(False)
        self.shd_btn.setChecked(False)
        self.rig_btn.setChecked(True)

    def init_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.set_btn.clicked.connect(self.set_action)
        self.fx_btn.clicked.connect(self.fx_action)
        self.mod_btn.clicked.connect(self.mod_action)
        self.shd_btn.clicked.connect(self.shd_action)
        self.rig_btn.clicked.connect(self.rig_action)

        self.close_btn.clicked.connect(self.close)

    def message_box(self, title, text, informative_text, accept_btn_label, reject_btn_label):

        msg_box = Qw.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setInformativeText(informative_text)
        msg_box.setStandardButtons(Qw.QMessageBox.Ok | Qw.QMessageBox.Cancel)
        msg_box.setDefaultButton(Qw.QMessageBox.Ok)

        return msg_box
