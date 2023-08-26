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
        number = crud.create_number_for_contact(self.db, py_number, request.contact_id)
        data = number.to_dict()
        return phonebook_pb2.NumberResponse(message='your number added!', **data)


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
