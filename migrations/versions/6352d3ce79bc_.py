"""empty message

Revision ID: 6352d3ce79bc
Revises: f9b8836512a4
Create Date: 2021-09-15 21:05:56.862742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6352d3ce79bc'
down_revision = 'f9b8836512a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
