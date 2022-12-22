"""eyesbeen cli entrypoint"""
import rich
import typer

from eyesbeen import validate_isbn

app = typer.Typer()


@app.command()
def main(isbn: str) -> str:
    """CLI entrypoint"""
    result = validate_isbn(isbn)

    colour = "blue"

    if "Invalid" in result:
        colour = "red"
    elif result == "Valid":
        colour = "green"

    rich.print(f"[{colour}]{result}[/{colour}]")
