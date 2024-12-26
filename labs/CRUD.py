from pyparsing import srange

from orm import setup_database, create_session, Password

engine = setup_database("sqlite:///passwords.sqlite")
session = create_session(engine)

def add_password(password, strength):
    new_password = Password(password=password, strength=strength)
    session.add(new_password)
    session.commit()
    print(f"Password '{password}' added with ID: {new_password.id}")
    return new_password.id

def get_password_by_id(id):
    password = session.query(Password).filter_by(id=id).first()
    if password:
        print(f"Password: ID: {password.id}, Password: {password.password}, Strength: {password.strength}")
        return password
    else:
        print(f"Password with ID {id} not found.")
        return None

def get_all_passwords_2():
    passwords = session.query(Password).filter_by(strength=2)
    if passwords==None:
        return []
    chis=set()
    return passwords

def get_all_passwords():
    passwords = session.query(Password).all()
    if passwords==None:
        return []
    for password in passwords:
        print(f"Password: ID: {password.id}, Password: {password.password}, Strength: {password.strength}")
    return passwords

def update_password(id, new_password=None, new_strength=None):
    password = session.query(Password).filter_by(id=id).first()
    if password:
        if new_password:
            password.password = new_password
        if new_strength:
            password.strength = new_strength
        session.commit()
        print(f"Password ID {id} updated.")
        return password
    else:
        print(f"Password with ID {id} not found.")
        return None

def delete_password(id):
    password = session.query(Password).filter_by(id=id).first()
    if password:
        session.delete(password)
        session.commit()
        print(f"Password ID {id} deleted.")
    else:
        print(f"Password with ID {id} not found.")
