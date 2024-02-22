from src.ToDo.application.services.usesCases.UpdateToDoUseCase import UpdateToDoUseCase
from src.ToDo.Domain.Port.PortToDo import PortToDo
from src.ToDo.Infrastructure.dto.ToDoReponse import response

class UpdateController:
    def __int__(self, toDo_port:PortToDo):
        self.useCase = UpdateToDoUseCase(toDo_port)


    def run(self, id, data):
        return response(self.useCase.run(id, data.get_json()))
