"""photo_link_2

Revision ID: 1a7d5b42358f
Revises: 962a77b69894
Create Date: 2023-09-09 18:10:16.063289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a7d5b42358f'
down_revision: Union[str, None] = '962a77b69894'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_posts', 'photo_link_p')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_posts', sa.Column('photo_link_p', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
