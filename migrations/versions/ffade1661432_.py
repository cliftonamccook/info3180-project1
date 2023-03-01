"""empty message

Revision ID: ffade1661432
Revises: 869df7b4358e
Create Date: 2023-02-28 23:09:29.429797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffade1661432'
down_revision = '869df7b4358e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('property_type', sa.String(length=10), nullable=True))
        batch_op.drop_column('type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
        batch_op.drop_column('property_type')

    # ### end Alembic commands ###
