"""empty message

Revision ID: ef5cac8df619
Revises: b882f83871b6
Create Date: 2018-02-17 23:41:28.822515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef5cac8df619'
down_revision = 'b882f83871b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('step', sa.Column('value', sa.String(length=1), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('step', 'value')
    # ### end Alembic commands ###