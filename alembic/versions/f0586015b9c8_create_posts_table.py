"""Create posts table

Revision ID: f0586015b9c8
Revises: 
Create Date: 2023-12-11 14:31:06.535368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0586015b9c8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts", 
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_table("posts")
    pass
