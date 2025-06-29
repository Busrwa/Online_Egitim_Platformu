"""Add category_id to courses

Revision ID: b46fff274949
Revises: a5606fa61771
Create Date: 2025-06-18 17:42:02.707957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b46fff274949'
down_revision: Union[str, None] = 'a5606fa61771'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('category_id', sa.Integer(), nullable=True))
    op.alter_column('courses', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('courses', 'description',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)
    op.drop_index('ix_courses_id', table_name='courses')
    op.create_foreign_key(None, 'courses', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.create_index('ix_courses_id', 'courses', ['id'], unique=False)
    op.alter_column('courses', 'description',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('courses', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_column('courses', 'category_id')
    # ### end Alembic commands ###
