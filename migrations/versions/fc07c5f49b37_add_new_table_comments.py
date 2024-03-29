"""Add new table comments

Revision ID: fc07c5f49b37
Revises: 74fc2c59fa4e
Create Date: 2019-11-25 16:14:05.895618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc07c5f49b37'
down_revision = '74fc2c59fa4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
