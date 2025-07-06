"""01_create_roles_table

Revision ID: d3b9581b559b
Revises: 
Create Date: 2025-07-06 17:30:11.412281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3b9581b559b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), unique=True),
        sa.Column("description", sa.String(255))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("roles")
