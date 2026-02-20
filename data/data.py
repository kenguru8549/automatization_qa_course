from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None  #  обязательно прописывать тип данных
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None  #  обязательно прописывать тип данных
    current_address: str = None  #  обязательно прописывать тип данных
    permanent_address: str = None  #  обязательно прописывать тип данных
    mobile: str = None


@dataclass
class Color:
    color_name: list = None
