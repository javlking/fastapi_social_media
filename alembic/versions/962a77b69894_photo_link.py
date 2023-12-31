"""photo_link

Revision ID: 962a77b69894
Revises: 76f62e274d4e
Create Date: 2023-09-09 18:09:48.304693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '962a77b69894'
down_revision: Union[str, None] = '76f62e274d4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_posts', sa.Column('photo_link_p', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_posts', 'photo_link_p')
    # ### end Alembic commands ###
