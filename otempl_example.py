#!/usr/bin/env python3

import otempl

dot_template = {
    'base': [
        '''digraph G {
          compound=true
          newrank=true
          rankdir = LR

          labelloc="t"
          label="
            ${titulo}
            ${versao}

            ${produto}

        ''',
        {'type': 'loop',
         'dict': 'caracteristicas',
         'repeat': '''${fase}
            '''},
        '"',
        ('conteudo',),
        '}\n',
    ],
    'conteudo': [
        '''
        Oi_${mundo}
        '''
    ]
}

dot_values = {
    "base": {
        "titulo": "Fluxo 1 - Interno",
        "versao": "Versão 19.01 (07/02/2019)",
        "produto": "CUECA COM costura - PRAIA - SHORT",
        "caracteristicas": {
            "fase": [
              "Corte: Interno",
              "Estamparia: Interna ou Sem",
              "Costura: Interna",
            ]
        },
    },
    "conteudo": {
        "mundo": "Mundo"
    }
}

ot = otempl.OTempl(dot_template, dot_values)
ot.mount()
