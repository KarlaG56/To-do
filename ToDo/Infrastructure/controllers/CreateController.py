from src.ToDo.application.services.usesCases.CreateToDoUseCase import CreateToDoUseCase
from src.ToDo.Domain.Port.PortToDo import PortToDo
from src.ToDo.Infrastructure.dto.ToDoReponse import response

class CreateController:
    def __init__(self, toDo_port:PortToDo):
        self.useCase = CreateToDoUseCase(toDo_port)


    def run(self, data):
        return response(response(self.useCase.run(data.get_json())))
