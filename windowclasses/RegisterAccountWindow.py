from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from windowclasses import WindowManager as wm

import db_control as db

# This class allows a patient user to register an account
class RegisterAccountWindow(Screen):
    kv = Builder.load_file("stylefolders/raw.kv")
    fr_name = ObjectProperty(None)
    lt_name = ObjectProperty(None)
    phone = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def reg_accout(self):
        db.create_user(self.fr_name.text, self.lt_name.text, self.email.text, self.password.text,
                        self.phone.text,"Not", "Patient")
        wm.screen_manager.current = "pat_login"

    def reset_inputs(self):
        self.fr_name.text = ""
        self.lt_name.text = ""
        self.phone.text = ""
        self.email.text = ""
        self.password.text = ""