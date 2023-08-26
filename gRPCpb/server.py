import datetime
from concurrent import futures
import logging

import grpc
import phonebook_pb2
import phonebook_pb2_grpc
from phonebook import crud, database, models, schemas


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=database.engin)


class Contact(phonebook_pb2_grpc.ContactServiceServicer):
    def __init__(self):
        self.db = get_db()
        self.db = database.SessionLocal()

    def GetContact(self, request, context):
        contact = crud.get_contact(self.db, request.contact_id)
        data = contact.to_dict()
        data['numbers'] = [phonebook_pb2.NumberResponse(label=n.label, phone=n.phone, is_default=n.is_default) for n in
                           contact.numbers.all()]
        return phonebook_pb2.ContactResponse(message="here you are :)", **data)

    def AddContact(self, request, context):
        py_contact = self.request_to_py_contact(request)
        contact = crud.create_contact(self.db, py_contact)

        data = contact.to_dict()

        return phonebook_pb2.ContactResponse(message="seems like contact added! hooray!", **data)

    def EditContact(self, request, context):
        py_contact = self.request_to_py_contact(request)
        old_contact = crud.get_contact(self.db, request.contact_id)

        contact = crud.update_contact(self.db, py_contact, old_contact)

        return phonebook_pb2.ContactResponse(message="did it! updated~!", **contact.to_dict())

    def DeleteContact(self, request, context):
        contact = crud.get_contact(self.db, request.contact_id)
        crud.delete_contact(self.db, contact)
        return phonebook_pb2.ContactDeleteResponse(message=f"your contact with id {request.contact_id} deleted!")

    def request_to_py_contact(self, request):
        py_contact = schemas.ContactCreate(first_name=request.first_name,
                                           last_name=request.last_name,
                                           nick_name=request.nick_name
                                           )
        return py_contact


class Number(phonebook_pb2_grpc.NumberServiceServicer):
    def __init__(self):
        self.db = database.SessionLocal()

    def AddNumber(self, request, context):
        py_number = schemas.NumberCreate(label=request.label,
                                         is_default=request.is_default,
                                         phone=request.phone,
                                         )
        contact = self.get_contact(request.contact_id)
        number = crud.create_number_for_contact(self.db, py_number, request.contact_id)
        data = number.to_dict()
        data['contact'] = phonebook_pb2.ContactRequest(**contact.to_dict())
        return phonebook_pb2.FullNumberResponse(**data)

    def GetNumber(self, request, context):
        contact = self.get_contact(request.contact_id)
        number = crud.get_number_for_contact(self.db, request.contact_id, request.number_id)
        data = number.to_dict()
        data['contact'] = phonebook_pb2.ContactRequest(**contact.to_dict())
        return phonebook_pb2.FullNumberResponse(**data)

    def EditNumber(self, request, context):
        py_number = schemas.NumberCreate(label=request.label,
                                         is_default=request.is_default,
                                         phone=request.phone,
                                         )
        contact = crud.partial_update_number_for_contact(self.db, request.contact_id, request.number_id, py_number)
        data = py_number.model_dump()
        data['contact'] = phonebook_pb2.ContactRequest(**contact.to_dict())
        return phonebook_pb2.FullNumberResponse(**data)

    def DeleteNumber(self, request, context):
        crud.delete_number(self.db, request.contact_id, request.number_id)
        return phonebook_pb2.NumberDeleteResponse(message="your number deleted!")

    def get_contact(self, contact_id) -> models.Contact:
        return crud.get_contact(self.db, contact_id)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    phonebook_pb2_grpc.add_ContactServiceServicer_to_server(Contact(), server)
    phonebook_pb2_grpc.add_NumberServiceServicer_to_server(Number(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
