import click

from git_remover import remove_git


@click.group('remover')
def remover():
    pass



@remover.command(help='Input .git folder path')
@click.option('--path')
def remove(path):
    remove_git(path)
    click.echo('Done')



try:
    if __name__ == '__main__':
        remover()
except Exception as e:
    print(e)