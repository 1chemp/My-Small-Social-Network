"""Add interests table

Revision ID: 8f501c0c4164
Revises: 2d6c952ed814
Create Date: 2021-06-02 16:26:45.547833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f501c0c4164'
down_revision = '2d6c952ed814'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('interests', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('users', 'interests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('interests', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_table('interests')
    # ### end Alembic commands ###
