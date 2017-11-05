from want_to_list_model import *
from want_to_list_view import *
from want_to_list_controller import *

organizer = Organizer.get_test_instance()

# If use pickle:
#organizer = organizer.load()
# If start fresh:
#organizer = Organizer()

print(organizer)

ui = UserInterface(organizer)

controller = Controller(organizer, ui)
ui.set_controller(controller)

ui.initialize()
ui.mainloop()

#organizer.save()

