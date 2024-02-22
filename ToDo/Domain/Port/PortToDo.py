from abc import ABC, abstractmethod
from typing import Any
from src.ToDo.Domain.entities.ToDo import ToDo


class PortToDo(ABC):
    @abstractmethod
    def list(self) -> Any: pass

    @abstractmethod
    def create(self, todo:ToDo) -> Any: pass

    @abstractmethod
    def update(self,id:str, title: str, text: str, check: str) -> Any: pass

    @abstractmethod
    def delete(self, id:str) -> Any: pass
