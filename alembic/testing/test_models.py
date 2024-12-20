import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, BeautyProduct, BeautyRoutine, RoutineProduct

# Test Setup - In-memory SQLite database
@pytest.fixture(scope="module")
def test_db_session():
    # Create a temporary in-memory database for testing
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Yield the session to test functions
    yield session

    # Cleanup after tests
    session.close()
    Base.metadata.drop_all(engine)

# Test for adding a beauty product
def test_add_beauty_product(test_db_session):
    product = BeautyProduct(name="Face Cream", type="Skincare", description="Moisturizing face cream")
    test_db_session.add(product)
    test_db_session.commit()
    
    # Verify the product is added
    product_from_db = test_db_session.query(BeautyProduct).filter_by(name="Face Cream").first()
    assert product_from_db is not None
    assert product_from_db.name == "Face Cream"
    assert product_from_db.type == "Skincare"
    assert product_from_db.description == "Moisturizing face cream"
    assert product_from_db.rating is None  # No rating by default

# Test for updating a beauty product
def test_update_beauty_product(test_db_session):
    product = BeautyProduct(name="Lipstick", type="Makeup", description="Red lipstick")
    test_db_session.add(product)
    test_db_session.commit()

    product.id = 1  # Assuming the product's ID is 1 after insertion
    updated_product = test_db_session.query(BeautyProduct).get(1)
    updated_product.name = "Red Lipstick"
    updated_product.description = "Bright red lipstick"
    test_db_session.commit()

    # Verify the update
    product_from_db = test_db_session.query(BeautyProduct).get(1)
    assert product_from_db.name == "Red Lipstick"
    assert product_from_db.description == "Bright red lipstick"

# Test for deleting a beauty product
def test_delete_beauty_product(test_db_session):
    product = BeautyProduct(name="Foundation", type="Makeup", description="Matte foundation")
    test_db_session.add(product)
    test_db_session.commit()

    product_from_db = test_db_session.query(BeautyProduct).filter_by(name="Foundation").first()
    test_db_session.delete(product_from_db)
    test_db_session.commit()

    # Verify the product is deleted
    product_from_db = test_db_session.query(BeautyProduct).filter_by(name="Foundation").first()
    assert product_from_db is None

# Test for setting a valid rating
def test_set_valid_rating(test_db_session):
    product = BeautyProduct(name="Lipstick", type="Makeup", description="Red lipstick")
    test_db_session.add(product)
    test_db_session.commit()

    # Set a valid rating (between 1 and 5)
    product.set_rating(4.5)
    test_db_session.commit()

    # Verify the rating is set
    product_from_db = test_db_session.query(BeautyProduct).filter_by(name="Lipstick").first()
    assert product_from_db.rating == 4.5

# Test for setting an invalid rating
def test_set_invalid_rating(test_db_session):
    product = BeautyProduct(name="Lipstick", type="Makeup", description="Red lipstick")
    test_db_session.add(product)
    test_db_session.commit()

    # Try setting an invalid rating (greater than 5)
    with pytest.raises(ValueError, match="Rating must be between 1 and 5."):
        product.set_rating(6)  # Invalid rating, should raise ValueError

# Test for adding a beauty routine
def test_add_beauty_routine(test_db_session):
    routine = BeautyRoutine(name="Morning Routine", frequency="Daily")
    test_db_session.add(routine)
    test_db_session.commit()

    # Verify the routine is added
    routine_from_db = test_db_session.query(BeautyRoutine).filter_by(name="Morning Routine").first()
    assert routine_from_db is not None
    assert routine_from_db.name == "Morning Routine"
    assert routine_from_db.frequency == "Daily"

# Test for assigning a product to a routine
def test_assign_product_to_routine(test_db_session):
    product = BeautyProduct(name="Eye Cream", type="Skincare", description="Hydrating eye cream")
    routine = BeautyRoutine(name="Morning Routine", frequency="Daily")
    
    test_db_session.add(product)
    test_db_session.add(routine)
    test_db_session.commit()

    # Now assign product to routine
    routine_product = RoutineProduct(routine_id=routine.id, product_id=product.id, step=1)
    test_db_session.add(routine_product)
    test_db_session.commit()

    # Verify the assignment
    routine_product_from_db = test_db_session.query(RoutineProduct).filter_by(routine_id=routine.id, product_id=product.id).first()
    assert routine_product_from_db is not None
    assert routine_product_from_db.step == 1

# Test for deleting a beauty routine
def test_delete_beauty_routine(test_db_session):
    routine = BeautyRoutine(name="Weekly Routine", frequency="Weekly")
    test_db_session.add(routine)
    test_db_session.commit()

    routine_from_db = test_db_session.query(BeautyRoutine).filter_by(name="Weekly Routine").first()
    test_db_session.delete(routine_from_db)
    test_db_session.commit()

    # Verify the routine is deleted
    routine_from_db = test_db_session.query(BeautyRoutine).filter_by(name="Weekly Routine").first()
    assert routine_from_db is None
