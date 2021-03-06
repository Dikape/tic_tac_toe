"""empty message

Revision ID: 7bac6b011f81
Revises: fc0bc87df122
Create Date: 2018-02-18 15:34:30.069375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bac6b011f81'
down_revision = 'fc0bc87df122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('finished_datetime', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'finished_datetime')
    # ### end Alembic commands ###
