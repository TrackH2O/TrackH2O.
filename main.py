from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from login_screen import LoginScreen
from otp_screen import OTPScreen
from home_screen import HomeScreen


class WindowManager(ScreenManager):
    pass


class TrackH2OApp(App):
    def build(self):
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    TrackH2OApp().run()
