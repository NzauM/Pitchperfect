"""Add a new table pitches

Revision ID: 2860a03c61f2
Revises: feabe226b91a
Create Date: 2019-11-23 19:57:14.343264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2860a03c61f2'
down_revision = 'feabe226b91a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('pitch', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    # ### end Alembic commands ###
