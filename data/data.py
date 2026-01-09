from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None  #  обязательно прописывать тип данных
    email: str = None  #  обязательно прописывать тип данных
    current_address: str = None  #  обязательно прописывать тип данных
    permanent_address: str = None  #  обязательно прописывать тип данных
