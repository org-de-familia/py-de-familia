from playsound import playsound
import click
from pathlib import Path


ASSETS_PATH = 'assets'
assets = Path(ASSETS_PATH)


def discovery_persons_of_family() -> list:
    persons = []
    for person in assets.iterdir():
        persons.append(person.name)
    return persons


def discovery_phrases_of_person(person) -> list:
    phrases = []
    for phrase in Path(assets, person).iterdir():
        phrases.append(phrase.stem)
    return phrases


@click.command()
@click.option(
    '--personagem',
    '-p',
    default='jailson',
    help='Nome do Ator',
    type=click.Choice(discovery_persons_of_family(), case_sensitive=False)
)
@click.option(
    '--frase',
    '-f',
    default='ai',
    help='Frase Deliciosa',
    type=click.Choice(discovery_phrases_of_person('jailson'))
)
def run(personagem, frase):
    sound_path = Path(assets, personagem, frase).with_suffix('.mp3')
    print(sound_path)
    playsound(str(sound_path.absolute()))


def main():
    print('neto')


if __name__ == '__main__':
    run()
