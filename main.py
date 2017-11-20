import want_to_list as wtl

organizer = wtl.Organizer()
organizer.load()
ui = wtl.UserInterface(organizer)
controller = wtl.Controller(organizer, ui)
ui.set_controller(controller)

ui.initialize()
ui.mainloop()

