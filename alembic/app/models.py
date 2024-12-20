from sqlalchemy import Column, String, Integer, ForeignKey, Text, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# Define the base class for ORM models
Base = declarative_base()

# Define the BeautyProduct model
class BeautyProduct(Base):
    __tablename__ = "beauty_products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)  # e.g., Skincare, Makeup
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    rating = Column(Float, nullable=True)  # Rating between 1-5 stars
    
    # Relationship with RoutineProducts table (many-to-many with BeautyRoutine)
    routines = relationship("RoutineProduct", back_populates="product")
    
    def __repr__(self):
        return f"<BeautyProduct(name={self.name}, type={self.type}, rating={self.rating})>"

# Define the BeautyRoutine model
class BeautyRoutine(Base):
    __tablename__ = "beauty_routines"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    frequency = Column(String(50), nullable=True)  # E.g., Daily, Weekly
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship with RoutineProducts table (many-to-many with BeautyProduct)
    products = relationship("RoutineProduct", back_populates="routine")
    
    def __repr__(self):
        return f"<BeautyRoutine(name={self.name}, frequency={self.frequency})>"

# Define the RoutineProduct model (junction table for many-to-many relationship)
class RoutineProduct(Base):
    __tablename__ = "routine_products"
    
    id = Column(Integer, primary_key=True)
    routine_id = Column(Integer, ForeignKey('beauty_routines.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('beauty_products.id'), nullable=False)
    step = Column(Integer, nullable=False)  # Step number in the routine (1, 2, 3, etc.)
    
    # Relationships to connect the products and routines
    routine = relationship("BeautyRoutine", back_populates="products")
    product = relationship("BeautyProduct", back_populates="routines")
    
    def __repr__(self):
        return f"<RoutineProduct(routine_id={self.routine_id}, product_id={self.product_id}, step={self.step})>"
