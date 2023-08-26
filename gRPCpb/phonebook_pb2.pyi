from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NumberRequest(_message.Message):
    __slots__ = ["contact_id", "label", "phone", "is_default"]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    contact_id: int
    label: str
    phone: str
    is_default: bool
    def __init__(self, contact_id: _Optional[int] = ..., label: _Optional[str] = ..., phone: _Optional[str] = ..., is_default: bool = ...) -> None: ...

class NumberResponse(_message.Message):
    __slots__ = ["label", "phone", "is_default", "message"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    label: str
    phone: str
    is_default: bool
    message: str
    def __init__(self, label: _Optional[str] = ..., phone: _Optional[str] = ..., is_default: bool = ..., message: _Optional[str] = ...) -> None: ...

class ContactRequest(_message.Message):
    __slots__ = ["first_name", "last_name", "nick_name"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    nick_name: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., nick_name: _Optional[str] = ...) -> None: ...

class ContactResponse(_message.Message):
    __slots__ = ["message", "first_name", "last_name", "nick_name", "numbers"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    message: str
    first_name: str
    last_name: str
    nick_name: str
    numbers: _containers.RepeatedCompositeFieldContainer[NumberResponse]
    def __init__(self, message: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., nick_name: _Optional[str] = ..., numbers: _Optional[_Iterable[_Union[NumberResponse, _Mapping]]] = ...) -> None: ...

class EditContactRequest(_message.Message):
    __slots__ = ["contact_id", "first_name", "last_name", "nick_name"]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    contact_id: int
    first_name: str
    last_name: str
    nick_name: str
    def __init__(self, contact_id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., nick_name: _Optional[str] = ...) -> None: ...

class ReteriveContactRequest(_message.Message):
    __slots__ = ["contact_id"]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    contact_id: int
    def __init__(self, contact_id: _Optional[int] = ...) -> None: ...

class ContactDeleteResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
