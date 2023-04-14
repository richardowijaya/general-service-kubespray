from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configs.config import Settings

check = Settings()

#server = 'nomad2805'
#database = 'DMSTEST'

database_url = f"mssql+pymssql://{check.db_user}:{check.db_password}@{check.db_server}/{check.db_name}" #MSSQL SERVER
#database_url = 'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server'
#database_url = f"postgresql://{check.db_user}:{check.db_password}@{check.db_server}:{check.db_port}/{check.db_name}" #POSTGRESQL

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()