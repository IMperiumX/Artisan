"""Console script for artisan3d."""
import artisan3d

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for artisan3d."""
    console.print("Replace this message by putting your code into "
               "artisan3d.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
