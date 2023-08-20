import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from phonebook import crud, models, schemas
from phonebook.database import SessionLocal, engin

models.Base.metadata.create_all(bind=engin)
app = FastAPI(title="simple phonebook API",
              description="this is a simple phonebook api for practices purposes!"
              )


# region init
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def root():
    return {"hey": "welcome!"}


# endregion

# region contact
@app.get('/contacts/', tags=["Contacts", ], response_model=list[schemas.FullContact])
def contacts_list(db: Session = Depends(get_db)):
    objs = crud.get_contacts(db)
    return objs


@app.post('/contacts/', tags=["Contacts", ], response_model=schemas.FullContact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)


@app.get('/contacts/{contact_id}/', tags=["Contacts", ], response_model=schemas.FullContact)
def contact_detail(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="this contact does not exists!")
    return db_contact


@app.patch('/contacts/{contact_id}/', tags=["Contacts", ], response_model=schemas.FullContact)
def contact_update(contact_id: int, contact: schemas.ContactPartialUpdate, db: Session = Depends(get_db)):
    contact_obj = crud.get_contact(db, contact_id)
    if not contact_obj:
        raise HTTPException(status_code=404, detail="this contact does not exists!")
    return crud.update_contact(db, contact, contact_obj)


@app.delete('/contacts/{contact_id}/', tags=["Contacts", ], )
def contact_delete(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="this contact does not exists!")
    crud.delete_contact(db, db_contact)
    return {"detail": f"contact with id #{db_contact.id} deleted"}


# endregion

# region number

@app.get('/contacts/{contact_id}/numbers/', tags=["Numbers"], response_model=list[schemas.Number])
def list_number_for_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="this contact does not exists!")
    return crud.get_contact_numbers(db, contact_id)


@app.post('/contacts/{contact_id}/numbers/', tags=["Numbers"], response_model=schemas.FullContact)
def create_number_for_contact(contact_id: int, number: schemas.NumberCreate, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="this contact does not exists!")
    number = crud.create_number_for_contact(db, number, contact_id)
    return crud.get_contact(db, contact_id)


@app.patch('/contacts/{contact_id}/numbers/{number_id}/', tags=["Numbers"], response_model=schemas.FullContact)
def create_number_for_contact(contact_id: int, number_id: int, number: schemas.NumberPartialUpdate,
                              db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="this contact does not exists!")
    return crud.partial_update_number_for_contact(db, contact_id, number_id, number)


@app.delete('/contacts/{contact_id}/numbers/{number_id}/', tags=["Numbers"], )
def create_number_for_contact(contact_id: int, number_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="this contact does not exists!")
    crud.delete_number(db, contact_id, number_id)
    return {"detail": f"number of contact #{db_contact.id} deleted"}


# endregion

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=4)
