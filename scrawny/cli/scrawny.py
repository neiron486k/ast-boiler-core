import click
from .colours import *
from click import echo
import os
import shutil


@click.group(help=yellow('Welcome to console of project'))
def cli():
    pass


@cli.command(name='init')
@click.option('--force', '-f', default=False, is_flag=True, help='Recreate project structure if exists')
@click.argument('destination', default='.')
def init(destination: str, force: bool) -> None:
    """
    Initialise new project
    """
    echo(green('\nInitialise:'))
    echo(green('-' * 30))
    destination = os.path.realpath(destination)

    if not os.path.exists(destination):
        os.makedirs(destination)

    source = os.path.join(
        os.path.realpath(os.path.dirname(os.path.dirname(__file__))),
        'scrawny_templates'
    )

    # copy all files from scrawny_templates to destination
    exclude = ['.env.def']

    if force:
        echo(red('Removing old data'))
        if destination != '.':
            shutil.rmtree(destination)
            os.makedirs(destination)

    for path, _, files in os.walk(source):
        for file_name in files:
            file = os.path.join(path, file_name)
            rel_path = os.path.relpath(path, source)
            dst = os.path.join(destination, rel_path)

            if rel_path == '.':
                dst = destination

            dst_file = os.path.join(dst, file_name)

            if not os.path.exists(dst):
                os.makedirs(dst)

            if not os.path.isfile(dst_file) and file_name not in exclude:
                shutil.copy(file, dst_file)

    # create .env
    echo(yellow('Create .env'))
    dotenv = os.path.join(os.getcwd(), destination, '.env')
    dist_dotenv = os.path.join(source, '.env.def')
    create_dotenv(dist_dotenv, dotenv)
    echo(yellow('Initialize completed'))


def create_dotenv(src: str, dst: str) -> None:
    """
    Create .evn file with FLASK_APP such as destination folder of project
    :param src: str
    :param dst: str
    :return: None
    """
    if not os.path.isfile(dst):
        shutil.copy(src, dst)
        with open(dst, 'a') as file:
            file.write('\nFLASK_APP=' + os.path.basename(os.path.dirname(dst)))
