"""add foreign key to post table

Revision ID: 13833ba7204f
Revises: 7377daa8506a
Create Date: 2022-10-01 18:27:04.341353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13833ba7204f'
down_revision = '7377daa8506a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id' , sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk' , source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass

 
def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('owner_id','posts')
    pass
