"""o código é pequeninho mais é garantido"""

from playsound import playsound
import click
from pathlib import Path
from typing import (
    Text,
    List
)
import os


def configurar_autocomplete():
    autocomple_de_familia = Path(
        Path(__file__).parent,
        'autocomplete-de-familia.sh'
    )
    os.system(f'{autocomple_de_familia.absolute()}')


class ExcessaoDeFamilia(RuntimeError):
    pass


ativos_de_familia = Path(
    Path(__file__).parent,
    'ativos-de-familia'
)


def listar_personagens_de_familia() -> List[Text]:
    personagens_de_familia = []
    for personagem_de_familia in ativos_de_familia.iterdir():
        personagens_de_familia.append(personagem_de_familia.name)
    return personagens_de_familia


def obter_audio_de_familia(personagem_de_familia, frase_de_familia) -> str:
    frase_de_familia = Path(
        ativos_de_familia,
        personagem_de_familia,
        frase_de_familia
    ).with_suffix('.mp3')

    return str(frase_de_familia.absolute())


def obter_frases_de_familia(personagem_de_familia):
    frases_de_familia = []

    diretorio_de_familia = Path(
        ativos_de_familia,
        personagem_de_familia
    )

    for frase_de_familia in diretorio_de_familia.iterdir():
        frases_de_familia.append(frase_de_familia.stem)

    return frases_de_familia


def autocompletar_personagem_de_familia(ctx, args, incomplete) -> List[Text]:
    personagens_de_familia = listar_personagens_de_familia()
    possiveis_personagens_de_familia = []

    for personagem_de_familia in personagens_de_familia:
        if incomplete in personagem_de_familia:
            possiveis_personagens_de_familia.append(personagem_de_familia)

    return possiveis_personagens_de_familia


def autocompletar_frase_de_familia(ctx, args, incomplete) -> List[Text]:
    personagens_de_familia = listar_personagens_de_familia()

    if args[1] in personagens_de_familia:
        personagens_de_familia = args[1]
    else:
        raise ExcessaoDeFamilia('nao identificado personagem de familia')

    frases_de_familia = obter_frases_de_familia(personagens_de_familia)

    if not incomplete:
        possiveis_frases_de_familia = frases_de_familia
    else:
        possiveis_frases_de_familia = []
        for frase_de_familia in frases_de_familia:
            if incomplete in frase_de_familia:
                possiveis_frases_de_familia.append(frase_de_familia)

    return possiveis_frases_de_familia


def listar_frases_de_familia(personagem_de_familia) -> List[Text]:
    frases_de_familia = []
    diretorio_de_familia = Path(ativos_de_familia, personagem_de_familia)
    for frase_de_familia in diretorio_de_familia.iterdir():
        frases_de_familia.append(frase_de_familia.stem)
    return frases_de_familia


@click.command()
@click.option(
    '-p',
    '--personagem-de-familia',
    default='jailson',
    help='Personagem de Família',
    type=click.Choice(listar_personagens_de_familia()),
    autocompletion=autocompletar_personagem_de_familia
)
@click.option(
    '-f',
    '--frase-de-familia',
    default='ai',
    help='Frase de Família',
    autocompletion=autocompletar_frase_de_familia
)
def entrypoint_de_familia(personagem_de_familia, frase_de_familia):
    audio = obter_audio_de_familia(
        personagem_de_familia,
        frase_de_familia
    )
    playsound(audio)


if __name__ == '__main__':
    configurar_autocomplete()
    entrypoint_de_familia()
