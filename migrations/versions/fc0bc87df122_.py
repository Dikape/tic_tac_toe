"""empty message

Revision ID: fc0bc87df122
Revises: ef5cac8df619
Create Date: 2018-02-18 13:04:00.971760

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

# revision identifiers, used by Alembic.
revision = 'fc0bc87df122'
down_revision = 'ef5cac8df619'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_step_member_id'), 'step', ['member_id'], unique=False)
    op.create_index(op.f('ix_step_x_coordinate'), 'step', ['x_coordinate'], unique=False)
    op.create_index(op.f('ix_step_y_coordinate'), 'step', ['y_coordinate'], unique=False)
    # ### end Alembic commands ###
    status_table = table('status',
                         column('id', Integer),
                         column('status', String),
                         )

    op.bulk_insert(status_table,
                   [
                       {'id': 1, 'status': 'winner'},
                       {'id': 2, 'status': 'loser'},
                       {'id': 3, 'status': 'draw'},
                   ]
                   )

    accounts_table = table('game_type',
                           column('id', Integer),
                           column('title', String),
                           )

    op.bulk_insert(accounts_table,
                   [
                       {'id': 1, 'title': 'hot_seat'},
                       {'id': 2, 'title': 'online'},
                   ]
                   )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_step_y_coordinate'), table_name='step')
    op.drop_index(op.f('ix_step_x_coordinate'), table_name='step')
    op.drop_index(op.f('ix_step_member_id'), table_name='step')
    # ### end Alembic commands ###