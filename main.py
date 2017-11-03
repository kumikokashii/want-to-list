from want_to_list_model import *
from user_interface import *

organizer = Organizer()

#organizer = organizer.load()
organizer.load_default()

print(organizer)

ui = UserInterface(organizer)
ui.initialize()

#controller = Controller()

#organizer.save()

