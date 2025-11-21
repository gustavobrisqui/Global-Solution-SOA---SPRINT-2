from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('usuarios',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(100), nullable=False),
        sa.Column('email', sa.String(150), nullable=False, unique=True),
        sa.Column('area_atuacao', sa.String(100)),
        sa.Column('nivel_carreira', sa.String(50)),
        sa.Column('data_cadastro', sa.Date, nullable=False)
    )

    op.create_table('trilhas',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(150), nullable=False),
        sa.Column('descricao', sa.Text),
        sa.Column('nivel', sa.String(50), nullable=False),
        sa.Column('carga_horaria', sa.Integer, nullable=False),
        sa.Column('foco_principal', sa.String(100))
    )

    op.create_table('matriculas',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey("usuarios.id"), nullable=False),
        sa.Column('trilha_id', sa.Integer, sa.ForeignKey("trilhas.id"), nullable=False),
        sa.Column('data_inscricao', sa.Date, nullable=False),
        sa.Column('status', sa.String(50), nullable=False)
    )

def downgrade():
    op.drop_table('matriculas')
    op.drop_table('trilhas')
    op.drop_table('usuarios')
