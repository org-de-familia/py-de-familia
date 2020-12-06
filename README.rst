.. raw:: html

    <p align="center">
        <a href="#readme">
            <img alt="py-de-família logo" src="https://github.com/augustoliks/py-de-familia/blob/main/docs/source/_static/logo-with-desc.png?raw=true">
        </a>
    </p>

    <p align="center">
        <a href="https://badge.fury.io/py/py-de-familia">
            <img alt="Pypi version" src="https://badge.fury.io/py/py-de-familia.svg">
        </a>
        <a href='https://py-de-familia.readthedocs.io/en/latest/?badge=latest'>
            <img src='https://readthedocs.org/projects/py-de-familia/badge/?version=latest' alt='Documentation Status' />
        </a>
        <a href="https://codecov.io/gh/augustoliks/py-de-familia">
          <img src="https://codecov.io/gh/augustoliks/py-de-familia/branch/main/graph/badge.svg?token=EHJKGJKW3T"/>
        </a>
        <a href="https://www.codacy.com/gh/augustoliks/py-de-familia/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=augustoliks/py-de-familia&amp;utm_campaign=Badge_Grade">
            <img src="https://app.codacy.com/project/badge/Grade/2f6923d397794cec937347e9c792d1dc"/>
        </a>
    </p>

=========

É Essa Biblioteca Que Você Queria???
====================================

``py-de-família`` é uma CLI deliciosa, criada no intuíto de relaxar os Programadores de Família.

Nela é possível ouvir diretamente do seu terminal, as frases relexantes do mestre Jailson Mendes e de outros personagens do universo PDF.

.. end-of-readme-intro

*Features* de Família
=====================

Atualmente, é possível apreciar os aúdios relexantes dos seguintes personagens de família:

+-------------------------------+----------------------------------+--------------------------------------------------------+
| Personagem de Família         | Filmes de Família                | Biografia de Família                                   |
+===============================+==================================+========================================================+
| Jailson Mendes de Família     | Trilogia Pai de Família          | https://desciclopedia.org/wiki/Pai_de_Fam%C3%ADlia     |
+-------------------------------+----------------------------------+--------------------------------------------------------+
| Kauan Desu de Família         | Trilogia Pai de Família          | https://desciclopedia.org/wiki/Kauan_Desu              |
+-------------------------------+----------------------------------+--------------------------------------------------------+
| Paulo Guina de Família        | Trilogia Pai de Família          | https://desciclopedia.org/wiki/Paulo_Guina             |
+-------------------------------+----------------------------------+--------------------------------------------------------+
| Boliviano de Família          | Princesa Demacol e o Boliviano   | http://desciclo.pedia.ws/wiki/Boliviano                |
+-------------------------------+----------------------------------+--------------------------------------------------------+

Instalação
==========

.. code-block:: shell

    # Instalação da biblioteca de familia
    $ pip3 install py-de-familia

    # Habilitando o autocomplete de familia
    $ eval "$(_PY_DE_FAMILIA_COMPLETE=source_bash py-de-familia)"

Execução
========

TODO

Estrutura do Projeto de Família
===============================

::

    ├── CODE-OF-CONDUCT-DE-FAMILIA.rst  # Código de conduta de Família
    ├── docs                            # Documentação de Família
    │   └── ...
    ├── LICENSE-DE-FAMILIA              # Descrição da Licença APAICHE-DE-FAMILIA-2.0
    ├── Makefile                        # Makefile de Família para extrair audios de família do youtube
    ├── poetry.lock                     # Dependencias de Família Versionadas
    ├── py_de_familia
    │   ├── ativos-de-familia
    │   │   ├── boliviano               # Audios do Boliviano de Família
    │   │   │   └── ...
    │   │   ├── jailson                 # Audios do Jailson Mendes de Família
    │   │   │   └── ...
    │   │   ├── kauan-desu              # Audios do Kauan Desu de Família
    │   │   │   └── ...
    │   │   └── pau-guina               # Audios do Paulo Guina de Família
    │   │       └── ...
    │   ├── autocomplete-de-familia.sh  # Shell Script Para habilitar o auto-complete
    │   └── clidefamilia.py             # Código Fonte de Família
    ├── pyproject.toml                  # Metadados do projeto de família
    ├── README.rst                      # Documentação de família
    └── tests                           # Testes de Família
        ├── __pycache__
        └── test_clidefamilia.py        # Testes unitários de Família, que seja pequeneninho mais que seja garantido

Licença de Família
==================

``py-de-família`` é uma biblioteca *open-source*. Todo o desenvolvimento foi feito sobre a Licença **APAICHE-DE-FAMILIA-2.0**.

Essa licença, tem como restrição, o tipo do Desenvolvedor atuante no o projeto. É aceito apenas:

* Héteros;
* Machos;
* Ursos; e
* Lolitos.

A licença é baseada nas licenças **PAPAKU** e **KUKÉPAU**, criadas respectivamente nas cidades de **Cú Pequeno** e **Pau Grande**.

Contribuições de Família
========================

Para contribuir para com o código fonte, é necessário seguir o Código de Conduta deste projeto.

Para adicionar mais audios relexantes, basta utilizar o ``Makefile`` de familia. Este tem seções que utilizam os utilitários ``youtube-dl`` e ``ffmpeg`` para baixar e converter os audios respectivamente.
