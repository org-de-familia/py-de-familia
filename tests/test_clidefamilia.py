# testes unitários de familia

from py_de_familia import cli


def test_listar_personagens_de_familia():
    obtido = cli.listar_personagens_de_familia()
    esperado = ['pau-guina', 'boliviano', 'kauan-desu', 'jailson']
    assert sorted(esperado) == sorted(obtido)


def test_listar_frases_de_familia():
    obtido = cli.listar_frases_de_familia('jailson')
    esperado = [
        'ai',
        'ai-eu-nao-resisto',
        'como-assim-caralho',
        'essa-peca-que-voce-queria',
        'grande-e-gostosa',
        'nao-cara',
        'que-delicia',
        'queimando-uma-rosquinha',
        'tive-tanto-trabalho-para-buscar-essa-peca',
        'trabalhando-e-relexando'
    ]
    assert sorted(obtido) == sorted(esperado)
