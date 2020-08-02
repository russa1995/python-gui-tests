from pywinauto.application import Application as WinApplication


class Application:

    def __init__(self, target):
        self.application = WinApplication(backend="win32").start(target)
        self.main_window = self.application.window(title="Free Address Book")
        self.main_window.wait("visible")

    def destroy(self):
        self.main_window.close()
