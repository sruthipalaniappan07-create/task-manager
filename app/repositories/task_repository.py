import sqlite3

DATABASE = "tasks.db"


class TaskRepository:

    def __init__(self, database=DATABASE):
        self.database = database
        self.create_table()

    def get_connection(self):
        connection = sqlite3.connect(self.database)
        connection.row_factory = sqlite3.Row
        return connection

    def create_table(self):
        connection = self.get_connection()

        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        """)

        connection.commit()
        connection.close()

    def create_task(self, title, description):
        connection = self.get_connection()

        cursor = connection.execute(
            """
            INSERT INTO tasks (title, description)
            VALUES (?, ?)
            """,
            (title, description)
        )

        connection.commit()

        task_id = cursor.lastrowid

        connection.close()

        return self.get_task_by_id(task_id)

    def get_all_tasks(self):
        connection = self.get_connection()

        rows = connection.execute(
            "SELECT * FROM tasks"
        ).fetchall()

        connection.close()

        return [dict(row) for row in rows]

    def get_task_by_id(self, task_id):
        connection = self.get_connection()

        row = connection.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        connection.close()

        if row is None:
            return None

        return dict(row)

    def update_task(self, task_id, title, description, completed):
        connection = self.get_connection()

        cursor = connection.execute(
            """
            UPDATE tasks
            SET title = ?, description = ?, completed = ?
            WHERE id = ?
            """,
            (title, description, completed, task_id)
        )

        connection.commit()

        connection.close()

        if cursor.rowcount == 0:
            return None

        return self.get_task_by_id(task_id)

    def delete_task(self, task_id):
        connection = self.get_connection()

        cursor = connection.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        connection.commit()

        connection.close()

        return cursor.rowcount > 0
