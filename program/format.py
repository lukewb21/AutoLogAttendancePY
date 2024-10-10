from rich import print
from rich.console import Console
from rich.markdown import Markdown

def printmd(text):
    console = Console()
    markdown = Markdown(text)
    console.print(markdown)