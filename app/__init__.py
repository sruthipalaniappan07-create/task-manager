from flask import Flask

from app.routes.task_routes import task_routes


def create_app():
    app = Flask(__name__)

    app.register_blueprint(task_routes)

    @app.route("/")
    def home():
        return {
            "message": "Task Manager API is running"
        }

    return app
