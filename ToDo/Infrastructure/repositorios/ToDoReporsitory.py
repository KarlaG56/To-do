from typing import Any

from src.ToDo.Domain.entities.ToDo import ToDo
from src.ToDo.Domain.Port.PortToDo import PortToDo

class ToDoRepository(PortToDo):

    def __init__(self):
        self.arreglo = []

    def list(self) -> Any:
        return self.arreglo
    def create(self, todo:ToDo) -> Any:
        self.arreglo.append(todo)
        return todo

    def update(self,id:str, title: str, text: str, check: str) -> Any:
        toDo_update = next((todo for todo in self.arreglo if todo.uuid == id), None)
        if toDo_update:
            toDo_update.title = title
            toDo_update.text = text
            toDo_update.check = check
            return toDo_update
        else:
            return None
    def delete(self, id:str) -> Any:
        toDo_index = next((i for i, todo in enumerate(self.arreglo) if todo.uuid == id), None)
        if toDo_index is not None:
            return self.arreglo.pop(toDo_index)
        return None

