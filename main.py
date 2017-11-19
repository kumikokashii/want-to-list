from want_to_list_model import *
from want_to_list_view import *
from want_to_list_controller import *

organizer = Organizer()
ui = UserInterface(organizer)
controller = Controller(organizer, ui)
ui.set_controller(controller)

organizer.load()
ui.initialize()
ui.mainloop()

