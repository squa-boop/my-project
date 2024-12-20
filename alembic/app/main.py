import os
from config import session
from models import BeautyProduct, BeautyRoutine, RoutineProduct

# CRUD operations for Beauty Products
def add_beauty_product():
    name = input("Enter the beauty product name: ")
    product_type = input("Enter the product type (e.g., Skincare, Makeup): ")
    description = input("Enter a description of the product: ")
    product = BeautyProduct(name=name, type=product_type, description=description)
    session.add(product)
    session.commit()
    print("Beauty product added successfully.")

def view_beauty_products():
    products = session.query(BeautyProduct).all()
    for product in products:
        print(f"{product.id} - {product.name} ({product.type})")

def update_beauty_product():
    product_id = int(input("Enter product ID to update: "))
    product = session.query(BeautyProduct).filter_by(id=product_id).first()
    if product:
        product.name = input(f"Enter new name (current: {product.name}): ")
        product.type = input(f"Enter new type (current: {product.type}): ")
        product.description = input(f"Enter new description (current: {product.description}): ")
        session.commit()
        print("Beauty product updated successfully.")
    else:
        print("Product not found.")

def delete_beauty_product():
    product_id = int(input("Enter product ID to delete: "))
    product = session.query(BeautyProduct).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print("Beauty product deleted successfully.")
    else:
        print("Product not found.")

# CRUD operations for Beauty Routines
def add_beauty_routine():
    name = input("Enter routine name: ")
    frequency = input("Enter routine frequency (e.g., Daily, Weekly): ")
    routine = BeautyRoutine(name=name, frequency=frequency)
    session.add(routine)
    session.commit()
    print("Beauty routine added successfully.")

def view_beauty_routines():
    routines = session.query(BeautyRoutine).all()
    for routine in routines:
        print(f"{routine.id} - {routine.name} ({routine.frequency})")

def update_beauty_routine():
    routine_id = int(input("Enter routine ID to update: "))
    routine = session.query(BeautyRoutine).filter_by(id=routine_id).first()
    if routine:
        routine.name = input(f"Enter new name (current: {routine.name}): ")
        routine.frequency = input(f"Enter new frequency (current: {routine.frequency}): ")
        session.commit()
        print("Beauty routine updated successfully.")
    else:
        print("Routine not found.")

def delete_beauty_routine():
    routine_id = int(input("Enter routine ID to delete: "))
    routine = session.query(BeautyRoutine).filter_by(id=routine_id).first()
    if routine:
        session.delete(routine)
        session.commit()
        print("Beauty routine deleted successfully.")
    else:
        print("Routine not found.")

# Assign a product to a routine
def assign_product_to_routine():
    routine_id = int(input("Enter routine ID: "))
    product_id = int(input("Enter product ID: "))
    step = int(input("Enter the step number in the routine (e.g., 1, 2, 3): "))
    
    routine_product = RoutineProduct(routine_id=routine_id, product_id=product_id, step=step)
    session.add(routine_product)
    session.commit()
    print("Product assigned to routine successfully.")

# Main CLI interface
def main():
    while True:
        os.system('clear')
        print("Welcome to the Makeup Kit & Beauty Routine Manager")
        print("1. Manage Beauty Products")
        print("2. Manage Beauty Routines")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            while True:
                print("\nManage Beauty Products")
                print("1. Add Beauty Product")
                print("2. View Beauty Products")
                print("3. Update Beauty Product")
                print("4. Delete Beauty Product")
                print("5. Back to Main Menu")
                product_choice = input("Enter your choice: ")
                
                if product_choice == '1':
                    add_beauty_product()
                elif product_choice == '2':
                    view_beauty_products()
                elif product_choice == '3':
                    update_beauty_product()
                elif product_choice == '4':
                    delete_beauty_product()
                elif product_choice == '5':
                    break
        
        elif choice == '2':
            while True:
                print("\nManage Beauty Routines")
                print("1. Add Beauty Routine")
                print("2. View Beauty Routines")
                print("3. Update Beauty Routine")
                print("4. Delete Beauty Routine")
                print("5. Assign Product to Routine")
                print("6. Back to Main Menu")
                routine_choice = input("Enter your choice: ")
                
                if routine_choice == '1':
                    add_beauty_routine()
                elif routine_choice == '2':
                    view_beauty_routines()
                elif routine_choice == '3':
                    update_beauty_routine()
                elif routine_choice == '4':
                    delete_beauty_routine()
                elif routine_choice == '5':
                    assign_product_to_routine()
                elif routine_choice == '6':
                    break
        
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
