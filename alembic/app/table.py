from config import engine 
from models import Base # Import the models you created

# Create all tables in the database
Base.metadata.create_all(bind=engine)
