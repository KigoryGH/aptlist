import subprocess
from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input, Collapsible, OptionList


def get_installed_packages():
    result = subprocess.run(
        ["apt", "list", "--installed"],
        capture_output=True,
        text=True
    )
    names = []
    for line in result.stdout.splitlines()[1:]:
        if not line.strip():
            continue
        parts = line.split("/")
        names.append(parts[0])
    return names


class AptListApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+d", "quit", "Quit"),
        ("j", "focus_next", "Next"),
        ("k", "focus_previous", "Previous"),
        ("down", "focus_next", "Next"),
        ("up", "focus_previous", "Previous"),
    ]

    def on_mount(self):
        for widget in self.query("#sidebar, #main"):
            widget.can_focus = True

    def on_option_list_option_selected(self, event):
        self.query_one("#main", Static).update(event.option.prompt)

    def compose(self):
        yield Static("aptlist", id="title")
        with Horizontal():
            with Vertical(id="sidebar", classes="panel"):
                with Vertical(id="search"):
                    yield Static("Search")
                    yield Input(placeholder="Search packages", id="search-box")
                with Collapsible(title="Browse", id="browse"):
                    yield OptionList(*get_installed_packages(), id="browse-list")
            yield Static("Information", id="main", classes="panel")


if __name__ == "__main__":
    app = AptListApp()
    app.run()