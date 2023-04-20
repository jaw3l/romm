"""init

Revision ID: 1.6.2
Revises: 
Create Date: 2023-04-10 23:02:37.472055

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError


# revision identifiers, used by Alembic.
revision = '1.6.2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.create_table('platforms',
            sa.Column('igdb_id', sa.String(length=10), nullable=True),
            sa.Column('sgdb_id', sa.String(length=10), nullable=True),
            sa.Column('slug', sa.String(length=50), nullable=False),
            sa.Column('name', sa.String(length=400), nullable=True),
            sa.Column('logo_path', sa.String(length=1000), nullable=True),
            sa.Column('n_roms', sa.Integer(), nullable=True),
            sa.PrimaryKeyConstraint('slug')
        )
        op.create_table('roms',
            sa.Column('r_igdb_id', sa.String(length=10), nullable=True),
            sa.Column('p_igdb_id', sa.String(length=10), nullable=True),
            sa.Column('r_sgdb_id', sa.String(length=10), nullable=True),
            sa.Column('p_sgdb_id', sa.String(length=10), nullable=True),
            sa.Column('p_slug', sa.String(length=50), nullable=False),
            sa.Column('file_name', sa.String(length=450), nullable=False),
            sa.Column('file_name_no_tags', sa.String(length=450), nullable=True),
            sa.Column('file_extension', sa.String(length=10), nullable=True),
            sa.Column('file_path', sa.String(length=1000), nullable=True),
            sa.Column('file_size', sa.Float(), nullable=True),
            sa.Column('name', sa.String(length=350), nullable=True),
            sa.Column('r_slug', sa.String(length=100), nullable=True),
            sa.Column('summary', sa.Text(), nullable=True),
            sa.Column('path_cover_s', sa.Text(), nullable=True),
            sa.Column('path_cover_l', sa.Text(), nullable=True),
            sa.Column('has_cover', sa.Boolean(), nullable=True),
            sa.Column('region', sa.String(length=20), nullable=True),
            sa.Column('revision', sa.String(length=20), nullable=True),
            sa.Column('tags', sa.JSON(), nullable=True),
            sa.PrimaryKeyConstraint('p_slug', 'file_name')
        )
    except OperationalError:
        pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
