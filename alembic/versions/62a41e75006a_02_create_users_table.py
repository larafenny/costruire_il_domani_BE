"""02_create_users_table

Revision ID: 62a41e75006a
Revises: d3b9581b559b
Create Date: 2025-07-06 17:41:48.346812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62a41e75006a'
down_revision: Union[str, Sequence[str], None] = 'd3b9581b559b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255)),
        sa.Column("surname", sa.String(255)),
        sa.Column("email", sa.String(255), unique=True, nullable=False),
        sa.Column("email_verified_at", sa.DateTime()),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column("status", sa.Enum("active", "inactive", "blocked", "pending", name="user_status"), server_default="pending", nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP),
        sa.Column("last_access_at", sa.TIMESTAMP),
        sa.Column("role_id", sa.Integer, sa.ForeignKey("roles.id")),
        sa.Column("deleted", sa.Boolean, nullable=False, server_default=sa.text("0"))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
