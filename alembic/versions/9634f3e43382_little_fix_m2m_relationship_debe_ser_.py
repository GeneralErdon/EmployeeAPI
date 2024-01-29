"""Little fix M2M relationship, debe ser una instancia de Table()

Revision ID: 9634f3e43382
Revises: 68eabb1ea3d7
Create Date: 2024-01-24 08:22:03.965205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9634f3e43382'
down_revision: Union[str, None] = '68eabb1ea3d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_empleado_bono_id'), 'empleado_bono', ['id'], unique=False)
    op.drop_column('empleado_bono', 'modified_date')
    op.drop_column('empleado_bono', 'created_date')
    op.drop_column('empleado_bono', 'status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('empleado_bono', sa.Column('status', sa.BOOLEAN(), nullable=True))
    op.add_column('empleado_bono', sa.Column('created_date', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('empleado_bono', sa.Column('modified_date', sa.DATETIME(), nullable=True))
    op.drop_index(op.f('ix_empleado_bono_id'), table_name='empleado_bono')
    # ### end Alembic commands ###