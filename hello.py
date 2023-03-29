import click

@click.command(help="This is just a hello app. It does nothing.")
@click.option("--name1", prompt="I need your name", help="Need name")
@click.option("--color", prompt="I need your color", help="This is your color")
def hello(name1, color):
    if name1 == "Thor":
        click.echo("Thor, you are always red.")
        click.echo(click.style(f"Hello {name1}!", fg= color))
    else:
        pass

if __name__ == "__main__":
    hello()