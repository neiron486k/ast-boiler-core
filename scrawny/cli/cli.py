from werkzeug import run_simple
import click
from dotenv import dotenv_values

dotenv_values()


@click.command()
@click.option('--host', '-h', default='0.0.0.0', help='Bind to host')
@click.option('--port', '-p', default=8000, help='Listen on port')
def run(host, port):

    run_simple(
        hostname=host,
        port=port,
        application=app
    )
