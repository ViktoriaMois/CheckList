from datetime import date

from ninja import ModelSchema

from .models import Task


class TaskIn(ModelSchema):
    title: str
    description: str
    urgency: bool

    class Config:
        model = Task
        model_fields = ['title', 'description', 'urgency']


class TaskUpd(ModelSchema):
    class Config:
        model = Task
        model_fields = ['id', 'completed']


class TaskOut(ModelSchema):
    id: int
    title: str
    urgency: bool
    created: date
    description: str
    completed: bool

    class Config:
        model = Task
        model_fields = ['id', 'title', 'urgency', 'created', 'description', 'completed']


