"""adding the rest columns

Revision ID: 3674ea491064
Revises: 13833ba7204f
Create Date: 2022-10-01 18:41:42.749322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3674ea491064'
down_revision = '13833ba7204f'
branch_labels = None
depends_on = None
 

def upgrade() -> None:
    op.add_column('posts' , sa.Column('published' , sa.Boolean(), nullable=False, server_default= 'TRUE'),)
    op.add_column('posts' , sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','publised')
    op.drop_column('posts','created_at')
    pass
