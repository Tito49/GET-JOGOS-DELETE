# Importa o objeto db responsável pela conexão com o banco
from db import db


# =========================================
# MODEL JOGO
# =========================================

class Jogo(db.Model):

    # Nome da tabela no banco
    __tablename__ = 'jogos'

    # Colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    desenvolvedor = db.Column(db.String(100), nullable=False)
    plataforma = db.Column(db.String(100), nullable=False)

    # Retorna os dados em formato JSON
    def json(self):

        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'desenvolvedor': self.desenvolvedor,
            'plataforma': self.plataforma
        }