from flask import Blueprint, jsonify, request

from app.services.task_service import TaskService


task_routes = Blueprint("task_routes", __name__)

service = TaskService()


@task_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    try:
        task = service.create_task(
            data.get("title"),
            data.get("description", "")
        )

        return jsonify(task), 201

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = service.get_all_tasks()

    return jsonify(tasks), 200


@task_routes.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    try:
        task = service.get_task(task_id)

        if task is None:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(task), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    try:
        task = service.update_task(
            task_id,
            data.get("title"),
            data.get("description", ""),
            data.get("completed", False)
        )

        if task is None:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(task), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        deleted = service.delete_task(task_id)

        if not deleted:
            return jsonify({"error": "Task not found"}), 404

        return jsonify({
            "message": "Task deleted successfully"
        }), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400
