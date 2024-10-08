"""refactore all shemas and models

Revision ID: cc979a6b39a8
Revises: 860c947cc40e
Create Date: 2024-10-02 15:06:54.524162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'cc979a6b39a8'
down_revision: Union[str, None] = '860c947cc40e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('bookings', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('rooms', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('rooms', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('rooms', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('rooms', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('bookings', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('bookings', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
