from CommonTools.save_load.ui import UI

from Odin.source.core import assets, sets, fx


class Controller(object):

    def __init__(self, core, title, ui_instance, root, project, buttons):

        self.core = core
        self.ui = UI(self, title, buttons, ui_instance)

        self.ui.accept_btn.setText(title)

        self.title = title
        self.root = root
        self.project = project

        self.asset_type = "CHARA"
        self.dpt = list(buttons.keys())[0]

        self.chara_btn = self.ui.chara_btn
        self.props_btn = self.ui.props_btn
        self.set_btn = self.ui.set_btn
        self.fx_btn = self.ui.fx_btn

        self.accept_btn = self.ui.accept_btn
        self.close_btn = self.ui.close_btn

        self.library_box = self.ui.library_combobox

        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.set_btn.setChecked(False)
        self.fx_btn.setChecked(False)

        self.get_assets()

        self.init_btn_connections()

        self.show()

    def accept_action(self):
        choice, accept_choice = self.ui.message_box(title=self.title,
                                                    text="You are going to {} the file.".format(self.title.lower()),
                                                    informative_text="Continue?")

        if choice == accept_choice:
            self.core(self.asset_type, self.asset_name, self.dpt)

    def show(self):
        self.ui.show()

    def init_btn_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.set_btn.clicked.connect(self.set_action)
        self.fx_btn.clicked.connect(self.fx_action)

        self.accept_btn.clicked.connect(self.accept_action)

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
