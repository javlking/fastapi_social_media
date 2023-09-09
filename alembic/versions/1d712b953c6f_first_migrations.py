"""first migrations

Revision ID: 1d712b953c6f
Revises: a3a304374442
Create Date: 2023-09-09 17:55:23.791426

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d712b953c6f'
down_revision: Union[str, None] = 'a3a304374442'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
