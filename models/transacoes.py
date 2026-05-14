import sqlalchemy as sa
from database import metadata

transacoes = sa.Table('transacoes',
                      metadata,
                      sa.Column('id', sa.Integer, primary_key=True),
                      sa.Column('conta_id', sa.Integer, sa.ForeignKey('contas.id'), nullable=False),
                      sa.Column('tipo', sa.String(50), nullable=False),
                      sa.Column('valor', sa.Float, nullable=False),
                      sa.Column('data', sa.DateTime, nullable=False))