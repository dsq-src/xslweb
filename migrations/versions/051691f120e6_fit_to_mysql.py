"""fit to MySQL

Revision ID: 051691f120e6
Revises: None
Create Date: 2016-03-06 19:11:38.238238

"""

# revision identifiers, used by Alembic.
revision = '051691f120e6'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articleTypeSettings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('protected', sa.Boolean(), nullable=True),
    sa.Column('hide', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('blog_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('signature', sa.Text(), nullable=True),
    sa.Column('navbar', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog_view',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num_of_view', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('plugins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('articleTypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('introduction', sa.Text(), nullable=True),
    sa.Column('menu_id', sa.Integer(), nullable=True),
    sa.Column('setting_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], ),
    sa.ForeignKeyConstraint(['setting_id'], ['articleTypeSettings.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('num_of_view', sa.Integer(), nullable=True),
    sa.Column('articleType_id', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['articleType_id'], ['articleTypes.id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_articles_create_time'), 'articles', ['create_time'], unique=False)
    op.create_index(op.f('ix_articles_update_time'), 'articles', ['update_time'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_name', sa.String(length=64), nullable=True),
    sa.Column('author_email', sa.String(length=64), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('comment_type', sa.String(length=64), nullable=True),
    sa.Column('reply_to', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['comments.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    op.drop_table('comments')
    op.drop_index(op.f('ix_articles_update_time'), table_name='articles')
    op.drop_index(op.f('ix_articles_create_time'), table_name='articles')
    op.drop_table('articles')
    op.drop_table('articleTypes')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('sources')
    op.drop_table('plugins')
    op.drop_table('menus')
    op.drop_table('blog_view')
    op.drop_table('blog_info')
    op.drop_table('articleTypeSettings')
    ### end Alembic commands ###
