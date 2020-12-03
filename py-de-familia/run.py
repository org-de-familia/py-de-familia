from playsound import playsound
import click
from pathlib import Path


@click.command()
@click.option('--personagem', default='jailson', help='Nome do Ator')
@click.option('--frase', default='ai', help='Frase Deliciosa')
def jailson(personagem, frase):
    playsound(f"{Path('assets', personagem, frase).absolute()}.mp3")


if __name__ == '__main__':
    jailson()
