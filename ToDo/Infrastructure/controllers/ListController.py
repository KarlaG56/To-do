from src.ToDo.application.services.usesCases.ListToDoUseCase import ListToDoUseCase
from src.ToDo.Domain.Port.PortToDo import PortToDo
from src.ToDo.Infrastructure.dto.ToDoReponse import response

class ListController:
    def __int__(self, toDo_port:PortToDo):
        self.useCase = ListToDoUseCase(toDo_port)


    def run(self):
        return response(self.useCase.run())
