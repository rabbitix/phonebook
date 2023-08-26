its a communication protocol.. 

so you need to use it for your data transfer

i mean only send your data and process it in python, then send back some response


how to generate files??

`python3 -m grpc_tools.protoc -I .   --python_out=. --pyi_out=. --grpc_python_out=. phonebook.proto`


### some docs
- [best practise for gRPC](https://kreya.app/blog/grpc-best-practices/#separate-request-and-response-messages)
- [basic python implementation](https://grpc.io/docs/languages/python/basics/)
- [porto3 language docs](https://protobuf.dev/programming-guides/proto3/)
- [porto-3 spec](https://protobuf.dev/reference/protobuf/proto3-spec/)
- [gRPC Reflection in python](https://grpc.github.io/grpc/python/grpc_reflection.html)
- 