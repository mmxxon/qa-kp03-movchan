import click

url = "http://172.18.0.2:5000"


@click.group()
@click.pass_context
def cli(ctx):
    pass
