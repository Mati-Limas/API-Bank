import sqlalchemy as sa
from database import metadata

contas = sa.Table('contas',
                  metadata,
                  sa.Column('id', sa.Integer, primary_key=True),
                  sa.Column('usuario', sa.String(100), nullable=False, unique=True),
                  sa.Column('senha', sa.String(200), nullable=False),
                  sa.Column('saldo', sa.Float, nullable=False, default=0.0)
                  )