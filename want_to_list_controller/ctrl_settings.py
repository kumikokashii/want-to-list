
class CTRLSettings():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.ui = ui

    def save_exit(self):
        self.organizer.save()
        self.ui.destroy()

    def start_fresh(self):
        self.organizer.start_fresh()
        self.ui.initialize()
