from ui import UI


class Controller(object):
    def __init__(self, core, parent=None):
        self.ui = UI(self, parent)
        self.core = core

    def get_frame_range(self):
        return self.core.START_FRAME, self.core.END_FRAME

    def export_asset(self, export_hd, only_hd):
        if not only_hd:
            self.core.export_abc(self.core.compute_export_path("LD"))

        if only_hd or export_hd:
            self.core.compute_hd_export()

    def export_anim(self, start, end):
        self.core.export_abc(self.core.compute_export_path(), start, end)

    def export_camera(self, start, end, comment):
        print(self.core.compute_export_path(comment))
        self.core.export_abc(self.core.compute_export_path(comment), start, end)
