from flask import Blueprint, request, jsonify

from src.ToDo.Infrastructure.controllers.CreateController import CreateController
from src.ToDo.Infrastructure.controllers.DeleteController import DeleteController
from src.ToDo.Infrastructure.controllers.UpdateController import UpdateController
from src.ToDo.Infrastructure.controllers.ListController import ListController
from src.ToDo.Infrastructure.repositorios.ToDoReporsitory import ToDoRepository

todo_blueprint = Blueprint("To-do", __name__)

repository = ToDoRepository
create_controller = CreateController(repository)
delete_controller = DeleteController(repository)
update_controller = UpdateController(repository)
list_controller = ListController(repository)


@todo_blueprint.route("/", methods=["GET"])
def list():
    return jsonify(list_controller.run())

@todo_blueprint.route("/", methods=["POST"])
def create():
    return jsonify(create_controller.run(request))

@todo_blueprint.route("/<string:id>", methods=["PUT"])
def update(id):
    return jsonify(update_controller.run(id, request))

@todo_blueprint.route("/<string:id>", methods=["DELETE"])
def delete(id):
    return jsonify(delete_controller.run(id))


