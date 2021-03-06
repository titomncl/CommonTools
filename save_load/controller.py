from CommonTools.save_load.ui import UI

from Odin.source.core import assets, sets, fx


class Controller(object):

    def __init__(self, save_load, title, ui_instance, root, project):

        self.save_load = save_load
        self.ui = UI(self, title, ui_instance)

        self.ui.accept_btn.setText(title)

        self.root = root
        self.project = project

        self.asset_type = "CHARA"
        self.dpt = "MOD"

        self.chara_btn = self.ui.chara_btn
        self.props_btn = self.ui.props_btn
        self.set_btn = self.ui.set_btn
        self.fx_btn = self.ui.fx_btn
        self.mod_btn = self.ui.mod_btn
        self.shd_btn = self.ui.shd_btn
        self.rig_btn = self.ui.rig_btn
        self.accept_btn = self.ui.accept_btn
        self.close_btn = self.ui.close_btn

        self.library_box = self.ui.library_combobox

        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.set_btn.setChecked(False)
        self.fx_btn.setChecked(False)
        self.mod_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.rig_btn.setChecked(False)

        self.get_assets()

        self.init_btn_connections()

        self.show()

    def save_load_action(self):
        self.save_load(self.asset_type, self.asset_name, self.dpt)

    def show(self):
        self.ui.show()

    def init_btn_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.set_btn.clicked.connect(self.set_action)
        self.fx_btn.clicked.connect(self.fx_action)
        self.mod_btn.clicked.connect(self.mod_action)
        self.shd_btn.clicked.connect(self.shd_action)
        self.rig_btn.clicked.connect(self.rig_action)

        self.accept_btn.clicked.connect(self.save_load_action)

    def chara_action(self):
        self.asset_type = "CHARA"
        self.get_assets()

    def props_action(self):
        self.asset_type = "PROPS"
        self.get_assets()

    def set_action(self):
        self.asset_type = "SET"
        self.get_sets()

    def fx_action(self):
        self.dpt = "FX"
        self.get_fx()

    def mod_action(self):
        self.dpt = "MOD"

    def shd_action(self):
        self.dpt = "SHD"

    def rig_action(self):
        self.dpt = "RIG"

    def get_assets(self):
        assets_ = assets.find_assets(self.root, self.project, self.asset_type)
        self.library_box.clear()

        if assets_:
            assets_.sort()
            self.library_box.addItems(assets_)

    def get_sets(self):
        sets_ = sets.find_sets(self.root, self.project)
        self.library_box.clear()

        if sets_:
            sets_.sort()

            self.library_box.addItems(sets_)

    def get_fx(self):
        fx_ = fx.find_fx(self.root, self.project)
        self.library_box.clear()

        if fx_:
            fx_.sort()
            self.library_box.addItems(fx_)

    @property
    def asset_name(self):
        return self.library_box.currentText()
