from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Todo(BaseModel):
    todo: str = Field(...)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    important: bool = Field(default=False)

    class Config:
        populate_by_name = True
