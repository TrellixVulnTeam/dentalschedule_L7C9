from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from windowclasses import StaffLoginWindow as slw
from windowclasses import PatientLoginWindow as plw
from windowclasses import MakeAppointmentWindow as maw
from windowclasses import WindowManager as wm
from windowclasses import CalendarWindow as calendar

import db_control as db

class StaffScheduleAppWindow(Screen):
    kv = Builder.load_file("stylefolders/ssaw.kv")
    dr_email = ObjectProperty(None)
    hy_email = ObjectProperty(None)
    pat_email = ObjectProperty(None)
    descrp = ObjectProperty(None)


    def get_input(self):
        dr_id = db.get_emp_id(self.dr_email.text)
        hy_id = db.get_emp_id(self.hy_email.text)
        pat_id = db.get_pat_id(self.pat_email.text)
        if(dr_id == None):
            self.pop_up("Bad Input", "The provided doctor could not be found")
        elif(hy_id == None):
            self.pop_up("Bad Input", "The provided hygenist could not be found")
        elif(pat_id == None):
            self.pop_up("Bad Input", "The provided patient could not be found")
        else:
            maw.dr_info[0] = self.dr_email.text
            maw.dr_info[1] = self.hy_email.text
            plw.user_info[0] = pat_id
            plw.user_info[2] = self.pat_email.text
            plw.user_info[3] = self.descrp.text
            calendar.window = "st_home"
            wm.screen_manager.current = "calendar"


    # Pop up window for giving the user feedback
    # handles errors or successful operations
    def pop_up(self,header, message):
        popup = Popup(title = header,
                      content = Label(text = message),
                      size_hint = (None, None), size = (400, 400))
        popup.open()