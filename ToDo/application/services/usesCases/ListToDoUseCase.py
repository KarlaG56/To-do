from typing import Any
from src.ToDo.Domain.Port.PortToDo import PortToDo

class ListToDoUseCase:
    def __init__(self, repository:PortToDo):
        self.repository = repository

    def run(self) -> Any:
        return self.repository.list()
