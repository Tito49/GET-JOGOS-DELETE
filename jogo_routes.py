from flask import Blueprint, request

from controllers.jogo_controllers import (
    get_jogos,
    get_jogo_by_id,
    create_jogo,
    update_jogo,
    delete_jogo
)

# =========================================
# BLUEPRINT DAS ROTAS
# =========================================

jogo_routes = Blueprint('jogo_routes', __name__)


# =========================================
# GET - LISTAR TODOS OS JOGOS
# =========================================

@jogo_routes.route('/jogos', methods=['GET'])
def jogos_get():

    return get_jogos()


# =========================================
# GET - BUSCAR JOGO POR ID
# =========================================

@jogo_routes.route('/jogos/<int:jogo_id>', methods=['GET'])
def jogo_get_by_id(jogo_id):

    return get_jogo_by_id(jogo_id)


# =========================================
# POST - CRIAR JOGO
# =========================================

@jogo_routes.route('/jogos', methods=['POST'])
def jogos_post():

    return create_jogo(request.json)


# =========================================
# PUT - ATUALIZAR JOGO
# =========================================

@jogo_routes.route('/jogos/<int:jogo_id>', methods=['PUT'])
def jogos_put(jogo_id):

    return update_jogo(jogo_id, request.json)


# =========================================
# DELETE - REMOVER JOGO
# =========================================

@jogo_routes.route('/jogos/<int:jogo_id>', methods=['DELETE'])
def jogos_delete(jogo_id):

    return delete_jogo(jogo_id)