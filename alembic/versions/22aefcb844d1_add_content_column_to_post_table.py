"""add content column to post table

Revision ID: 22aefcb844d1
Revises: f0586015b9c8
Create Date: 2023-12-11 14:41:27.115869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22aefcb844d1'
down_revision: Union[str, None] = 'f0586015b9c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
