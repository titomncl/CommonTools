import os
import sys

if sys.version_info > (3,):
    import typing
    
    if typing.TYPE_CHECKING:
        from typing import List, Union

from CommonTools.save_load.ui import UI
from Odin import Project, Asset, Sequence, Shot


class Controller(object):
    def __init__(self, core, title, ui_instance, root, project, buttons):
        self.core = core
        self.ui = UI(self, title, buttons, ui_instance)

        self.ui.accept_btn.setText(title)

        self.project = Project.load(root, project)

        self.show()

    def show(self):
        self.ui.show()
    
    def get_asset(self, asset_name, asset_type):
        # type: (str, str) -> Asset
        return Asset.load(self.project, asset_name, asset_type)
    
    def get_sequence(self, seq_name):
        # type: (str) -> Sequence
        return Sequence.load(self.project, seq_name)
    
    def get_shot(self, seq, shot_name):
        # type: (Sequence, str) -> Shot
        return Shot.load(seq, shot_name)
    
    def list_assets(self, asset_type):
        # type: (str) -> List[str]
        return Asset.list(self.project, asset_type)

    def list_seq(self):
        # type: () -> List[str]
        return Sequence.list(self.project)
    
    def list_shots(self, seq):
        # type: (Sequence) -> List[str]
        return Shot.list(seq)

    def accept_action(self, item, dpt):
        # type: (Union[Asset, Shot], str) -> None
        self.core(item, dpt)
