from CommonTools.save_load.ui import UI
from Odin import Project, Asset


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

        self.library_box = self.ui.library_combobox

        self.get_assets()

        self.show()

    def accept_action(self):
        self.core(self.asset_type, self.asset_name, self.dpt)

    def show(self):
        self.ui.show()

    def asset_action(self, asset_type):
        self.asset_type = asset_type
        self.get_assets()

    def get_assets(self):
        assets_ = Asset.list(Project.load(self.root, self.project), self.asset_type)
        self.library_box.clear()

        if assets_:
            assets_.sort()
            self.library_box.addItems(assets_)

    @property
    def asset_name(self):
        return self.library_box.currentText()
