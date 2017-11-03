
from .ctrl_item_list import *
from .ctrl_contact_info import *
from .ctrl_priorities import *

class Controller():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.ui = ui
        self.item_list = CTRLItemList(organizer, ui)
        self.contact_info = CTRLContactInfo(organizer, ui)
        self.priorities = CTRLPriorities(organizer, ui)

