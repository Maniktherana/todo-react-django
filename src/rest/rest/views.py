import os
import datetime
from bson import ObjectId

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest.model import Todo
from rest.db import MongoConnection


class TodoListView(APIView):
    """
    A CRUD API view for todos
    """

    def __init__(self, *args, **kwargs):
        super(TodoListView, self).__init__(*args, **kwargs)
        self.conn = MongoConnection(
            os.environ["MONGO_HOST"],
            os.environ["MONGO_PORT"],
            "todos_db",
            "todos",
        )

    def get(self, request):
        try:
            todos = self.conn.find()
            serialized_todos = [self.serialize_todo(todo) for todo in todos]
            return Response({"todos": serialized_todos}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "error": f"Internal Server Error: {e}",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        try:
            todo = Todo.parse_obj(request.data)
            todo_dict = todo.dict(by_alias=True, exclude_none=True)
            result = self.conn.insert_one(todo_dict)
            created_todo = self.conn.find_one({"_id": result.inserted_id})
            return Response(
                self.serialize_todo(created_todo),
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": f"Internal Server Error: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request):
        try:
            data = request.data
            todo_id = data.get("_id", None)
            if todo_id is None:
                return Response(
                    {"error": "Missing todo ID in request body"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            todo_id = ObjectId(todo_id)
            existing_todo = self.conn.find_one({"_id": todo_id})
            if not existing_todo:
                return Response(
                    {"error": "Todo not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            # Prepare data for update
            data.pop("_id", None)
            data["updated_at"] = datetime.datetime.utcnow()
            updated_todo = self.conn.update_one({"_id": todo_id}, data)

            if not updated_todo:
                return Response(
                    {"error": "Failed to update todo"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            return Response(
                self.serialize_todo(updated_todo),
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"error": f"Internal Server Error: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request):
        try:
            todo_id = request.data.get("_id", None)
            if todo_id is None:
                return Response(
                    {"error": "Missing todo ID in request body"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Check if todo exists
            todo_id = ObjectId(todo_id)
            existing_todo = self.conn.find_one({"_id": todo_id})
            if not existing_todo:
                return Response(
                    {"error": "Todo not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            self.conn.delete_one({"_id": todo_id})
            return Response(
                {"message": f"Todo {todo_id} deleted successfully"},
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"error": f"Internal Server Error: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @staticmethod
    def serialize_todo(todo):
        serialized_todo = todo.copy()
        serialized_todo["_id"] = str(todo["_id"])
        return serialized_todo
