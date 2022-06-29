"""added user and breed tables

Revision ID: f25d7d593eaf
Revises: 
Create Date: 2022-06-21 17:53:30.578135

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f25d7d593eaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('breed',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('breed', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('login', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )


def downgrade():
    op.drop_table('user')
    op.drop_table('breed')
