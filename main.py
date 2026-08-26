from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static
from textual.widgets import Input

class AptListApp(App):
    CSS_PATH = "style.tcss"

    def compose(self):
        yield Static("aptlist", id="title")
        with Horizontal():
            with Vertical(id="sidebar"):
                with Vertical(id="search"):
                    yield Static("Search")
                    yield Input(placeholder="Search packages", id="search-box")
            yield Static("Information", id="main")

if __name__ == "__main__":
    app = AptListApp()
    app.run()   