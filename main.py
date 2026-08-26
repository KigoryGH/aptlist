from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static

class AptListApp(App):
    CSS_PATH = "style.tcss"

    def compose(self):
        yield Static("aptlist", id="title")
        with Horizontal():
            with Vertical(id="sidebar"):
                with Vertical(id="search"):
                    yield Static("Search")
            yield Static("Information", id="main")

if __name__ == "__main__":
    app = AptListApp()
    app.run()