"""empty message

Revision ID: 7c7ada8f5308
Revises: a30c9fc3949b
Create Date: 2021-02-17 14:59:06.912073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c7ada8f5308'
down_revision = 'a30c9fc3949b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises_muscles',
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('muscle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['muscle_id'], ['muscles.id'], ),
    sa.PrimaryKeyConstraint('exercise_id', 'muscle_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercises_muscles')
    # ### end Alembic commands ###
