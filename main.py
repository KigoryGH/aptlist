from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Static

class AptListApp(App):
    CSS_PATH = "style.tcss"

    def compose(self):
        yield Static("aptlist", id="title")
        with Horizontal():
            yield Static("Search", id="sidebar")
            yield Static("Information", id="main")

if __name__ == "__main__":
    app = AptListApp()
    app.run()