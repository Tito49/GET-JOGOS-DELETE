from models.jogo_models import Jogo
from db import db
import json
from flask import make_response

# =========================================
# JOGOS PADRÃO PARA O BANCO
# =========================================

def inserir_jogos_padrao():

    jogos_padrao = [
        {
            "titulo": "Red Dead Redemption 2",
            "genero": "Ação e Aventura",
            "desenvolvedor": "Rockstar Games",
            "plataforma": "PC"
        },
        {
            "titulo": "Resident Evil 4",
            "genero": "Survival Horror",
            "desenvolvedor": "Capcom",
            "plataforma": "PlayStation 5"
        },
        {
            "titulo": "Minecraft",
            "genero": "Sandbox",
            "desenvolvedor": "Mojang",
            "plataforma": "PC"
        },
        {
            "titulo": "Roblox",
            "genero": "Sandbox",
            "desenvolvedor": "Roblox Corporation",
            "plataforma": "PC"
        },
        {
            "titulo": "The Last Of Us",
            "genero": "Ação e Drama",
            "desenvolvedor": "Naughty Dog",
            "plataforma": "PlayStation 5"
        }
    ]

    # Só adiciona se o banco estiver vazio
    if len(Jogo.query.all()) == 0:

        for jogo in jogos_padrao:

            novo_jogo = Jogo(
                titulo=jogo["titulo"],
                genero=jogo["genero"],
                desenvolvedor=jogo["desenvolvedor"],
                plataforma=jogo["plataforma"]
            )

            db.session.add(novo_jogo)

        db.session.commit()


# =========================================
# GET TODOS OS JOGOS
# =========================================

def get_jogos():

    inserir_jogos_padrao()

    jogos = Jogo.query.all()

    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogos.',
            'dados': [jogo.json() for jogo in jogos]
        }, ensure_ascii=False, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response


# =========================================
# GET JOGO POR ID
# =========================================

def get_jogo_by_id(jogo_id):

    jogo = Jogo.query.get(jogo_id)

    if jogo:

        response = make_response(
            json.dumps({
                'mensagem': 'Jogo encontrado.',
                'dados': jogo.json()
            }, ensure_ascii=False, sort_keys=False)
        )

        response.headers['Content-Type'] = 'application/json'
        return response

    else:

        response = make_response(
            json.dumps({
                'mensagem': 'Jogo não encontrado.',
                'dados': {}
            }, ensure_ascii=False),
            404
        )

        response.headers['Content-Type'] = 'application/json'
        return response


# =========================================
# POST - CRIAR JOGO
# =========================================

def create_jogo(jogo_data):

    if not all(key in jogo_data for key in ['titulo', 'genero', 'desenvolvedor', 'plataforma']):

        response = make_response(
            json.dumps({
                'mensagem': 'Dados inválidos.'
            }, ensure_ascii=False),
            400
        )

        response.headers['Content-Type'] = 'application/json'
        return response

    novo_jogo = Jogo(
        titulo=jogo_data['titulo'],
        genero=jogo_data['genero'],
        desenvolvedor=jogo_data['desenvolvedor'],
        plataforma=jogo_data['plataforma']
    )

    db.session.add(novo_jogo)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Jogo cadastrado com sucesso.',
            'jogo': novo_jogo.json()
        }, ensure_ascii=False, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response


# =========================================
# PUT - ATUALIZAR JOGO
# =========================================

def update_jogo(jogo_id, jogo_data):

    jogo = Jogo.query.get(jogo_id)

    if not jogo:

        response = make_response(
            json.dumps({
                'mensagem': 'Jogo não encontrado.'
            }, ensure_ascii=False),
            404
        )

        response.headers['Content-Type'] = 'application/json'
        return response

    jogo.titulo = jogo_data['titulo']
    jogo.genero = jogo_data['genero']
    jogo.desenvolvedor = jogo_data['desenvolvedor']
    jogo.plataforma = jogo_data['plataforma']

    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Jogo atualizado com sucesso.',
            'jogo': jogo.json()
        }, ensure_ascii=False, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response


# =========================================
# DELETE - REMOVER JOGO
# =========================================

def delete_jogo(jogo_id):

    jogo = Jogo.query.get(jogo_id)

    if not jogo:

        response = make_response(
            json.dumps({
                'mensagem': 'Jogo não encontrado.'
            }, ensure_ascii=False),
            404
        )

        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(jogo)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Jogo removido com sucesso.'
        }, ensure_ascii=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response