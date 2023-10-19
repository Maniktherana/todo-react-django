from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import logging, os
from dotenv import load_dotenv

from rest.db import MongoConnection


dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)


class TodoListView(APIView):
    def __init__(self, *args, **kwargs):
        super(TodoListView, self).__init__(*args, **kwargs)
        self.mongo_connection = MongoConnection(
            os.environ["MONGO_HOST"],
            os.environ["MONGO_PORT"],
            "todos_db",
            "todos",
        )

    def get(self, request):
        try:
            todos = self.mongo_connection.collection.find({})
            serialized_todos = [self.serialize_todo(todo) for todo in todos]
            return Response({"todos": serialized_todos}, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"An error occurred while retrieving todos: {e}")
            return Response(
                {
                    "error": "Internal Server Error",
                    "hello": os.environ["DATABASE_NAME"],
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        try:
            data = request.data
            todo_item = data.get("todo", None)
            if todo_item:
                result = self.mongo_connection.collection.insert_one(
                    {"todo": todo_item}
                )
                inserted_id = str(result.inserted_id)
                return Response(
                    {"id": inserted_id, "todo": todo_item},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": "Request data must contain a todo item"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            logging.error(f"An error occurred while adding a todo: {e}")
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @staticmethod
    def serialize_todo(todo):
        serialized_todo = todo.copy()
        serialized_todo["_id"] = str(todo["_id"])
        return serialized_todo
