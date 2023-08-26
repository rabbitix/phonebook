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
        return phonebook_pb2.ContactResponse(message="here you are :)", **data)

    def AddContact(self, request, context):
        py_contact = schemas.ContactCreate(first_name=request.first_name,
                                           last_name=request.last_name,
                                           nick_name=request.nick_name
                                           )
        contact = crud.create_contact(self.db, py_contact)

        data = contact.to_dict()
        data['created'] = data['created'].strftime("%x")
        return phonebook_pb2.ContactResponse(message="seems like contact added! hooray!", **data)


class Number(phonebook_pb2_grpc.NumberServiceServicer):
    def AddNumber(self, request, context):
        return phonebook_pb2.NumberResponse()


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
