from flask import Flask
from db import db
from routes.jogo_routes import jogo_routes

# =========================================
# CRIA A APLICAÇÃO FLASK
# =========================================

app = Flask(__name__)

# =========================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# =========================================

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogos.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# =========================================
# INICIALIZA O BANCO
# =========================================

db.init_app(app)

# =========================================
# REGISTRA AS ROTAS
# =========================================

app.register_blueprint(jogo_routes)

# =========================================
# EXECUTA A APLICAÇÃO
# =========================================

if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    app.run(debug=True)