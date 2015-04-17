"""empty message

Revision ID: 1fb6e528ca58
Revises: 529d6d3b30bb
Create Date: 2015-04-17 20:05:43.165594

"""

# revision identifiers, used by Alembic.
revision = '1fb6e528ca58'
down_revision = '529d6d3b30bb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('roles', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('roles', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('roles', sa.Column('member_since', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'member_since')
    op.drop_column('roles', 'location')
    op.drop_column('roles', 'last_seen')
    op.drop_column('roles', 'about_me')
    ### end Alembic commands ###
