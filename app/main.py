from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, database, schemas, crud

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Task API Running"}

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.post("/tasks")
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)
