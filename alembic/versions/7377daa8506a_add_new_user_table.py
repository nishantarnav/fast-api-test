"""add new user table

Revision ID: 7377daa8506a
Revises: df87f87e0beb
Create Date: 2022-10-01 18:17:45.291200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7377daa8506a'
down_revision = 'df87f87e0beb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                            sa.Column('id', sa.Integer(), nullable=False),
                            sa.Column('email' , sa.String(), nullable=False),
                            sa.Column('password' , sa.String(), nullable=False),
                            sa.Column('created_at' , sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email')
                             )


def downgrade() -> None:
    pass
