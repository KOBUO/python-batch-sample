import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (
    'root',
    'your_password',
    'sample-batch_db_1',
    '3306',
    'test_db'
)

ENGINE = sqlalchemy.create_engine(
    DATABASE,
    encoding='utf-8',
    echo=False)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()

if __name__ == '__main__':
    Base.metadata.create_all(bind=ENGINE)
