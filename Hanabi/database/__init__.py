
import databases
import sqlalchemy
import logging

logger = logging.getLogger("Database")

DATABASE_URL = "sqlite:///db.sqlite"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)



