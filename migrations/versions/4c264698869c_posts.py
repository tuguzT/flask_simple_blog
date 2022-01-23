"""posts

Revision ID: 4c264698869c
Revises: ab101e5cee94
Create Date: 2022-01-23 16:14:07.462015

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4c264698869c'
down_revision = 'ab101e5cee94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
                    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('create_datetime', sa.DateTime(), nullable=False),
                    sa.Column('title', sa.String(length=100), nullable=False),
                    sa.Column('text_content', sa.Text(), nullable=False),
                    sa.Column('author_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.ForeignKeyConstraint(('author_id',), ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_post_create_datetime'), 'post', ['create_datetime'], unique=False)
    op.create_index(op.f('ix_post_title'), 'post', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_title'), table_name='post')
    op.drop_index(op.f('ix_post_create_datetime'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
