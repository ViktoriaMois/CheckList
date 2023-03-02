from typing import List

from ninja import NinjaAPI
from .schemas import *
from .models import *
from django.shortcuts import get_object_or_404

api = NinjaAPI()


@api.post("/task", tags=['Tasks'])
def create_task(request, payload: TaskIn):
    task = Task.objects.create(**payload.dict())
    return {"id": task.id}


@api.get("/task/{task_id}", tags=['Tasks'], response=TaskOut)
def get_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    return task


@api.patch("/task/{task_id}", tags=['Tasks'])
def update_task(request, task_id: int, payload: TaskUpd):
    task = get_object_or_404(Task, id=task_id)
    for atr, value in payload.dict().items():
        setattr(task, atr, value)
    task.save()
    return {"Success": True}


# @api.put("/tasks/{task_id}", tags=['Tasks'])
# def update_task(request, task_id: int, payload: TaskIn):
#     task = get_object_or_404(Task, id=task_id)
#     for atr, value in payload.dict().items():
#         setattr(task, atr, value)
#     task.save()
#     return {"Success": True}


@api.delete("/task/{task_id}", tags=['Tasks'])
def delete_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return {"Success": True}


@api.get("/tasks", tags=['Tasks'], response=List[TaskOut])
def list_tasks(request):
    tasks = Task.objects.all()
    return tasks
