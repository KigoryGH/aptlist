from textual.app import App
from textual.widgets import Static

class AptListApp(App):
CSS_PATH = "style.tcss";
    def compose(self):
        yield Static("Welcome to aptlist")

if __name__ == "__main__":
    app = AptListApp()
    app.run()