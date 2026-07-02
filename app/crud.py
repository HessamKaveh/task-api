from . import models, schemas

def get_tasks(db):
    return db.query(models.Task).all()

def create_task(db, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
