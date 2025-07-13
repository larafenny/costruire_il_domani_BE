"""04_create_files_table

Revision ID: 11c63f15fc08
Revises: 0e27b72ef28d
Create Date: 2025-07-13 15:59:54.353792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11c63f15fc08'
down_revision: Union[str, Sequence[str], None] = '0e27b72ef28d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'files',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('file_name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text),
        sa.Column('file_type', sa.Enum(
            'image', 'document', 'video', 'audio', 'archive', 'spreadsheet',
            'pdf', 'other', name='file_type'), nullable=False),
        sa.Column('size', sa.BIGINT),
        sa.Column('checksum', sa.String(255)),
        sa.Column('storage_disk', sa.String(255), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('organization_id', sa.Integer, sa.ForeignKey('organizations.id')),
        sa.Column('visibility', sa.Enum(
            'private', 'public', 'shared', name='file_visibility'), nullable=False),
        sa.Column('file_status', sa.Enum('active', 'archived', 'failed', name='file_status'), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('files')
