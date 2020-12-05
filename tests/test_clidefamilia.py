"""testes unitários de familia"""

import clidefamilia


def test_listar_personagens_de_familia():
    obtido = clidefamilia.listar_personagens_de_familia()
    esperado = ['pau-guina', 'boliviano', 'kauan-desu', 'jailson']
    assert sorted(esperado) == sorted(obtido)


def test_listar_frases_de_familia():
    obtido = clidefamilia.listar_frases_de_familia('jailson')
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
