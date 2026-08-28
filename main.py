import subprocess
from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Collapsible, OptionList
from textual.widgets.option_list import Option
from textual import work


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


def get_all_packages():
    result = subprocess.run(
        ["apt", "list"],
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


def get_package_details(name):
    result = subprocess.run(
        ["apt-cache", "show", name],
        capture_output=True,
        text=True
    )
    return result.stdout


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

    def compose(self):
        yield Static("aptlist", id="title")
        with Horizontal():
            with Vertical(id="sidebar", classes="panel"):
                with Collapsible(title="Browse", id="browse"):
                    yield Static("Please wait...", id="loading")
                    yield OptionList(id="browse-list")
            yield Static("Information", id="main", classes="panel")

    def on_mount(self):
        self.load_packages()

    @work(thread=True)
    def load_packages(self):
        all_names = sorted(set(get_all_packages()))
        installed_names = set(get_installed_packages())
        options = []
        for name in all_names:
            if name in installed_names:
                options.append(Option(f"[blue]{name}[/blue]", id=name))
            else:
                options.append(Option(name, id=name))
        self.call_from_thread(self.finish_loading, options)

    def finish_loading(self, options):
        self.query_one("#loading", Static).remove()
        self.query_one("#browse-list", OptionList).add_options(options)

    def on_option_list_option_selected(self, event):
        name = event.option.id
        details = get_package_details(name)
        self.query_one("#main", Static).update(details)


if __name__ == "__main__":
    app = AptListApp()
    app.run()