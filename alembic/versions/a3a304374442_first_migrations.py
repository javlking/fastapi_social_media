"""first migrations

Revision ID: a3a304374442
Revises: 3e206228281f
Create Date: 2023-09-09 17:54:18.961435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3a304374442'
down_revision: Union[str, None] = '3e206228281f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
