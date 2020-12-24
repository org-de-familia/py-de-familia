"""o código é pequeninho mais é garantido"""

import domain
from playsound import playsound
import click


@click.command()
@click.option(
    '-p',
    '--personagem-de-familia',
    default='jailson',
    help='Personagem de Família',
    type=click.Choice(domain.listar_personagens_de_familia()),
    autocompletion=domain.autocompletar_personagem_de_familia
)
@click.option(
    '-f',
    '--frase-de-familia',
    default='ai',
    help='Frase de Família',
    autocompletion=domain.autocompletar_frase_de_familia
)
def entrypoint_de_familia(personagem_de_familia, frase_de_familia):
    audio = domain.obter_audio_de_familia(
        personagem_de_familia,
        frase_de_familia
    )
    playsound(audio)


if __name__ == '__main__':
    entrypoint_de_familia()
