from qtpy import QtCore as Qc
from qtpy import QtWidgets as Qw


class UI(Qw.QWidget):
    def __init__(self, controller, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.setAttribute(Qc.Qt.WidgetAttribute.WA_QuitOnClose)

        self.setParent(parent)
        self.setWindowFlags(Qc.Qt.Tool)

        self.setWindowTitle("Exporter")

        self.controller = controller

        self.set_ui()

    def set_ui(self):

        self.setFixedSize(400, 250)

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        main_layout.addLayout(self.export_type_layout())
        main_layout.addLayout(self.hd_or_ld_export_layout())
        main_layout.addLayout(self.frame_range_layout())
        main_layout.addLayout(self.export_close_btn_layout())

        self.setLayout(main_layout)

    def export_type_layout(self):
        h_layout = Qw.QHBoxLayout()
        h_layout.setContentsMargins(10, 10, 10, 10)

        self.asset_btn = Qw.QPushButton()
        self.asset_btn.setText("Asset")
        self.asset_btn.setCheckable(True)
        self.asset_btn.clicked.connect(self.asset_action)

        self.anim_btn = Qw.QPushButton()
        self.anim_btn.setText("Anim")
        self.anim_btn.setCheckable(True)
        self.anim_btn.clicked.connect(self.anim_action)

        self.camera_btn = Qw.QPushButton()
        self.camera_btn.setText("Camera")
        self.camera_btn.setCheckable(True)
        self.camera_btn.clicked.connect(self.camera_action)

        h_layout.addWidget(self.asset_btn)
        h_layout.addWidget(self.anim_btn)
        h_layout.addWidget(self.camera_btn)

        return h_layout

    def hd_or_ld_export_layout(self):
        h_layout = Qw.QHBoxLayout()
        h_layout.setContentsMargins(10, 10, 10, 10)

        self.export_hd = Qw.QCheckBox()
        self.export_hd.setText("Auto export HD with LD")
        self.export_hd.clicked.connect(self.export_hd_action)

        self.only_hd = Qw.QCheckBox()
        self.only_hd.setText("Only HD")
        self.only_hd.setEnabled(False)

        h_layout.addWidget(self.export_hd)
        h_layout.addWidget(self.only_hd)

        return h_layout

    def frame_range_layout(self):
        v_layout = Qw.QVBoxLayout()
        v_layout.setContentsMargins(10, 10, 10, 10)

        label = Qw.QLabel("Frame range:")

        h_layout = Qw.QHBoxLayout()

        start_label = Qw.QLabel("Start frame:")
        self.start_frame = Qw.QSpinBox()
        self.start_frame.setValue(1)
        self.start_frame.setEnabled(False)
        self.start_frame.setMinimum(0)
        self.start_frame.setMaximum(10000)

        end_label = Qw.QLabel("End frame:")
        self.end_frame = Qw.QSpinBox()
        self.end_frame.setValue(1)
        self.end_frame.setEnabled(False)
        self.end_frame.setMinimum(0)
        self.end_frame.setMaximum(10000)

        self.lock_frame_range = Qw.QPushButton("Lock")
        self.lock_frame_range.setCheckable(True)
        self.lock_frame_range.setChecked(True)
        self.lock_frame_range.clicked.connect(self.lock_frame_range_action)

        h_layout.addWidget(start_label)
        h_layout.addWidget(self.start_frame)
        h_layout.addWidget(end_label)
        h_layout.addWidget(self.end_frame)
        h_layout.addWidget(self.lock_frame_range)

        v_layout.addWidget(label)
        v_layout.addLayout(h_layout)

        return v_layout

    def export_close_btn_layout(self):
        h_layout = Qw.QHBoxLayout()
        h_layout.setContentsMargins(10, 10, 10, 10)

        self.export_btn = Qw.QPushButton()
        self.export_btn.setText("Export")
        self.export_btn.clicked.connect(self.export_action)

        self.close_btn = Qw.QPushButton()
        self.close_btn.setText("Close")
        self.close_btn.clicked.connect(self.close)

        h_layout.addWidget(self.export_btn)
        h_layout.addWidget(self.close_btn)

        return h_layout

    def set_frame_range(self, start, end):
        self.start_frame.setValue(start)
        self.end_frame.setValue(end)

    def asset_action(self):
        if not self.asset_btn.isChecked():
            self.asset_btn.setChecked(True)
        self.anim_btn.setChecked(False)
        self.camera_btn.setChecked(False)

        self.export_hd.setEnabled(True)
        self.lock_frame_range.setEnabled(False)

        self.set_frame_range(1, 1)

    def anim_action(self):
        if not self.anim_btn.isChecked():
            self.anim_btn.setChecked(True)
        self.asset_btn.setChecked(False)
        self.camera_btn.setChecked(False)

        self.export_hd.setEnabled(False)
        self.lock_frame_range.setEnabled(True)

        self.set_frame_range(*self.controller.get_frame_range())

    def camera_action(self):
        if not self.camera_btn.isChecked():
            self.camera_btn.setChecked(True)
        self.asset_btn.setChecked(False)
        self.anim_btn.setChecked(False)

        self.export_hd.setEnabled(False)
        self.lock_frame_range.setEnabled(True)

        self.set_frame_range(*self.controller.get_frame_range())

    def export_hd_action(self):
        if self.export_hd.isChecked():
            self.only_hd.setEnabled(True)
        else:
            self.only_hd.setChecked(False)
            self.only_hd.setEnabled(False)

    def lock_frame_range_action(self):
        if self.lock_frame_range.isChecked():
            self.start_frame.setEnabled(False)
            self.end_frame.setEnabled(False)
        else:
            self.start_frame.setEnabled(True)
            self.end_frame.setEnabled(True)

    def export_action(self):
        if self.asset_btn.isChecked():
            self.controller.export_asset(self.export_hd.isChecked(), self.only_hd.isChecked())
        elif self.anim_btn.isChecked():
            if self.start_frame.value() > self.end_frame.value():
                raise RuntimeError("Start frame can't be greater than end frame")
            else:
                self.controller.export_anim(self.start_frame.value(), self.end_frame.value())
        elif self.camera_btn.isChecked():
            if self.start_frame.value() > self.end_frame.value():
                raise RuntimeError("Start frame can't be greater than end frame")
            else:
                self.controller.export_camera(self.start_frame.value(), self.end_frame.value(), "CAMERA")
        else:
            raise RuntimeError("No type selected")

    def closeEvent(self, QCloseEvent):
        self.destroy()
