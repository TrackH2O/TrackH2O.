from kivy.uix.screenmanager import Screen
from backend import AuthBackend

class LoginScreen(Screen):

    def send_otp(self):
        email = self.ids.email.text

        if "@" in email:
            AuthBackend.send_otp(email)
            self.manager.current = 'otp'
        else:
            print("Enter valid email")
