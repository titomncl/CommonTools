from PySide2 import QtWidgets as Qw
from PySide2 import QtCore as Qc


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
        self.btns_w = {"Assets": [], "Shots": []}
        self.asset_type = None

        self.set_ui()
        self.init_connections()

    def set_ui(self):

        self.setFixedSize(400, 300)

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        btn_layout = Qw.QHBoxLayout()

        self.asset_btn = Qw.QPushButton("Assets")
        self.asset_btn.setCheckable(True)
        self.asset_btn.setChecked(False)

        self.shots_btn = Qw.QPushButton("Shots")
        self.shots_btn.setCheckable(True)
        self.shots_btn.setChecked(False)

        btn_layout.addWidget(self.asset_btn)
        btn_layout.addWidget(self.shots_btn)

        self.assets_w = self.asset_widget()
        self.shots_w = self.shot_widget()

        self.stacked_widget = Qw.QStackedWidget()
        self.stacked_widget.addWidget(self.assets_w)
        self.stacked_widget.addWidget(self.shots_w)
        empty_w = Qw.QWidget()
        self.stacked_widget.addWidget(empty_w)
        self.stacked_widget.setCurrentWidget(empty_w)

        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.stacked_widget)
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 20))
        main_layout.addLayout(self.accept_close_layout())

        self.setLayout(main_layout)

    def asset_widget(self):
        a_widget = Qw.QWidget()
        v_layout = Qw.QVBoxLayout()

        v_layout.addLayout(self.asset_type_layout())
        v_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        v_layout.addLayout(self.asset_library_layout())
        v_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        v_layout.addLayout(self.buttons_layout("Assets"))

        a_widget.setLayout(v_layout)
        return a_widget

    def shot_widget(self):
        s_widget = Qw.QWidget()
        v_layout = Qw.QVBoxLayout()

        v_layout.addLayout(self.seq_shot_layout())
        v_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        v_layout.addLayout(self.buttons_layout("Shots"))

        s_widget.setLayout(v_layout)
        return s_widget

    def seq_shot_layout(self):
        v_layout = Qw.QVBoxLayout()

        seq_label = Qw.QLabel("Sequence:")

        self.seq_library_combobox = Qw.QComboBox()
        self.seq_library_combobox.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Ignored)
        self.seq_library_combobox.setMinimumSize(0, 25)
        self.seq_library_combobox.currentIndexChanged.connect(self.list_shots)

        shot_label = Qw.QLabel("Shot:")

        self.shot_library_combobox = Qw.QComboBox()
        self.shot_library_combobox.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Ignored)
        self.shot_library_combobox.setMinimumSize(0, 25)

        v_layout.addWidget(seq_label)
        v_layout.addWidget(self.seq_library_combobox)
        v_layout.addWidget(shot_label)
        v_layout.addWidget(self.shot_library_combobox)

        return v_layout

    def asset_type_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.chara_btn = self.type_btn("CHARA", True)

        self.props_btn = self.type_btn("PROPS", True)

        self.set_btn = self.type_btn("SET", True)

        self.fx_btn = self.type_btn("FX", True)

        self.chara_btn.setChecked(False)
        self.props_btn.setChecked(False)
        self.set_btn.setChecked(False)
        self.fx_btn.setChecked(False)

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

    def buttons_layout(self, key):

        for title in self.buttons[key]:
            btn = self.dpt_btn(title, True)
            self.btns_w[key].append(btn)

        return self.department_layout(self.btns_w[key])

    def type_btn(self, text, is_checkable=False):
        type_btn = Qw.QPushButton()
        type_btn.setText(text)
        type_btn.setCheckable(is_checkable)
        type_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        type_btn.setProperty("type", text)

        return type_btn

    def dpt_btn(self, title, is_checkable=False):
        dpt_btn = Qw.QPushButton(title)
        dpt_btn.setCheckable(is_checkable)
        dpt_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.MinimumExpanding)
        dpt_btn.clicked.connect(self.dpt_btn_action)

        return dpt_btn

    def dpt_btn_action(self):
        for btn in self.btns_w[self.asset_or_shot()]:
            if btn != self.sender():
                btn.setChecked(False)

    def asset_library_layout(self):

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Asset:")

        self.asset_library_combobox = Qw.QComboBox()
        self.asset_library_combobox.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Ignored)
        self.asset_library_combobox.setMinimumSize(0, 25)

        v_layout.addWidget(label)
        v_layout.addWidget(self.asset_library_combobox)

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
        self.asset_type = self.chara_btn.text()
        self.list_assets(self.asset_type)

    def props_action(self):
        self.props_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.set_btn.setChecked(False)
        self.fx_btn.setChecked(False)
        self.asset_type = self.props_btn.text()
        self.list_assets(self.asset_type)

    def set_action(self):
        self.set_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.props_btn.setChecked(False)
        self.fx_btn.setChecked(False)
        self.asset_type = self.set_btn.text()
        self.list_assets(self.asset_type)

    def fx_action(self):
        self.fx_btn.setChecked(True)
        self.set_btn.setChecked(False)
        self.chara_btn.setChecked(False)
        self.props_btn.setChecked(False)
        self.asset_type = self.fx_btn.text()
        self.list_assets(self.asset_type)

    def assets_btn_action(self):
        if not self.asset_btn.isChecked():
            self.asset_btn.setChecked(True)
        self.shots_btn.setChecked(False)
        self.stacked_widget.setCurrentWidget(self.assets_w)

    def list_assets(self, asset_type):
        self.asset_library_combobox.clear()
        assets = self.controller.list_assets(asset_type)

        if assets:
            self.asset_library_combobox.addItems(assets)

    def list_shots(self):
        self.shot_library_combobox.clear()
        if self.seq_library_combobox.currentText():
            shots = self.controller.list_shots(self.controller.get_sequence(self.seq_library_combobox.currentText()))

            if shots:
                self.shot_library_combobox.addItems(shots)

    def shots_btn_action(self):
        if not self.shots_btn.isChecked():
            self.shots_btn.setChecked(True)
        self.asset_btn.setChecked(False)
        self.stacked_widget.setCurrentWidget(self.shots_w)

        self.seq_library_combobox.clear()
        self.shot_library_combobox.clear()
        sequences = self.controller.list_seq()

        if sequences:
            self.seq_library_combobox.addItems(sequences)

    def init_connections(self):
        self.asset_btn.clicked.connect(self.assets_btn_action)
        self.shots_btn.clicked.connect(self.shots_btn_action)

        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.set_btn.clicked.connect(self.set_action)
        self.fx_btn.clicked.connect(self.fx_action)

        self.accept_btn.clicked.connect(self.accept_action)
        self.close_btn.clicked.connect(self.close)

    def accept_action(self):
        choice, accept_choice = self.message_box(title=self.windowTitle(),
                                                 text="You are going to {} the file.".format(
                                                     self.windowTitle().lower()),
                                                 informative_text="Continue?")

        if choice == accept_choice:
            if self.asset_or_shot() == "Assets":
                asset = self.controller.get_asset(self.asset_library_combobox.currentText(), self.asset_type)

                self.controller.accept_action(asset, self.selected_dpt())

            if self.asset_or_shot() == "Shots":
                seq = self.controller.get_sequence(self.seq_library_combobox.currentText())
                shot = self.controller.get_shot(seq, self.shot_library_combobox.currentText())

                self.controller.accept_action(shot, self.selected_dpt())

    def asset_or_shot(self):
        if self.asset_btn.isChecked():
            return self.asset_btn.text()
        elif self.shots_btn.isChecked():
            return self.shots_btn.text()

    def selected_dpt(self):
        for btn in self.btns_w[self.asset_or_shot()]:
            if btn.isChecked():
                return btn.text()

    # @property
    # def get_file_info(self):

        # test = {
        #     "Assets":
        #         (
        #             self.asset_type,
        #             self.asset_library_combobox.currentText(),
        #             self.selected_dpt()
        #         ),
        #     "Shots":
        #         (
        #             self.controller.get_sequence(self.seq_library_combobox.currentText()),
        #             self.shot_library_combobox.currentText(),
        #             self.selected_dpt()
        #         )
        # }
        #
        # return test

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
