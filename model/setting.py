from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE = 'mssql+pymssql://%s:%s@%s:%s/%s?charset=utf8' % (
    'SA',
    '4iF5uTjJ8vJG0YGL',
    'sqlserver',
    '1433',
    'TestDB'
)

ENGINE = create_engine(
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
