import click
from utils.meta import Meta

@click.command()
@click.option(
    "-w", 
    "--what", 
    help="what? meta or linkdin what you want to run"
)
def execute(what):
    if what=="meta":
        Meta()

if __name__=="__main__":
    execute()
