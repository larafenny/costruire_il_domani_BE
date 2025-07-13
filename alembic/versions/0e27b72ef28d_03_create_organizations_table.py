"""03_create_organizations_table

Revision ID: 0e27b72ef28d
Revises: 62a41e75006a
Create Date: 2025-07-13 15:52:29.604484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e27b72ef28d'
down_revision: Union[str, Sequence[str], None] = '62a41e75006a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'organizations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text),
        sa.Column('cf', sa.String(255), nullable=False, unique=True),
        sa.Column('p_iva', sa.String(255), nullable=False, unique=True),
        sa.Column('is_partner', sa.Boolean(), server_default=sa.text('0')),
        sa.Column('deleted', sa.Boolean(), server_default=sa.text('0')),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('organizations')

