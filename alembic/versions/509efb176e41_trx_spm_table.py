"""trx_spm table

Revision ID: 509efb176e41
Revises: 
Create Date: 2023-03-20 16:11:58.813619

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column,Boolean,Integer,String,DateTime


# revision identifiers, used by Alembic.
revision = '509efb176e41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "trx_spm_form_registration", 
        Column("is_active",Boolean,nullable=False,default=True),
        Column("company_id",Integer,nullable=False),
        Column("register_system_number",Integer, nullable=False, primary_key=True),
        Column("registered_document_number",Integer,nullable=False),
        Column("spm_received_by",String(8),nullable=False),
        Column("spm_received_date",DateTime,nullable=False),
        Column("spm_number_format",String(20),nullable=False),
        Column("spm_number_from",Integer,nullable=False),
        Column("total_spm",Integer,nullable=False)
    )


def downgrade() -> None:
    pass
