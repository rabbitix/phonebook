from fastapi.testclient import TestClient
from phonebook.main import app
import grpc
from gRPCpb import phonebook_pb2_grpc


def before_all(context):
    client = TestClient(app, base_url="http://127.0.0.1:8000")

    context.client = client
    url = "localhost:50051"
    context.channel = grpc.insecure_channel(url)
    context.stub = phonebook_pb2_grpc.ContactServiceStub(context.channel)


def after_all(context):
    context.channel.close()
