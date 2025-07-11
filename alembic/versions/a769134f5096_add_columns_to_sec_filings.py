"""add columns to sec_filings

Revision ID: a769134f5096
Revises: 715250acf2a7
Create Date: 2025-07-08 13:14:51.980520

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a769134f5096"
down_revision: Union[str, Sequence[str], None] = "715250acf2a7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("sec_filings", sa.Column("format", sa.Text(), nullable=True))
    op.add_column("sec_filings", sa.Column("parsed_at", sa.TIMESTAMP(timezone=True)))
    op.add_column("sec_filings", sa.Column("parse_ok", sa.Boolean(), default=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("sec_filings", "parse_ok")
    op.drop_column("sec_filings", "parsed_at")
    op.drop_column("sec_filings", "format")
