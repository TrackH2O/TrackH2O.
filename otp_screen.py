from kivy.uix.screenmanager import Screen
from backend import AuthBackend

class OTPScreen(Screen):

    def verify_otp(self):
        otp = self.ids.otp.text

        if AuthBackend.verify_otp(otp):
            print("Verified Successfully")
            self.manager.current = 'home'
        else:
            print("Invalid OTP")
