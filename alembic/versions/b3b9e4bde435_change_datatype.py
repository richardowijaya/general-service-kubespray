"""change_datatype

Revision ID: b3b9e4bde435
Revises: 509efb176e41
Create Date: 2023-03-30 14:57:42.463391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3b9e4bde435'
down_revision = '509efb176e41'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("mtr_province",column_name="province_code",existing_nullable=False,existing_type=sa.Integer,new_column_name="province_code",nullable=False,type=sa.String(100))


def downgrade() -> None:
    pass
