from sqlalchemy.orm import Session

from . import models, schemas


def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()


def get_contact_by_first_name_last_name(db: Session, first_name: str = None, last_name: str = None):
    return db.query(models.Contact).filter(
        models.Contact.first_name == first_name or models.Contact.last_name == last_name).first()


def get_contacts(db: Session, limit: int = 30):
    return db.query(models.Contact).limit(limit).all()


def create_contact(db: Session, contact: schemas.ContactCreate):
    con = models.Contact(**contact.model_dump())
    db.add(con)
    db.commit()
    db.refresh(con)
    return con


def update_contact(db: Session, contact: schemas.ContactPartialUpdate, contact_obj: models.Contact):
    obj = contact_obj

    for field, value in vars(contact).items():
        setattr(obj, field, value) if value else None

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def delete_contact(db: Session, contact_obj: models.Contact):
    db.delete(contact_obj)
    db.commit()


def create_number_for_contact(db: Session, number: schemas.NumberCreate, contact_id: int):
    num = models.Number(**number.model_dump(),
                        contact_id=contact_id)
    db.add(num)
    db.commit()
    db.refresh(num)
    return num


def get_contact_numbers(db: Session, contact_id: int) -> list:
    contact_obj = get_contact(db, contact_id)
    return contact_obj.numbers


def partial_update_number_for_contact(db: Session, contact_id: int, number_id: int,
                                      number: schemas.NumberPartialUpdate):
    contact_obj: models.Contact = get_contact(db, contact_id)
    number_obj = contact_obj.numbers.filter(models.Number.id == number_id).first()
    obj = number_obj

    for field, value in vars(number).items():
        setattr(obj, field, value) if value else None

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return contact_obj


def delete_number(db: Session, contact_id: int, number_id: int):
    contact_obj: models.Contact = get_contact(db, contact_id)
    number_obj = contact_obj.numbers.filter(models.Number.id == number_id).first()
    db.delete(number_obj)
    db.commit()


def get_number_for_contact(db: Session, contact_id: int, number_id: int):
    contact_obj: models.Contact = get_contact(db, contact_id)
    number_obj = contact_obj.numbers.filter(models.Number.id == number_id).first()
    return number_obj
