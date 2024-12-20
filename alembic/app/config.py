from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create engine for SQLite database
engine = create_engine("sqlite:///beauty_routine_manager.db", echo=True)

# Create a sessionmaker to manage database connections
Session = sessionmaker(bind=engine)
session = Session()
